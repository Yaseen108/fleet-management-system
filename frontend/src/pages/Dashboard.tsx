import { useEffect, useState } from "react";
import api from "../api/axios";
import Layout from "../components/Layout";
import Card from "../components/Card";
import FuelCostChart from "../components/FuelCostChart";
import FuelLitresChart from "../components/FuelLitresChart";
import AveragePriceChart from "../components/AveragePriceChart";

export default function Dashboard() {
  const [vehicleFuelCosts, setVehicleFuelCosts] = useState([]);
  const [vehicleFuelLitres, setVehicleFuelLitres] = useState([]);
  const [averageFuelPrice, setAverageFuelPrice] = useState([]);

  useEffect(() => {
    api.get("/analytics/fuel-cost-per-vehicle")
      .then((res) => {
        setVehicleFuelCosts(res.data);
      })
      .catch((err) => {
        console.error(err);
      });
  }, []);

  useEffect(() => {
    api.get("/analytics/average-price-per-litre")
      .then((res) => {
        setAverageFuelPrice(res.data);
      })
      .catch((err) => {
        console.error(err);
      });
  }, []);

  useEffect(() => {
    api.get("/analytics/fuel-litres-per-vehicle")
      .then((res) => {
        setVehicleFuelLitres(res.data);
      })
      .catch((err) => {
        console.error(err);
      });
  }, []);

  return (
    <Layout>
      <h1 className="text-2xl font-bold mb-6">Dashboard</h1>

      {/* Grid Layout */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

        {/* Chart Card */}
        <Card title="Fuel Cost per Vehicle">
          <FuelCostChart data={vehicleFuelCosts} />
        </Card>

        {/* Placeholder for next chart */}
        <Card title="Fuel Litres per Vehicle">
          <FuelLitresChart data={vehicleFuelLitres} />
        </Card>

        <Card title="Average Fuel Price per Vehicle">
          <AveragePriceChart data={averageFuelPrice} />
        </Card>

      </div>
    </Layout>
  );
}