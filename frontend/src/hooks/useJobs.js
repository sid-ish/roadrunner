import { useEffect, useState } from "react";

export const useJobs = () => {
  const [jobs, setJobs] = useState([]);
  return { jobs };
};
