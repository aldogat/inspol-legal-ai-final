// Mock API para demo estática – reemplaza las llamadas reales con datos de ejemplo

const sampleClientes = [
  { id: 1, nombre: "García y Asociados", email: "contacto@garcia.com", telefono: "555-1234" },
  { id: 2, nombre: "Corporativo LM", email: "info@lm.com", telefono: "555-5678" },
  { id: 3, nombre: "Servicios Legales del Norte", email: "norte@legal.com", telefono: "555-9012" },
];

const sampleExpedientes = [
  { id: 1, titulo: "Caso 001 – Laboral", cliente: "García y Asociados", estado: "En trámite" },
  { id: 2, titulo: "Caso 002 – Civil", cliente: "Corporativo LM", estado: "Resuelto" },
  { id: 3, titulo: "Caso 003 – Penal", cliente: "Servicios Legales del Norte", estado: "Investigación" },
];

const sampleContratos = [
  { id: 1, titulo: "Contrato de arrendamiento", cliente: "García y Asociados", vigencia: "2025-01-01 a 2026-01-01" },
  { id: 2, titulo: "Convenio de confidencialidad", cliente: "Corporativo LM", vigencia: "2025-03-15 a 2027-03-15" },
];

const sampleEventos = [
  { id: 1, titulo: "Audiencia inicial Caso 001", fecha: "2025-06-01", tipo: "Presencial" },
  { id: 2, titulo: "Reunión de mediación", fecha: "2025-06-05", tipo: "Virtual" },
];

const sampleEstadisticas = {
  total_casos: 12,
  casos_activos: 5,
  clientes_nuevos: 3,
  ingresos_mensuales: "$45,000 MXN",
};

const mockData: Record<string, any> = {
  "/api/v1/clientes": sampleClientes,
  "/api/v1/expedientes": sampleExpedientes,
  "/api/v1/contratos": sampleContratos,
  "/api/v1/eventos": sampleEventos,
  "/api/v1/estadisticas": sampleEstadisticas,
};

export async function apiFetch<T = any>(path: string, options?: RequestInit): Promise<T> {
  // Extraer la parte final de la ruta para buscar en mockData
  const cleanPath = path.replace(/^https?:\/\/[^/]+/, ""); // por si viene una URL absoluta
  const key = Object.keys(mockData).find(k => cleanPath.includes(k));
  if (key) {
    return Promise.resolve(mockData[key] as T);
  }
  // Para cualquier otra ruta, devolvemos un array vacío
  return Promise.resolve([] as unknown as T);
}
