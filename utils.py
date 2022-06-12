from statics import mean, max, min
import pandas as pd


def message(max_value, min_value, mean_value, rows_load, source):
    """
    Genera los mensajes en consola a partir de los datos enviados
    """
    print(f"Filas cargadas de {source}: ", rows_load)
    print(f"Valor promedio {source}: ", mean_value)
    print(f"Valor minimo {source}: ", min_value)
    print(f"Valor maximo {source}: ", max_value)
    print("--------------------------")


def ETL(files, max_value, min_value, mean_value, rows_load, table, source):
    """
    Realiza el ETL de los datos y devuelve las variables resultantes
    """
    max_value = max_value
    min_value = min_value
    mean_value = mean_value
    rows_load = rows_load
    for file in files:
        df = pd.read_csv("data/{}.csv".format(file))
        # transformacion de datos
        df["price"].fillna(0, inplace=True)
        max_value = max(max_value, df["price"].max())
        min_value = min(min_value, df["price"].min())
        mean_value = mean(mean_value, df["price"].mean())
        for i in df.index:
            table.agregar(
                df["user_id"][i], df["price"][i], df["timestamp"][i])
            rows_load += 1
        message(max_value, min_value, mean_value, rows_load, source)

    return max_value, min_value, mean_value, rows_load
