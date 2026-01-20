import DetectionOverlay from "./DetectionOverlay";

export default function VideoPlayer({ jobId, detections }) {
  if (!jobId) {
    return (
      <div className="text-zinc-500 text-center py-10">
        Upload a video to start
      </div>
    );
  }

  return (
    <div className="relative w-full">
      <video
        src={`/api/v1/videos/${jobId}/annotated.mp4`}
        controls
        autoPlay
        className="w-full rounded-xl"
      />

      <DetectionOverlay detections={detections} />
    </div>
  );
}
