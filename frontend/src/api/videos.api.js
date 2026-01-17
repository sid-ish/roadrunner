import api from "./axios";
export const getVideos = () => api.get("/videos");
