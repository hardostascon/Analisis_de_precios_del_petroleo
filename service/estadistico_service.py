import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import text
from db.base import engine


class Estadisticos:
    def __init__(self):
        pass

    def obtener_diferenciaanno(self):
        with engine.connect() as conn:
            result = conn.execute(text('SELECT "Year"::text as anno, * FROM public.diferencia_anno'))
            columns = result.keys()
            return [dict(zip(columns, row)) for row in result.fetchall()]

    def obtener_media(self):
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM public.media"))
            columns = result.keys()
            return [dict(zip(columns, row)) for row in result.fetchall()]
    
    def promedio_anno(self):
        with engine.connect() as conn:
            result = conn.execute(text('SELECT "Year"::text as year,"Promedio_Precio" as Promedio_Precio FROM public.promedios_anno'))
            columns = result.keys()
            return [dict(zip(columns, row)) for row in result.fetchall()]  
        
    def promedio_mes(self):
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM public.promedios_mes"))
            columns = result.keys()
            return [dict(zip(columns, row)) for row in result.fetchall()]  
    
    def resumen_estadistico(self):
        with engine.connect() as conn:
            result = conn.execute(text('SELECT "Decade"::text as decada ,* FROM public.resumen_estadistico'))
            columns = result.keys()
            return [dict(zip(columns, row)) for row in result.fetchall()] 
        
    def variaciones(self):
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM public.variaciones"))
            columns = result.keys()
            return [dict(zip(columns, row)) for row in result.fetchall()]     
# if __name__ == "__main__":
#   est = Estadisticos()
#  print(est.obtener_diferenciaanno())
