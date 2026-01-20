import { useEffect, useState } from "react";
import { getDetections } from "../api/roadrunner";

// DIRECT components
import ModeSelector from "../components/ModeSelector.jsx";
import VideoUploader from "../components/video/VideoUploader.jsx";
import DetectionOverlay from "../components/DetectionOverlay.jsx";

// video folder components
import VideoPlayer from "../components/video/VideoPlayer.jsx";
import DepthBar from "../components/video/DepthBar.jsx";

// pages
import Results from "./Results.jsx";

export default function Dashboard() {
  const [mode, setMode] = useState("video"); // video | live | photo
  const [jobId, setJobId] = useState(null);
  const [detections, setDetections] = useState([]);

  // Poll detections
  useEffect(() => {
    if (!jobId) return;

    const interval = setInterval(async () => {
      try {
        const res = await getDetections(jobId);
        setDetections(res.data || []);
      } catch (e) {
        console.error(e);
      }
    }, 2000);

    return () => clearInterval(interval);
  }, [jobId]);

  return (
  <div style={{ padding: 20 }}>
    <div style={{ display: "grid", gridTemplateColumns: "3fr 6fr 3fr", gap: 16 }}>

      {/* LEFT */}
      <div className="panel fade-in">
        <h3 style={{ color: "var(--primary)" }}>Controls</h3>

        <ModeSelector mode={mode} setMode={setMode} />

        {mode === "video" && (
          <div style={{ marginTop: 12 }}>
            <VideoUploader onJobCreated={setJobId} />
          </div>
        )}

        <div style={{ marginTop: 16, fontSize: 12, color: "var(--muted)" }}>
          MODE: {mode.toUpperCase()} <br />
          JOB: {jobId || "—"}
        </div>
      </div>

      {/* MAIN VIEW */}
        <div className="col-span-6 bg-black rounded-xl p-2 relative">
          {!jobId && (
            <div className="flex items-center justify-center h-full text-zinc-500">
              Upload a video to start
            </div>
          )}

          {jobId && (
            <video
              src={`http://127.0.0.1:8000/api/v1/videos/${jobId}/annotated.mp4`}
              controls
              autoPlay
              className="w-full rounded"
            />
          )}
      </div>


      {/* RIGHT */}
      <div className="panel fade-in">
        <h3 style={{ color: "var(--primary)" }}>Detections</h3>

        {detections.length === 0 && (
          <p style={{ color: "var(--muted)" }}>No detections yet</p>
        )}

        {detections.map((d, i) => (
          <div key={i} className="card">
            <b>Pothole #{d.track_id ?? "?"}</b><br />
            <span style={{ fontSize: 12, color: "var(--muted)" }}>
              {(d.confidence * 100).toFixed(1)}%
            </span>
          </div>
        ))}
      </div>

    </div>

    {jobId && <Results jobId={jobId} />}
  </div>
);

}
