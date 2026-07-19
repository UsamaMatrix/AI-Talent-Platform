"use client";

import { useQuery } from "@tanstack/react-query";

async function fetchHealth(): Promise<{ status: string }> {
  const res = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000"}/api/v1/health`
  );
  if (!res.ok) throw new Error("API unreachable");
  return res.json() as Promise<{ status: string }>;
}

export function ApiHealthIndicator() {
  const { data, isLoading, isError } = useQuery({
    queryKey: ["api-health"],
    queryFn: fetchHealth,
    refetchInterval: 30_000,
  });

  if (isLoading) return <span className="text-xs text-gray-400">Checking API…</span>;
  if (isError) return <span className="text-xs text-red-500">● API unreachable</span>;
  return (
    <span className="text-xs text-green-600">
      ● API {data?.status ?? "unknown"}
    </span>
  );
}
