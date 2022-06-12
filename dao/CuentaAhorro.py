import sqlite3


class CuentaAhorro:

    def __init__(self, db_name) -> None:
        self.conexion = sqlite3.connect(db_name)
        self.conexion.text_factory = str

    def agregar(self, user_id, price, timestamp):
        """
        Agrega un registro en la tabla cuenta_ahorro
        """
        c = self.conexion.cursor()
        c.execute("""
            INSERT INTO cuenta_ahorro (user_id, price, time_stamp) 
            VALUES({},{},{})""".format(user_id, price, timestamp))
        c.close()

    def consultar(self):
        """
        Consulta todos los registros de la tabla cuenta_ahorro
        """
        c = self.conexion.cursor()
        c.execute("SELECT * FROM cuenta_ahorro")
        rows = c.fetchall()

        c.close()
        return rows

    def min(self):
        """
        Devuelve el minimo de los registros de la columna price de la tabla cuenta_ahorro
        """
        c = self.conexion.cursor()
        c.execute("SELECT min(price) FROM cuenta_ahorro")
        rows = c.fetchone()
        c.close()
        return rows[0]

    def max(self):
        """
        Devuelve el maximo de los registros de la columna price de la tabla cuenta_ahorro
        """
        c = self.conexion.cursor()
        c.execute("SELECT max(price) FROM cuenta_ahorro")
        rows = c.fetchone()
        c.close()
        return rows[0]

    def media(self):
        """
        Devuelve la media de los registros de la columna price de la tabla cuenta_ahorro
        """
        c = self.conexion.cursor()
        c.execute(
            "SELECT AVG(price) FROM cuenta_ahorro")
        rows = c.fetchone()
        c.close()
        return rows[0]

    def total_rows(self):
        """
        Devuelve la cantidad de registros que en la tabla cuenta_ahorro
        """
        c = self.conexion.cursor()
        c.execute("SELECT COUNT(*) FROM cuenta_ahorro")
        row = c.fetchone()
        c.close()
        return row[0]
