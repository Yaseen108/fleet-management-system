import { useEffect, useState } from "react";
import api from "../api/axios";

export default function Dashboard() {
  const [costData, setCostData] = useState<any[]>([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    const res = await api.get("/analytics/fuel-cost-per-vehicle");
    setCostData(res.data);
  };

  return (
    <div style={{ padding: 50 }}>
      <h1>Dashboard</h1>

      <h3>Fuel Cost Per Vehicle</h3>

      {costData.map((item, index) => (
        <div key={index}>
          {item.vehicle}: R{item.total_cost}
        </div>
      ))}
    </div>
  );
}