# Se importan los modulos necesarios para la ejecucion de la interfaz grafica
from PySide6.QtGui import QIcon
from PySide6 import QtWidgets, QtCore
from interfaces.main_window import Ui_MainWindow
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QMainWindow, QHeaderView, QMessageBox


# Se importa la clase que posee todos los metodos para manejar la base de datos
from datos.queries_Bd import QueriesBd

# Se importan las clases de las naves
from clases.lanzadera import Lanzadera
from clases.no_tripulada import NoTripulada
from clases.tripulada import Tripulada


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Se oculta el boton de reducir
        self.btn_reducir.hide()

        # Se elimina la barra de titulo
        self.setWindowFlag(
            QtCore.Qt.FramelessWindowHint
        )  # Eliminar barra de titulo de la ventana
        self.setWindowOpacity(0.95)  # Opacidad de la ventana

        # Se ajustan los tamaños de las tablas
        self.tbl_consulta_sencilla.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )  # Se ajusta el tamaño de la tabla
        self.tbl_consulta_avanzada.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )  # Se ajusta el tamaño de la tabla
        self.stackedWidget.setCurrentWidget(self.pg_consultas)

        # se hace un reescalamiento de la ventana
        self.gripSize = 30
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # Se habilita el movimiento de la ventana
        self.frame_encabezado.mouseMoveEvent = self.mover_ventana

        # =============== Conexión de todos los botones del programa =============== #

        # Botones del panel de control
        self.consultar_nave.clicked.connect(
            self.ventana_consultas
        )  # Conectar el boton con la ventana de consultas
        self.crear_lanzadera.clicked.connect(
            self.ventana_lanzadera
        )  # Conectar el boton con la ventana de lanzadera
        self.crear_no_tripulada.clicked.connect(
            self.ventana_no_tripulada
        )  # Conectar el boton con la ventana de no tripuladas
        self.crear_tripulada.clicked.connect(
            self.ventana_tripulada
        )  # Conectar el boton con la ventana de tripuladas

        # Botones del panel superior
        self.btn_menu.clicked.connect(self.mostrar_menu)
        self.btn_cerrar.clicked.connect(self.cerrar_programa)
        self.btn_ampliar.clicked.connect(self.ampliar_ventana)
        self.btn_reducir.clicked.connect(self.reducir_ventana)
        self.btn_minimizar.clicked.connect(self.minimizar_ventana)

        # Boton crear lanzadera
        self.btn_registrar_lanzadera.clicked.connect(self.registrar_nave)

        # Boton crear tripulada
        self.btn_registrar_tripulada.clicked.connect(self.registrar_nave)

        # Boton crear no tripulada
        self.btn_registrar_no_tripulada.clicked.connect(self.registrar_nave)

        # Botones de la venta de consultas
        self.btn_consulta_sencilla.clicked.connect(self.consulta_general_naves)

        # =============== Agrupación de todos los QLineEdit por ventana =============== #

        self.cuadros_texto_ventana_crear_lanzadera = [
            self.ql_pais_lanzadera,
            self.ql_peso_lanzadera,
            self.ql_anio_lanzadera,
            self.ql_nombre_lanzadera,
            self.ql_velocidad_lanzadera,
            self.ql_altura_lanzadera,
            self.ql_potencia_lanzadera,
            self.ql_carga_util_lanzadera,
            self.ql_autonomia_lanzadera,
            self.ql_combustible_lanzadera,
        ]  # Lista de los cuadros de texto de la ventana de crear lanzadera

        self.cuadros_texto_ventana_crear_tripulada = [
            self.ql_pais_tripulada,
            self.ql_peso_tripulada,
            self.ql_anio_tripulada,
            self.ql_nombre_tripulada,
            self.ql_velocidad_tripulada,
            self.ql_orbita_tripulada,
            self.ql_tipo_mision_tripulada,
            self.ql_capacidad_tripulada,
            self.ql_nombre_mision_tripulada,
        ]  # Lista de los cuadros de texto de la ventana de crear no tripulada

        self.cuadros_texto_ventana_crear_no_tripulada = [
            self.ql_pais_no_tripulada,
            self.ql_peso_no_tripulada,
            self.ql_anio_no_tripulada,
            self.ql_nombre_no_tripulada,
            self.ql_velocidad_no_tripulada,
            self.ql_empuje_no_tripulada,
            self.ql_combustible_no_tripulada,
            self.ql_planeta_exploracion_no_tripulada,
            self.ql_cantidad_motores_no_tripulada,
        ]  # Lista de los cuadros de texto de la ventana de  crear tripulada

    # =============== Metodos del panel de control =============== #
    def ventana_consultas(self):  # Ventana de consultas
        self.tbl_consulta_sencilla.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )  # Se ajusta el tamaño de la tabla
        self.tbl_consulta_avanzada.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )  # Se ajusta el tamaño de la tabla
        self.stackedWidget.setCurrentWidget(self.pg_consultas)

    def ventana_lanzadera(self):  # Ventana de lanzadera
        self.stackedWidget.setCurrentWidget(self.pg_crear_lanzadera)

    def ventana_tripulada(self):  # Ventana de tripulada
        self.stackedWidget.setCurrentWidget(self.pg_crear_tripulada)

    def ventana_no_tripulada(self):  # Ventana de no tripuladas
        self.stackedWidget.setCurrentWidget(self.pg_crear_no_tripulada)

    # =============== Metodos del panel superior =============== #
    def cerrar_programa(self):  # Cerrar el programa
        self.close()

    def mostrar_menu(self):  # Mostrar el menu
        if True:
            ancho = self.frame_control.width()
            por_defecto = 0
            if ancho == 0:
                desplegar = 200
            else:
                desplegar = por_defecto
            self.animacion = QPropertyAnimation(self.frame_control, b"minimumWidth")
            self.animacion.setDuration(300)
            self.animacion.setStartValue(ancho)
            self.animacion.setEndValue(desplegar)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()

    def ampliar_ventana(self):  # Ampliar la ventana
        self.btn_ampliar.hide()
        self.btn_reducir.show()
        self.showMaximized()

    def reducir_ventana(self):  # Reducir la ventana
        self.btn_ampliar.show()
        self.btn_reducir.hide()
        self.showNormal()

    def minimizar_ventana(self):  # Minimizar la ventana
        self.showMinimized()

    def mousePressEvent(self, evento):  # Metodo para saber donde se presiono el mouse
        self.posicion_click = evento.globalPos()

    # =============== Metodo de movimiento de la ventana =============== #
    def mover_ventana(self, evento):
        if self.isMaximized() == False:
            if evento.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + (evento.globalPos() - self.posicion_click))
                self.posicion_click = evento.globalPos()
                evento.accept()
        if evento.globalPos().y() <= 30:
            self.showMaximized()
            self.btn_ampliar.hide()
            self.btn_reducir.show()
        else:
            self.showNormal()
            self.btn_ampliar.show()
            self.btn_reducir.hide()

    # =============== Metodos para manipular los datos =============== #
    def registrar_nave(self):
        if self.stackedWidget.currentWidget() == self.pg_crear_lanzadera:
            Nave = Lanzadera(
                self.ql_pais_lanzadera.text(),
                self.ql_peso_lanzadera.text(),
                self.ql_anio_lanzadera.text(),
                self.ql_nombre_lanzadera.text(),
                self.ql_velocidad_lanzadera.text(),
                self.ql_altura_lanzadera.text(),
                self.ql_potencia_lanzadera.text(),
                self.ql_carga_util_lanzadera.text(),
                self.ql_autonomia_lanzadera.text(),
                self.ql_combustible_lanzadera.text(),
            )

            validacion_campos_nulos = [
                QLineEdit.text()
                for QLineEdit in self.cuadros_texto_ventana_crear_lanzadera
                if QLineEdit.text() == ""
            ]  # Se obtiene el valor de los cuadros de texto

            if validacion_campos_nulos:  # Si hay campos nulos
                dialogo = QMessageBox.critical(
                    self, "Error", "Debes de llenar todos los campos"
                )
            else:  # Si no hay campos nulos
                QueriesBd.registrar_nave(
                    self, Nave
                )  # Se registra la nave en la base de datos

                for (
                    QLineEdit
                ) in (
                    self.cuadros_texto_ventana_crear_lanzadera
                ):  # Se limpian los cuadros de texto
                    QLineEdit.clear()

                dialogo = QMessageBox.information(
                    self, "Operación éxitosa", "Tú nave fue creada correctamente"
                )

        elif self.stackedWidget.currentWidget() == self.pg_crear_tripulada:
            Nave = Tripulada(
                self.ql_pais_tripulada.text(),
                self.ql_peso_tripulada.text(),
                self.ql_anio_tripulada.text(),
                self.ql_nombre_tripulada.text(),
                self.ql_velocidad_tripulada.text(),
                self.ql_orbita_tripulada.text(),
                self.ql_tipo_mision_tripulada.text(),
                self.ql_capacidad_tripulada.text(),
                self.ql_nombre_mision_tripulada.text(),
            )

            validacion_campos_nulos = [
                QLineEdit.text()
                for QLineEdit in self.cuadros_texto_ventana_crear_tripulada
                if QLineEdit.text() == ""
            ]  # Se obtiene el valor de los cuadros de texto

            if validacion_campos_nulos:  # Si hay campos nulos
                dialogo = QMessageBox.critical(
                    self, "Error", "Debes de llenar todos los campos"
                )
            else:  # Si no hay campos nulos
                QueriesBd.registrar_nave(
                    self, Nave
                )  # Se registra la nave en la base de datos

                for (
                    QLineEdit
                ) in (
                    self.cuadros_texto_ventana_crear_tripulada
                ):  # Se limpian los cuadros de texto
                    QLineEdit.clear()

                dialogo = QMessageBox.information(
                    self, "Operación éxitosa", "Tú nave fue creada correctamente"
                )

        elif self.stackedWidget.currentWidget() == self.pg_crear_no_tripulada:
            Nave = NoTripulada(
                self.ql_pais_no_tripulada.text(),
                self.ql_peso_no_tripulada.text(),
                self.ql_anio_no_tripulada.text(),
                self.ql_nombre_no_tripulada.text(),
                self.ql_velocidad_no_tripulada.text(),
                self.ql_empuje_no_tripulada.text(),
                self.ql_combustible_no_tripulada.text(),
                self.ql_planeta_exploracion_no_tripulada.text(),
                self.ql_cantidad_motores_no_tripulada.text(),
            )

            validacion_campos_nulos = [
                QLineEdit.text()
                for QLineEdit in self.cuadros_texto_ventana_crear_no_tripulada
                if QLineEdit.text() == ""
            ]  # Se obtiene el valor de los cuadros de texto

            if validacion_campos_nulos:  # Si hay campos nulos
                dialogo = QMessageBox.critical(
                    self, "Error", "Debes de llenar todos los campos"
                )
            else:  # Si no hay campos nulos
                QueriesBd.registrar_nave(
                    self, Nave
                )  # Se registra la nave en la base de datos

                for (
                    QLineEdit
                ) in (
                    self.cuadros_texto_ventana_crear_no_tripulada
                ):  # Se limpian los cuadros de texto
                    QLineEdit.clear()

                dialogo = QMessageBox.information(
                    self, "Operación éxitosa", "Tú nave fue creada correctamente"
                )

    def consulta_general_naves(self):
        datos = QueriesBd.consulta_general_naves(self)
        filas = len(datos)
        self.tbl_consulta_sencilla.setRowCount(filas)
        fila_tabla = 0
        for fila in datos:
            self.Id = fila[0]
            self.tbl_consulta_sencilla.setItem(
                fila_tabla, 0, QtWidgets.QTableWidgetItem(fila[1])
            )
            self.tbl_consulta_sencilla.setItem(
                fila_tabla, 1, QtWidgets.QTableWidgetItem(fila[2])
            )
            self.tbl_consulta_sencilla.setItem(
                fila_tabla, 2, QtWidgets.QTableWidgetItem(fila[3])
            )
            self.tbl_consulta_sencilla.setItem(
                fila_tabla, 3, QtWidgets.QTableWidgetItem(fila[4])
            )
            self.tbl_consulta_sencilla.setItem(
                fila_tabla, 4, QtWidgets.QTableWidgetItem(fila[5])
            )
            self.tbl_consulta_sencilla.setItem(
                fila_tabla, 5, QtWidgets.QTableWidgetItem(fila[5])
            )
