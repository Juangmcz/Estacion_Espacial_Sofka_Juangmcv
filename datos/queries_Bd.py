""" Este modulo define la clase QueriesBd, la cual va a contener los metodos que ejecutan las consultas a la base de datos """

# Se importan las clases necesarias para la ejecución de las consultas
from clases.tripulada import Tripulada
from clases.lanzadera import Lanzadera
from clases.no_tripulada import NoTripulada

# Se importa la clase encargada de gestionar la conexion con la base de datos
from comunicaciones.conexion_bd import BdManager


class QueriesBd:
    def registrar_nave(self, Nave):

        if isinstance(Nave, Lanzadera):
            nombre = Nave.obtener_nombre()
            pais = Nave.obtener_pais()
            peso = Nave.obtener_peso()
            velocidad = Nave.obtener_velocidad()
            altura = Nave.obtener_altura()
            potencia = Nave.obtener_potencia()
            carga_util = Nave.obtener_carga_util()
            autonomia = Nave.obtener_autonomia()
            combustible = Nave.obtener_combustible()
            anio = Nave.obtener_anio()

            with BdManager() as conexion_sql:
                QUERY = f"""
                        /*
                        Arg: Nave
                        Return: 
                            None
                        */
                        INSERT INTO Estacion_Espacial_Sofka.dbo.Naves_Lanzaderas
                            (Nombre, 
                            Pais, 
                            Peso, 
                            Velocidad, 
                            Altura, 
                            Potencia, 
                            Carga_Util, 
                            Autonomia, 
                            Combustible, 
                            Anio)
                        VALUES
                            ('{nombre}', 
                            '{pais}', 
                            {peso}, 
                            {velocidad}, 
                            {altura}, 
                            {potencia}, 
                            {carga_util}, 
                            {autonomia}, 
                            '{combustible}', 
                            {anio}); 
                        
                        """
                conexion_sql.cursor.execute(QUERY)
                conexion_sql.cursor.commit()

        elif isinstance(Nave, Tripulada):
            nombre = Nave.obtener_nombre()
            pais = Nave.obtener_pais()
            peso = Nave.obtener_peso()
            velocidad = Nave.obtener_velocidad()
            orbita = Nave.obtener_orbita()
            tipo_mision = Nave.obtener_tipo_mision()
            capacidad = Nave.obtener_capacidad()
            nombre_mision = Nave.obtener_nombre_mision()
            anio = Nave.obtener_anio()

            with BdManager() as conexion_sql:
                QUERY = f"""
                        /*
                        Arg: Nave
                        Return: 
                            None
                        */
                        INSERT INTO Estacion_Espacial_Sofka.dbo.Naves_Tripuladas
                            (Nombre, 
                            Pais, 
                            Peso, 
                            Velocidad,
                            Orbita, 
                            Tipo_Mision, 
                            Capacidad, 
                            Nombre_Mision,
                            Anio)
                        VALUES
                            ('{nombre}',
                            '{pais}',
                            {peso},
                            {velocidad},
                            '{orbita}', 
                            '{tipo_mision}', 
                            {capacidad}, 
                            '{nombre_mision}', 
                            {anio});
                        
                        """
                conexion_sql.cursor.execute(QUERY)
                conexion_sql.cursor.commit()

        elif isinstance(Nave, NoTripulada):
            nombre = Nave.obtener_nombre()
            pais = Nave.obtener_pais()
            peso = Nave.obtener_peso()
            velocidad = Nave.obtener_velocidad()
            empuje = Nave.obtener_empuje()
            combustible = Nave.obtener_combustible()
            planeta_exploracion = Nave.obtener_planeta_exploracion()
            cantidad_motores = Nave.obtener_cantidad_motores()
            anio = Nave.obtener_anio()

            with BdManager() as conexion_sql:
                QUERY = f"""
                        /*
                        Arg: Nave
                        Return: 
                            None
                        */
                        INSERT INTO Estacion_Espacial_Sofka.dbo.Naves_No_Tripuladas
                            (Nombre, 
                            Pais, 
                            Peso, 
                            Velocidad, 
                            Empuje, 
                            Combustible, 
                            Planeta_Exploracion, 
                            Cantidad_Motores, 
                            Anio)
                        VALUES
                            ('{nombre}',
                            '{pais}',
                            {peso},
                            {velocidad},
                            {empuje},
                            '{combustible}',
                            '{planeta_exploracion}',
                            {cantidad_motores},
                            {anio});
                        
                        """
                conexion_sql.cursor.execute(QUERY)
                conexion_sql.cursor.commit()

    def consulta_general_naves(self):
        with BdManager() as conexion_sql:
            QUERY = f"""
                    /*
                    Arg: None
                    Return: 
                        Todas las naves almacenadas en la tabla
                    */
                    SELECT  Id, 
                            Nombre,
                            Anio,
                            Pais, 
                            Peso, 
                            Velocidad
                    FROM Estacion_Espacial_Sofka.dbo.Naves_Tripuladas;
                    
                    """
            conexion_sql.cursor.execute(QUERY)
            consulta = conexion_sql.cursor.fetchall()
        return consulta

    def consulta_avanzada_naves(self, tipo_de_nave, año, pais):
        if tipo_de_nave == "No Tripulada":
            with BdManager() as conexion_sql:
                QUERY = f"""
                        /*
                        Arg: None
                        Return: 
                            Todas las naves almacenadas en la tabla "Naves"
                        */
                        SELECT * FROM [Estacion_Espacial_Sofka].[dbo].[Naves_No_Tripuladas];
                            WHERE Año = {año} AND Pais = '{pais}';
                        
                        """
                conexion_sql.cursor.execute(QUERY)
                consulta = conexion_sql.cursor.fetchall()
            return consulta

        elif tipo_de_nave == "Tripulada":
            with BdManager() as conexion_sql:
                QUERY = f"""
                            /*
                            Arg: None
                            Return: 
                                Todas las naves almacenadas en la tabla "Naves"
                            */
                            SELECT * FROM [Estacion_Espacial_Sofka].[dbo].[Naves_Tripuladas]
                                WHERE Año = {año} AND Pais = '{pais}';
                            
                            """
                conexion_sql.cursor.execute(QUERY)
                consulta = conexion_sql.cursor.fetchall()
            return consulta

        elif tipo_de_nave == "Lanzadera":
            with BdManager() as conexion_sql:
                QUERY = f"""
                            /*
                            Arg: None
                            Return: 
                                Todas las naves almacenadas en la tabla "Naves"
                            */
                            SELECT * FROM [Estacion_Espacial_Sofka].[dbo].[Naves_Lanzaderas]
                                WHERE Año = {año} AND Pais = '{pais}';
                            
                            """
                conexion_sql.cursor.execute(QUERY)
                consulta = conexion_sql.cursor.fetchall()
            return consulta
