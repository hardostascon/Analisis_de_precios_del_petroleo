import pandas as pd


class CargarData:
    def __init__(self):
        pass

    def CargarDato(self, archivo):
        DataSetPetroleo = pd.read_csv(archivo)
        return DataSetPetroleo

    def FuncionesDataFrame(self, DataSetPetroleo, tipo):
        df = DataSetPetroleo.copy()
        try:
            fecha = pd.to_datetime(df["Date"])
            year = fecha.dt.year
            month = fecha.dt.to_period("M")

            if tipo == "1":
                df["Year"] = year
                df_reordenado = df.drop(columns=["Date"]).reindex(
                    columns=["Year", "Crude_Oil_Price"]
                )
                df_dataset = (
                    df_reordenado.groupby("Year")["Crude_Oil_Price"]
                    .mean()
                    .round(2)
                    .reset_index(name="Promedio_Precio")
                )
            elif tipo == "2":
                df["Yearmonth"] = month
                df_dataset = (
                    df.groupby("Yearmonth")["Crude_Oil_Price"]
                    .mean()
                    .round(2)
                    .reset_index(name="Promedio_Precio")
                )
            elif tipo == "3":
                df["Year"] = year
                df_reordenado = df.drop(columns=["Date"]).reindex(
                    columns=["Year", "Crude_Oil_Price"]
                )
                df_dataset = (
                    df_reordenado.groupby("Year")["Crude_Oil_Price"]
                    .agg(
                        Maximo_Anno="max",
                        Minimo_Anno="min",
                        Diferencia=lambda x: x.max() - x.min(),
                    )
                    .round(2)
                )
            elif tipo == "4":
                df["Yearmonth"] = month
                df["Variacion_%"] = df["Crude_Oil_Price"].pct_change().fillna(0) * 100
                df["Diferencia"] = df["Crude_Oil_Price"].diff().fillna(0).round(2)
                df_dataset = df
            elif tipo == "5":
                df["Media_Movil_12"] = (
                    df["Crude_Oil_Price"].rolling(window=12).mean().fillna(0).round(2)
                )
                df["Media_Movil_3"] = (
                    df["Crude_Oil_Price"].rolling(window=3).mean().fillna(0).round(2)
                )
                df_dataset = df
            elif tipo == "6":
                df["Decade"] = (year // 10) * 10
                df_dataset = df.groupby("Decade")["Crude_Oil_Price"].describe().round(2)
            elif tipo == "7":
                fila_max = df.loc[df["Crude_Oil_Price"].idxmax()]
                fila_min = df.loc[df["Crude_Oil_Price"].idxmin()]
                return f"Maximo: {round(fila_max['Crude_Oil_Price'], 2)} en {fila_max['Date']} \nMinimo: {round(fila_min['Crude_Oil_Price'], 2)} en {fila_min['Date']}"
            else:
                return None
            return df_dataset
        except Exception as e:
            print(f"Error: {e}")
            return None
            return df_dataset
        except Exception as e:
            print(f"Error: {e}")
            return None


#Cargadatos = CargarData()
#datos = Cargadatos.CargarDato("../CSV/fuel_prices_1970_2026.csv")
#print(Cargadatos.FuncionesDataFrame(datos, "1"))
#print(Cargadatos.FuncionesDataFrame(datos, "2"))
#print(Cargadatos.FuncionesDataFrame(datos, "3"))
#print(Cargadatos.FuncionesDataFrame(datos, "4"))
#print(Cargadatos.FuncionesDataFrame(datos, "5"))
#print(Cargadatos.FuncionesDataFrame(datos, "6"))
#print(Cargadatos.FuncionesDataFrame(datos, "7"))
