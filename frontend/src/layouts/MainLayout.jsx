import { Outlet } from "react-router-dom";
import Navbar from "../components/common/Navbar";

export default function MainLayout() {
  return (
    <div className="min-h-screen bg-bg text-text">
      <Navbar />
      <main className="p-6">
        <Outlet />
      </main>
    </div>
  );
}
