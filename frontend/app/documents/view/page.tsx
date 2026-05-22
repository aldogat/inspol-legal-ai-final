import { Suspense } from "react";
import DocumentViewInner from "./DocumentViewInner";

export default function DocumentViewPage() {
  return (
    <Suspense fallback={<div>Cargando página...</div>}>
      <DocumentViewInner />
    </Suspense>
  );
}
