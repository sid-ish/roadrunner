import React from "react";
import Navbar from "./components/common/Navbar";

export default function App() {
  return (
    <div className="min-h-screen bg-bg text-text">
      <Navbar />
      <div className="p-6">
        <h1 className="text-2xl font-bold">Dashboard</h1>
      </div>
    </div>
  );
}
