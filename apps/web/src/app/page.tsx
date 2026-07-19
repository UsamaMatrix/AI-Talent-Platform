import Link from "next/link";

export default function HomePage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center bg-gradient-to-b from-brand-50 to-white px-4">
      <h1 className="text-4xl font-bold text-brand-900 mb-4">AI Talent Platform</h1>
      <p className="text-lg text-gray-600 mb-8 text-center max-w-xl">
        Open-source AI-powered talent assessment, recruiting, coding interviews and LLM evaluation.
      </p>
      <div className="flex gap-4">
        <Link
          href="/sign-in"
          className="rounded-lg bg-brand-500 px-6 py-3 text-white font-medium hover:bg-brand-900 transition-colors"
        >
          Get Started
        </Link>
        <a
          href="https://github.com/UsamaMatrix/AI-Talent-Platform"
          target="_blank"
          rel="noopener noreferrer"
          className="rounded-lg border border-gray-300 px-6 py-3 text-gray-700 font-medium hover:bg-gray-50 transition-colors"
        >
          GitHub
        </a>
      </div>
    </main>
  );
}
