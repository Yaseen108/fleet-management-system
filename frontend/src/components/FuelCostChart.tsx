import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid
} from "recharts";

type Props = {
  data: {
    vehicle: string;
    total_cost: number;
  }[];
};

export default function FuelCostChart({ data }: Props) {
  return (
    <div className="w-full h-[300px]">
      <ResponsiveContainer width="100%" height="100%">
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          console.log(data);
          <XAxis dataKey="vehicle" />
          <YAxis />

          <Tooltip />

          <Bar dataKey="total_cost" fill="#3b82f6" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}