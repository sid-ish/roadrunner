import React from "react";
import Navbar from "./components/common/Navbar";
import Dashboard from "./pages/Dashboard";

export default function App() {
  return (
    <div className="min-h-screen bg-bg text-text">
      <Navbar />
      <div className="p-6">
        <Dashboard />
      </div>
    </div>
  );
}
