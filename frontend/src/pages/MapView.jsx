import { useEffect, useState } from "react";
import { getDetections } from "../api/roadrunner";
import { MapContainer, TileLayer, Circle } from "react-leaflet";

export default function MapView({ jobId }) {
  const [detections, setDetections] = useState([]);

  useEffect(() => {
    if (!jobId) return;
    getDetections(jobId).then(res => setDetections(res.data));
  }, [jobId]);

  return (
    <MapContainer
      center={[12.9716, 77.5946]}
      zoom={13}
      className="h-full w-full rounded-xl"
    >
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />

      {detections.map((d, i) => (
        <Circle
          key={i}
          center={[d.lat, d.lng]}   // backend-ready
          radius={20 + d.confidence * 40}
          pathOptions={{
            color:
              d.confidence < 0.5
                ? "green"
                : d.confidence < 0.75
                ? "orange"
                : "red",
          }}
        />
      ))}
    </MapContainer>
  );
}
