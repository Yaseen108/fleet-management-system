import {
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
  LineChart,
  Line
} from "recharts";

type Props = {
  data: {
    vehicle: string;
    avg_price: number;
  }[];
};

export default function AveragePriceChart({ data }: Props) {
  return (
    <div className="w-full h-[300px]">
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="vehicle" />
          <YAxis />

          <Tooltip />

          <Line dataKey="avg_price" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}