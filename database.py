import os
import sqlite3


def delete_db(db_name):
    """
    Elimina la base de datos si existe
    """
    try:
        os.remove(db_name)
    except:
        print("Base de datos no existe")


def create_db_tables(db_name):
    """
    Crea nuevamente la base de datos y la tabla o las crea por primera vez
    """
    try:
        conexion = sqlite3.connect(db_name)
        conexion.text_factory = str
        c = conexion.cursor()

        c.execute(
            """CREATE TABLE cuenta_ahorro(
                id Integer PRIMARY KEY AUTOINCREMENT, 
                user_id INT NOT NULL, 
                price INT NOT NULL,
                time_stamp DATE NOT NULL
            )""")

        conexion.commit()
        conexion.close()
        print("Base de datos y tabla fueron creadas")
    except sqlite3.OperationalError:
        print("Base de datos y tabla ya han sido creadas")
    except Exception as e:
        print("Error desconocido" + str(e))
