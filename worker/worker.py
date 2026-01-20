import os
import sys
import cv2
import torch
import subprocess
from redis import Redis
from sqlalchemy.orm import Session
from ultralytics import YOLO
from draw_and_track import draw_and_track

sys.path.append("backend")

from app.core.config import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_JOB_QUEUE
from app.db.session import SessionLocal
from app.db.models.job import Job
from app.db.models.detection import Detection

VIDEO_DIR = "data/videos"
FRAME_DIR = "data/frames"

os.makedirs(VIDEO_DIR, exist_ok=True)
os.makedirs(FRAME_DIR, exist_ok=True)

# Redis
redis_client = Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    decode_responses=True,
)

# YOLO
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
model = YOLO("worker/models/best.pt")
model.to(DEVICE)

def update_job(job_id, **fields):
    db = SessionLocal()
    try:
        job = db.query(Job).filter(Job.id == job_id).first()
        if job:
            for k, v in fields.items():
                setattr(job, k, v)
            db.commit()
    finally:
        db.close()

#def download_video(job_id, url):
#    out = os.path.join(VIDEO_DIR, f"{job_id}.mp4")
#    subprocess.run(
 #       [
  #          "yt-dlp",
   #         "--cookies", "cookies.txt",
    #        "-o", out,
     #       url,
      #  ],
       # check=True,
   ##return out  

def download_video(job_id, url):
    # TEMP: use local file instead of YouTube
    src = os.path.join(VIDEO_DIR, "test.mp4")
    dst = os.path.join(VIDEO_DIR, f"{job_id}.mp4")

    if not os.path.exists(src):
        raise RuntimeError("test.mp4 not found in data/videos/")

    import shutil
    shutil.copy(src, dst)
    return dst



def extract_frames(job_id, video_path):
    out_dir = os.path.join(FRAME_DIR, job_id)
    os.makedirs(out_dir, exist_ok=True)

    subprocess.run(
        [
            "ffmpeg",
            "-i", video_path,
            "-vf", "fps=6",
            os.path.join(out_dir, "%06d.jpg"),
        ],
        check=True,
    )
    return out_dir

def run_yolo(job_id, frames_path):
    db: Session = SessionLocal()

    for idx, frame_name in enumerate(sorted(os.listdir(frames_path))):
        img_path = os.path.join(frames_path, frame_name)
        img = cv2.imread(img_path)
        if img is None:
            continue

        h, w = img.shape[:2]

        results = model.track(
            img,
            persist=True,
            conf=0.4,
            iou=0.5,
            tracker="bytetrack.yaml"
        )

        for r in results:
            if r.boxes is None:
                continue

            for box in r.boxes:
                if box.id is None:
                    continue

                track_id = int(box.id[0])
                conf = float(box.conf[0])
                x1, y1, x2, y2 = map(float, box.xyxy[0])

                det = Detection(
                    job_id=job_id,
                    frame_index=idx,
                    track_id=track_id,
                    label="pothole",
                    confidence=conf,
                    x1=x1 / w,
                    y1=y1 / h,
                    x2=x2 / w,
                    y2=y2 / h,
                )
                db.add(det)

    db.commit()
    db.close()


def main():
    print("🚀 Worker running with YOLO")

    while True:
        _, job_id = redis_client.blpop(REDIS_JOB_QUEUE)
        print(f"▶️ Job {job_id}")

        update_job(job_id, status="processing")

        db = SessionLocal()
        job = db.query(Job).filter(Job.id == job_id).first()
        db.close()

        if not job:
            continue

        try:
            # 1️⃣ Download video
            video_path = download_video(job_id, job.youtube_url)

            # 2️⃣ Extract frames
            frames_path = extract_frames(job_id, video_path)

            # 3️⃣ YOLO inference
            run_yolo(job_id, frames_path)

            # 4️⃣ Draw + track potholes across frames
            draw_and_track(job_id)

            update_job(job_id, status="done")
            print(f"✅ Job {job_id} done")


        except Exception as e:
            print("❌", e)
            update_job(job_id, status="failed")

if __name__ == "__main__":
    main()
