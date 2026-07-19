import { test, expect } from "@playwright/test";

test("landing page loads", async ({ page }) => {
  await page.goto("/");
  await expect(page.getByRole("heading", { name: /AI Talent Platform/i })).toBeVisible();
  await expect(page.getByRole("link", { name: /Get Started/i })).toBeVisible();
});

test("sign-in page loads", async ({ page }) => {
  await page.goto("/sign-in");
  await expect(page.getByRole("heading", { name: /Sign in/i })).toBeVisible();
});
