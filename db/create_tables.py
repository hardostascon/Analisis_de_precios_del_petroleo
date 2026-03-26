import pandas as pd


class CrearTablas:
    def __init__(self):
        pass

    def guardar_en_bd(self, engine, dataframe, nombre):
        df = dataframe.copy()
        for col in df.columns:
            if df[col].dtype.name == "period[M]":
                df[col] = df[col].astype(str)
        df.to_sql(nombre, con=engine, if_exists="replace", index=True)
        print(f"Tabla '{nombre}' guardada exitosamente")
