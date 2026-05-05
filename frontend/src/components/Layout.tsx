export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-gray-100">
      
      {/* Navbar */}
      <header className="bg-white shadow p-4">
        <h1 className="text-xl font-semibold">Fleet Management</h1>
      </header>

      {/* Main Content */}
      <main className="min-h-screen bg-gray-100 p-6">
        {children}
      </main>
    </div>
  );
}