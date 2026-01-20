export default function DepthBar({ confidence, area }) {
  const severity = Math.min(1, confidence * area * 4);

  


  return (
    <div className="mt-1">
      <div className="h-2 w-full bg-zinc-700 rounded">
        <div
          className={`h-2 rounded ${
            severity > 0.7
              ? "bg-red-500"
              : severity > 0.4
              ? "bg-yellow-400"
              : "bg-green-500"
          }`}
          style={{ width: `${severity * 100}%` }}
        />
      </div>
      <p className="text-xs text-zinc-400 mt-1">
        Severity: {(severity * 100).toFixed(0)}%
      </p>
    </div>
  );
}
