import { useState } from "react";
import { createJob } from "../api/jobs.api";

export default function NewAnalysis() {
  const [url, setUrl] = useState("");
  const [status, setStatus] = useState("");

  const submit = async () => {
    try {
      const res = await createJob({ youtube_url: url });
      setStatus(`Job created: ${res.data.job_id}`);
    } catch {
      setStatus("Backend not reachable");
    }
  };

  return (
    <div className="bg-card p-6 rounded shadow max-w-xl">
      <h1 className="text-xl font-bold mb-4">New Analysis</h1>

      <input
        className="border p-2 w-full"
        placeholder="YouTube URL"
        value={url}
        onChange={e => setUrl(e.target.value)}
      />

      <button
        onClick={submit}
        className="mt-4 bg-primary text-white px-4 py-2 rounded"
      >
        Start Analysis
      </button>

      {status && <p className="mt-4">{status}</p>}
    </div>
  );
}