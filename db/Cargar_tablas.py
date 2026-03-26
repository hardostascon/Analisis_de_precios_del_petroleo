import sys

sys.path.append("..")

import create_tables as creatablas
from carga import carga_registro as carga
from db.base import engine

Cargadatos = carga.CargarData()
creatabla = creatablas.CrearTablas()
datos = Cargadatos.CargarDato("../CSV/fuel_prices_1970_2026.csv")
# DataFrames #
promediosanno = Cargadatos.FuncionesDataFrame(datos, "1")
Promediomes=(Cargadatos.FuncionesDataFrame(datos, "2"))
diferencia_anno=(Cargadatos.FuncionesDataFrame(datos, "3"))
variacion_diferencia=(Cargadatos.FuncionesDataFrame(datos, "4"))
media=(Cargadatos.FuncionesDataFrame(datos, "5"))
resumen_estadistico=(Cargadatos.FuncionesDataFrame(datos, "6"))

#Carga Tablas
#creatabla.guardar_en_bd(engine, promediosanno, "promedios_anno")
#creatabla.guardar_en_bd(engine, Promediomes, "promedios_mes")
#creatabla.guardar_en_bd(engine, diferencia_anno, "diferencia_anno")
#creatabla.guardar_en_bd(engine, variacion_diferencia, "variaciones")
#creatabla.guardar_en_bd(engine, media, "media")
#creatabla.guardar_en_bd(engine, resumen_estadistico, "resumen_estadistico")
#creatabla.guardar_en_bd(engine, resumen_estadistico, "resumen_estadistico")