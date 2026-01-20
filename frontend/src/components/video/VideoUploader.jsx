import { useState } from "react";
import { uploadVideo } from "../../api/roadrunner";

export default function VideoUploader({ onJobCreated }) {
  const [loading, setLoading] = useState(false);

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setLoading(true);
    try {
      const res = await uploadVideo(file);
      onJobCreated(res.data.job_id);
    } catch (err) {
      console.error(err.response?.data || err);
      alert("Upload failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 rounded-xl border border-cyan-500/30">
      <input type="file" accept="video/*" onChange={handleUpload} />
      {loading && <p className="text-sm text-cyan-400 mt-2">Uploading…</p>}
    </div>
  );
}
