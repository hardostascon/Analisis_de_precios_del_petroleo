import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from service import estadistico_service


app = FastAPI(
    title="Estadistico de Precios del petroleo 1970-2026",
    description="API consulta de estadisticos",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

est = estadistico_service.Estadisticos()


@app.get("/diferencia_anno")
def obtener_diferencia_anual():
    return est.obtener_diferenciaanno()

@app.get("/media")
def obtener_media():
    return est.obtener_media()

@app.get("/promedio_anno")
def obtener_promedio_anno():
    return est.promedio_anno()

@app.get("/promedio_mes")
def obtener_promedio_mes():
    return est.promedio_mes()

@app.get("/resumen_estadistico")
def obtener_resumen_est():
    return est.resumen_estadistico()

@app.get("/variaciones")
def variacion():
    return est.variaciones()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("api.api_estadistico:app", host="127.0.0.1", port=8000, reload=True)
