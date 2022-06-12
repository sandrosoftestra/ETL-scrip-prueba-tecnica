from dao.CuentaAhorro import CuentaAhorro
from database import create_db_tables, delete_db
from utils import ETL, message

DB_NAME = "basededatos.db"


def main():
    # Eliminacion de base de datos
    delete_db(DB_NAME)

    # Creacion de Base de datos
    create_db_tables(DB_NAME)

    print("--------------------------")

    # Creacion de variables
    cuenta_ahorro = CuentaAhorro(DB_NAME)
    max_value = True
    min_value = True
    mean_value = True
    rows_load = 0

    # Cargar archivos
    files1 = ["2012-1", "2012-2", "2012-3", "2012-4", "2012-5"]
    max_value, min_value, mean_value, rows_load = ETL(
        files1, max_value, min_value, mean_value, rows_load, cuenta_ahorro, "archivos")

    # Datos de db
    message(cuenta_ahorro.max(), cuenta_ahorro.min(),
            cuenta_ahorro.media(), cuenta_ahorro.total_rows(), "base de datos")

    # Cargar validation
    files2 = ["validation"]
    max_value, min_value, mean_value, rows_load = ETL(
        files2, max_value, min_value, mean_value, rows_load, cuenta_ahorro, "validation")

    # Datos de db luego de cargar validation
    message(cuenta_ahorro.max(), cuenta_ahorro.min(),
            cuenta_ahorro.media(), cuenta_ahorro.total_rows(), "base de datos")


if __name__ == '__main__':
    main()
