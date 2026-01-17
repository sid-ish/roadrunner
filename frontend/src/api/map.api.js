import api from "./axios";
export const getMapData = (jobId) => api.get(`/map/${jobId}`);
