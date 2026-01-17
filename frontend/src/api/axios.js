import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/api/v1"
});

let token = null;

export const initAuth = async () => {
  const res = await axios.get("http://localhost:8000/api/v1/auth/ping");
  token = res.data.token;
};

api.interceptors.request.use(config => {
  if (token) {
    config.headers["X-ROADDRUNNER-TOKEN"] = token;
  }
  return config;
});

export default api;
