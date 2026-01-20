export default function VideoPlayer({ jobId, children }) {
  if (!jobId) {
    return (
      <div className="h-full flex items-center justify-center text-zinc-500">
        Upload a video to start
      </div>
    );
  }

  return (
    <div className="relative w-full h-[70vh]">
      <video
        src={`http://127.0.0.1:8000/videos/${jobId}_annotated.mp4`}
        controls
        className="w-full h-full object-contain"
      />
      {children}
    </div>
  );
}
