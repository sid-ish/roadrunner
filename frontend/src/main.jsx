import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./styles/theme.css";
import { initAuth } from "./api/axios";

initAuth();

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
