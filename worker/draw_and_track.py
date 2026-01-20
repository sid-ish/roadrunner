import os
import cv2
import sqlite3

DB_PATH = "data/db/roadrunner.db"

def draw_and_track(job_id):
    frames_dir = f"data/frames/{job_id}"
    out_dir = f"data/frames_annotated/{job_id}"
    os.makedirs(out_dir, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    frames = sorted(os.listdir(frames_dir))

    for idx, frame_name in enumerate(frames):
        frame = cv2.imread(os.path.join(frames_dir, frame_name))
        h, w = frame.shape[:2]

        cur.execute("""
            SELECT track_id, x1, y1, x2, y2, confidence
            FROM detections
            WHERE job_id=? AND frame_index=?
        """, (job_id, idx))

        for tid, x1, y1, x2, y2, conf in cur.fetchall():
            x1, y1, x2, y2 = int(x1*w), int(y1*h), int(x2*w), int(y2*h)

            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.putText(
                frame,
                f"Pothole #{tid} | {int(conf*100)}%",
                (x1, y1-8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0,255,0),
                2
            )

        cv2.imwrite(os.path.join(out_dir, frame_name), frame)

    conn.close()
    print("✅ Drawing done (YOLO-tracked)")
