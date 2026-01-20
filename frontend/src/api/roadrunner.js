import axios from "axios";

export const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1",
  headers: {
    "X-ROADDRUNNER-TOKEN": "PASTE_TOKEN_HERE"
  }
});

export const uploadVideo = (file) => {
  const form = new FormData();
  form.append("file", file);
  return api.post("/videos/upload", form);
};

export const getDetections = (jobId) =>
  api.get(`/detections/${jobId}`);
