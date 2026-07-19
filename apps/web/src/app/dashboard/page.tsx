export default function DashboardPage() {
  return (
    <div>
      <h1 className="text-2xl font-bold text-gray-900 mb-2">Dashboard</h1>
      <p className="text-gray-500">
        Platform modules are under active development. Check the{" "}
        <a
          href="https://github.com/UsamaMatrix/AI-Talent-Platform"
          className="text-brand-500 underline"
          target="_blank"
          rel="noopener noreferrer"
        >
          roadmap
        </a>{" "}
        for progress.
      </p>
    </div>
  );
}
