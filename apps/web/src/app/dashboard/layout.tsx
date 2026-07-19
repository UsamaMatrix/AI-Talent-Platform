import { ApiHealthIndicator } from "@/components/api-health-indicator";
import Link from "next/link";

const NAV_ITEMS = [
  { href: "/dashboard", label: "Overview" },
  { href: "/dashboard/resume", label: "Resume Intelligence" },
  { href: "/dashboard/recruiter", label: "AI Recruiter" },
  { href: "/dashboard/coding", label: "Coding Interview" },
  { href: "/dashboard/voice", label: "Voice Interview" },
  { href: "/dashboard/evaluation", label: "AI Evaluation" },
];

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex min-h-screen">
      <aside className="w-56 border-r bg-white flex flex-col">
        <div className="p-4 font-bold text-brand-900 border-b">AI Talent Platform</div>
        <nav className="flex-1 p-2 space-y-1">
          {NAV_ITEMS.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="block rounded-md px-3 py-2 text-sm text-gray-700 hover:bg-brand-50 hover:text-brand-900 transition-colors"
            >
              {item.label}
            </Link>
          ))}
        </nav>
        <div className="p-4 border-t">
          <ApiHealthIndicator />
        </div>
      </aside>
      <main className="flex-1 bg-gray-50 p-6">{children}</main>
    </div>
  );
}
