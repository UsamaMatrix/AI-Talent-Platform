import { render, screen } from "@testing-library/react";
import { describe, it, expect, vi } from "vitest";

// Mock TanStack Query
vi.mock("@tanstack/react-query", () => ({
  useQuery: () => ({ data: { status: "ok" }, isLoading: false, isError: false }),
}));

import { ApiHealthIndicator } from "@/components/api-health-indicator";

describe("ApiHealthIndicator", () => {
  it("renders ok status", () => {
    render(<ApiHealthIndicator />);
    expect(screen.getByText(/API ok/i)).toBeInTheDocument();
  });
});
