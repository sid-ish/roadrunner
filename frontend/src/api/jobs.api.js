import api from "./axios";

export const createJob = (data) => api.post("/jobs", data);
export const getJobStatus = (id) => api.get(`/jobs/${id}`);
