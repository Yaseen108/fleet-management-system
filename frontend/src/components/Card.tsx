export default function Card({ title, children }: any) {
  return (
    <div className="bg-white rounded-2xl shadow p-4 h-[350px] flex flex-col">
      <h2 className="text-lg font-semibold mb-4">{title}</h2>
      <div className="flex-1">
        {children}
      </div>
    </div>
  );
}