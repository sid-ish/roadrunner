import { useEffect, useState } from "react";
import { getDetections } from "../api/roadrunner";
import jsPDF from "jspdf";

export default function Results({ jobId }) {
  const [detections, setDetections] = useState([]);

  useEffect(() => {
    if (!jobId) return;

    getDetections(jobId).then((res) => {
      setDetections(res.data || []);
    });
  }, [jobId]);

  const potholes = detections.length;

  const avgConfidence =
    potholes === 0
      ? 0
      : (
          detections.reduce((sum, d) => sum + d.confidence, 0) /
          potholes
        ).toFixed(2);

  const severity = { low: 0, medium: 0, high: 0 };

  detections.forEach((d) => {
    if (d.confidence < 0.5) severity.low++;
    else if (d.confidence < 0.75) severity.medium++;
    else severity.high++;
  });

  const exportPDF = () => {
    const pdf = new jsPDF();
    pdf.text(`Job ${jobId} Results`, 10, 10);

    detections.forEach((d, i) => {
      pdf.text(
        `#${i + 1} | Track ${d.track_id ?? "-"} | ${(d.confidence * 100).toFixed(
          1
        )}%`,
        10,
        20 + i * 6
      );
    });

    pdf.save(`job_${jobId}_report.pdf`);
  };

  return (
    <div className="grid grid-cols-3 gap-6 mt-6">

      {/* SUMMARY */}
      <div className="bg-zinc-900 p-4 rounded-xl">
        <h3 className="font-bold mb-2">Summary</h3>
        <p>Total potholes: <b>{potholes}</b></p>
        <p>Avg confidence: <b>{avgConfidence}</b></p>
      </div>

      {/* SEVERITY */}
      <div className="bg-zinc-900 p-4 rounded-xl">
        <h3 className="font-bold mb-2">Severity</h3>
        <p className="text-green-400">Low: {severity.low}</p>
        <p className="text-yellow-400">Medium: {severity.medium}</p>
        <p className="text-red-400">High: {severity.high}</p>
      </div>

      {/* EXPORT */}
      <div className="bg-zinc-900 p-4 rounded-xl">
        <h3 className="font-bold mb-2">Export</h3>
        <button
          className="w-full bg-red-600 hover:bg-red-500 px-3 py-2 rounded"
          onClick={exportPDF}
        >
          Export PDF
        </button>
      </div>

    </div>
  );
}
