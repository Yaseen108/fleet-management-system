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
    total_litres: number;
  }[];
};

export default function FuelLitresChart({ data }: Props) {
  return (
    <div className="w-full h-[300px]">
      <ResponsiveContainer>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="vehicle" />
          <YAxis />

          <Tooltip />

          <Bar dataKey="total_litres" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}