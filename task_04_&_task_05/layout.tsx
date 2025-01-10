/**
 * Root layout component for the FAQ bot application.
 */

import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "LangChain FAQ Bot",
  description: "A simple FAQ bot built with Next.js, TypeScript, and LangChain",
};

/**
 * RootLayout component that wraps all pages in the application
 * @param {Object} props - Component properties
 * @param {React.ReactNode} props.children - Child components to be rendered within the layout
 * @returns {JSX.Element} The root layout structure with proper HTML setup
 */
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="bg-white dark:bg-gray-900">{children}</body>
    </html>
  );
}
