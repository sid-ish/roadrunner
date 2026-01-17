export default function JobCard({ job }) {
  return (
    <div className="bg-card p-4 rounded shadow">
      <div className="font-bold">{job.job_id}</div>
      <div>Status: {job.status}</div>
    </div>
  );
}
