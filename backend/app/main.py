import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.api.v1 import (
    chat, expedientes, clientes, contratos, eventos,
    finanzas, reportes, auth, estadisticas,
    archivos, documentos, archivos_contratos,
    historial, analisis
)

load_dotenv()

app = FastAPI(title="INSPOL")

# 🔥 CORS GLOBAL (ESTO ARREGLA TU ERROR)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://inspol-legal-frontend.vercel.app",
        "http://localhost:3000",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTERS
app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(chat.router, prefix="/api/v1/chat")
app.include_router(expedientes.router, prefix="/api/v1/expedientes")
app.include_router(clientes.router, prefix="/api/v1/clientes")
app.include_router(contratos.router, prefix="/api/v1/contratos")
app.include_router(eventos.router, prefix="/api/v1/eventos")
app.include_router(finanzas.router, prefix="/api/v1/finanzas")
app.include_router(reportes.router, prefix="/api/v1/reportes")
app.include_router(estadisticas.router, prefix="/api/v1/estadisticas")
app.include_router(archivos.router, prefix="/api/v1/archivos")
app.include_router(documentos.router, prefix="/api/v1/documentos")
app.include_router(archivos_contratos.router, prefix="/api/v1/archivos-contratos")
app.include_router(historial.router, prefix="/api/v1/historial")
app.include_router(analisis.router, prefix="/api/v1/analisis")

@app.get("/")
def root():
    return {"status": "ok"}
