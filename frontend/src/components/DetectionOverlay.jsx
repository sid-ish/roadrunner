export default function DetectionOverlay({ detections }) {
  return (
    <>
      {detections.map((d, i) => {
        const color =
          d.confidence < 0.5
            ? "border-green-400"
            : d.confidence < 0.75
            ? "border-yellow-400"
            : "border-red-500";

        return (
          <div
            key={i}
            className={`absolute border-2 ${color}`}
            style={{
              left: `${d.x1 * 100}%`,
              top: `${d.y1 * 100}%`,
              width: `${(d.x2 - d.x1) * 100}%`,
              height: `${(d.y2 - d.y1) * 100}%`,
            }}
          >
            <span className="bg-black/70 text-xs px-1">
              {(d.confidence * 100).toFixed(0)}%
            </span>
          </div>
        );
      })}
    </>
  );
}
