const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export async function apiFetch<T = any>(
  path: string,
  options?: RequestInit
): Promise<T> {
  const token = typeof window !== "undefined" ? localStorage.getItem("auth_token") : null;

  // Construir URL completa si no es absoluta
  const url = path.startsWith("http") ? path : `${API_BASE}${path}`;

  const res = await fetch(url, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...options?.headers,
    },
  });

  if (!res.ok) {
    throw new Error(`Error ${res.status}: ${res.statusText}`);
  }

  return res.json() as Promise<T>;
}
