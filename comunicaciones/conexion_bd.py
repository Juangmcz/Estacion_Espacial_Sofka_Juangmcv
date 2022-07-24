""" Este modulo se encarga de establecer la conexión con la base de datos """

import pyodbc


class BdManager:
    def __enter__(self):
        try:
            self.conexion = pyodbc.connect(
                "DRIVER={SQL Server};SERVER=MR-PC;UID=sa;PWD=3220"
            )
            self.cursor = self.conexion.cursor()
        except Exception as e:
            print("Error de conexión con la base de datos: ", e)

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.cursor.close()
        self.conexion.close()
