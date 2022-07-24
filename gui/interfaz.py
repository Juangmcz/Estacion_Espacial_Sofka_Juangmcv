# Se importan los modulos necesarios para la ejecucion de la interfaz grafica
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
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # Opacidad de la ventana
        self.setWindowOpacity(0.95)

        # Se ajustan los tamaños de las tablas
        self.tbl_consulta_sencilla.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.tbl_consulta_avanzada.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.stackedWidget.setCurrentWidget(self.pg_consultas)

        # se hace un reescalamiento de la ventana
        self.gripSize = 30
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # Se habilita el movimiento de la ventana
        self.frame_encabezado.mouseMoveEvent = self.mover_ventana

        # =============== Conexión de todos los botones del programa =============== #

        # Botones del panel de control
        self.ayuda.clicked.connect(self.ventana_ayuda)
        self.consultar_nave.clicked.connect(self.ventana_consultas)
        self.crear_tripulada.clicked.connect(self.ventana_tripulada)
        self.crear_lanzadera.clicked.connect(self.ventana_lanzadera)
        self.explora_tu_nave.clicked.connect(self.ventana_explorar_nave)
        self.crear_no_tripulada.clicked.connect(self.ventana_no_tripulada)

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
        self.btn_consulta_avanzada.clicked.connect(self.consulta_avanzada_naves)

        # Boton de la ventana de explorar naves
        self.btn_explorar_funcion.clicked.connect(self.explorar_funcion_nave)

        self.cBox_tipo_nave_conoce_tu_nave.currentIndexChanged.connect(
            self.actualizar_lista_funciones
        )

        # =============== Agrupación de todos los QLineEdit por ventana =============== #

        # Lista de los cuadros de texto de la ventana de crear lanzadera
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
        ]

        # Lista de los cuadros de texto de la ventana de crear no tripulada
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
        ]

        # Lista de los cuadros de texto de la ventana de crear tripulada
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
        ]

        # Lista de los cuadros de texto de consultas avanzadas
        self.cuadros_texto_consultas_avanzadas = [
            self.ql_pais_nave,
            self.ql_anio_nave,
        ]

        # =============== Metodos disponibles por tipo de nave  =============== #

        # Lista de metodos disponibles nave tripulada
        self.metodos_nave_tripulada = [
            "despegar",
            "cuenta_regresiva",
            "chequeo_general",
            "aterrizar",
            "repostar",
            "acoplamiento",
        ]

        # Lista de metodos disponibles nave no tripulada
        self.metodos_nave_no_tripulada = [
            "despegar",
            "cuenta_regresiva",
            "chequeo_general",
            "explorar",
            "amartizar",
            "corregir_trayectoria",
        ]

        # Lista de metodos disponibles nave no tripulada
        self.metodos_nave_lanzadera = [
            "despegar",
            "cuenta_regresiva",
            "chequeo_general",
            "aterrizar",
            "separacion",
            "abrir_paracaidas",
        ]

    # =============== Metodos del panel de control =============== #
    def ventana_consultas(self):  # Ventana de consultas
        # Se ajusta el tamaño de la tabla
        self.tbl_consulta_sencilla.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        # Se ajusta el tamaño de la tabla
        self.tbl_consulta_avanzada.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.stackedWidget.setCurrentWidget(self.pg_consultas)

    def ventana_lanzadera(self):  # Ventana de lanzadera
        self.stackedWidget.setCurrentWidget(self.pg_crear_lanzadera)

    def ventana_tripulada(self):  # Ventana de tripulada
        self.stackedWidget.setCurrentWidget(self.pg_crear_tripulada)

    def ventana_no_tripulada(self):  # Ventana de no tripuladas
        self.stackedWidget.setCurrentWidget(self.pg_crear_no_tripulada)

    def ventana_ayuda(self):  # Ventana de ayuda
        self.stackedWidget.setCurrentWidget(self.pg_ayuda)

    def ventana_explorar_nave(self):  # Ventana de explorar nave
        self.ql_nombre_conoce_tu_nave.clear()  # Se limpia el cuadro de texto
        self.lbl_resultado_conoce_tu_nave.clear()  # Se limpia el cuadro de texto
        self.actualizar_lista_funciones()  # Se actualiza la lista de funciones
        self.stackedWidget.setCurrentWidget(self.pg_explora_tu_nave)

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
    def actualizar_lista_funciones(self):
        # Se limpia el cuadro de texto
        self.cBox_funcion_conoce_tu_nave.clear()
        # Se obtiene el tipo de nave
        tipo_nave = self.cBox_tipo_nave_conoce_tu_nave.currentText()
        if tipo_nave == "Tripulada":
            self.cBox_funcion_conoce_tu_nave.addItems(self.metodos_nave_tripulada)
        elif tipo_nave == "No Tripulada":
            self.cBox_funcion_conoce_tu_nave.addItems(self.metodos_nave_no_tripulada)
        elif tipo_nave == "Lanzadera":
            self.cBox_funcion_conoce_tu_nave.addItems(self.metodos_nave_lanzadera)

    def explorar_funcion_nave(self):  # Metodo para expolar la funcion de la nave

        nombre_nave = self.ql_nombre_conoce_tu_nave.text()
        tipo_nave = self.cBox_tipo_nave_conoce_tu_nave.currentText()
        metodo_nave = self.cBox_funcion_conoce_tu_nave.currentText()

        if nombre_nave == "":
            dialogo = QMessageBox.critical(
                self, "Error", "Debes ingresar un nombre para tu nave"
            )
        else:
            if tipo_nave == "Tripulada":
                nave = Tripulada(nombre=nombre_nave)
                if metodo_nave == "despegar":
                    resultado = nave.despegar()
                elif metodo_nave == "cuenta_regresiva":
                    resultado = nave.cuenta_regresiva()
                elif metodo_nave == "chequeo_general":
                    resultado = nave.chequeo_general()
                elif metodo_nave == "aterrizar":
                    resultado = nave.aterrizar()
                elif metodo_nave == "repostar":
                    resultado = nave.repostar()
                elif metodo_nave == "acoplamiento":
                    resultado = nave.acoplamiento()
                self.lbl_resultado_conoce_tu_nave.setText(str(resultado))

            elif tipo_nave == "No Tripulada":
                nave = NoTripulada(nombre=nombre_nave)
                if metodo_nave == "despegar":
                    resultado = nave.despegar()
                elif metodo_nave == "cuenta_regresiva":
                    resultado = nave.cuenta_regresiva()
                elif metodo_nave == "chequeo_general":
                    resultado = nave.chequeo_general()
                elif metodo_nave == "explorar":
                    resultado = nave.explorar()
                elif metodo_nave == "amartizar":
                    resultado = nave.amartizar()
                elif metodo_nave == "corregir_trayectoria":
                    resultado = nave.corregir_trayectoria()
                self.lbl_resultado_conoce_tu_nave.setText(str(resultado))

            elif tipo_nave == "Lanzadera":
                nave = Lanzadera(nombre=nombre_nave)
                if metodo_nave == "despegar":
                    resultado = nave.despegar()
                elif metodo_nave == "cuenta_regresiva":
                    resultado = nave.cuenta_regresiva()
                elif metodo_nave == "chequeo_general":
                    resultado = nave.chequeo_general()
                elif metodo_nave == "aterrizar":
                    resultado = nave.aterrizar()
                elif metodo_nave == "separacion":
                    resultado = nave.separacion()
                elif metodo_nave == "abrir_paracaidas":
                    resultado = nave.abrir_paracaidas()
                self.lbl_resultado_conoce_tu_nave.setText(str(resultado))

    def registrar_nave(self):  # Metodo para registrar una nave
        if self.stackedWidget.currentWidget() == self.pg_crear_lanzadera:
            nave = Lanzadera(
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

            # Se obtiene el valor de los cuadros de texto
            validacion_campos_nulos = [
                QLineEdit.text()
                for QLineEdit in self.cuadros_texto_ventana_crear_lanzadera
                if QLineEdit.text() == ""
            ]

            if validacion_campos_nulos:  # Si hay campos nulos
                dialogo = QMessageBox.critical(
                    self, "Error", "Debes de llenar todos los campos"
                )
            else:  # Si no hay campos nulos
                # Se registra la nave en la base de datos
                QueriesBd.registrar_nave(self, nave)

                # Se limpian los cuadros de texto
                for QLineEdit in self.cuadros_texto_ventana_crear_lanzadera:
                    QLineEdit.clear()

                dialogo = QMessageBox.information(
                    self, "Operación éxitosa", "Tú nave fue creada correctamente"
                )

        elif self.stackedWidget.currentWidget() == self.pg_crear_tripulada:
            nave = Tripulada(
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

            # Se obtiene el valor de los cuadros de texto
            validacion_campos_nulos = [
                QLineEdit.text()
                for QLineEdit in self.cuadros_texto_ventana_crear_tripulada
                if QLineEdit.text() == ""
            ]

            if validacion_campos_nulos:  # Si hay campos nulos
                dialogo = QMessageBox.critical(
                    self, "Error", "Debes de llenar todos los campos"
                )
            else:  # Si no hay campos nulos
                # Se registra la nave en la base de datos
                QueriesBd.registrar_nave(self, nave)

                # Se limpian los cuadros de texto
                for QLineEdit in self.cuadros_texto_ventana_crear_tripulada:
                    QLineEdit.clear()

                dialogo = QMessageBox.information(
                    self, "Operación éxitosa", "Tú nave fue creada correctamente"
                )

        elif self.stackedWidget.currentWidget() == self.pg_crear_no_tripulada:
            nave = NoTripulada(
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

            # Se obtiene el valor de los cuadros de texto
            validacion_campos_nulos = [
                QLineEdit.text()
                for QLineEdit in self.cuadros_texto_ventana_crear_no_tripulada
                if QLineEdit.text() == ""
            ]

            if validacion_campos_nulos:  # Si hay campos nulos
                dialogo = QMessageBox.critical(
                    self, "Error", "Debes de llenar todos los campos"
                )
            else:  # Si no hay campos nulos
                # Se registra la nave en la base de datos
                QueriesBd.registrar_nave(self, nave)

                # Se limpian los cuadros de texto
                for QLineEdit in self.cuadros_texto_ventana_crear_no_tripulada:
                    QLineEdit.clear()

                dialogo = QMessageBox.information(
                    self, "Operación éxitosa", "Tú nave fue creada correctamente"
                )

    def consulta_general_naves(self):  # Metodo para consultar todas las naves
        # Se obtiene el tipo de nave
        tipo_de_nave = self.cBox_tipo_nave_general.currentText()

        # Se obtienen los datos de la base de datos
        datos = QueriesBd.consulta_general_naves(self, tipo_de_nave)

        # Se obtiene el número de filas
        filas = len(datos)

        # Se establece el número de filas
        self.tbl_consulta_sencilla.setRowCount(filas)

        # Se inicializa la fila
        fila_tabla = 0

        for fila in datos:
            self.tbl_consulta_sencilla.setItem(
                fila_tabla, 0, QtWidgets.QTableWidgetItem(fila[0])
            )
            self.tbl_consulta_sencilla.setItem(
                fila_tabla, 1, QtWidgets.QTableWidgetItem(fila[1])
            )
            self.tbl_consulta_sencilla.setItem(
                fila_tabla, 2, QtWidgets.QTableWidgetItem(str(fila[2]) + " kg")
            )
            self.tbl_consulta_sencilla.setItem(
                fila_tabla, 3, QtWidgets.QTableWidgetItem(str(fila[3]) + " km/s")
            )
            self.tbl_consulta_sencilla.setItem(
                fila_tabla, 4, QtWidgets.QTableWidgetItem(str(fila[4]))
            )

            # Se incrementa la fila
            fila_tabla += 1

    def consulta_avanzada_naves(self):  # Metodo avanzado para consultar naves
        # Se obtiene el tipo de nave
        tipo_nave = self.cBox_tipo_nave_avanzada.currentText()
        anio_nave = self.ql_anio_nave.text()  # Se obtiene el año de la nave
        pais_nave = self.ql_pais_nave.text()  # Se obtiene el país de la nave

        validacion_campos_nulos = [
            QLineEdit.text()
            for QLineEdit in self.cuadros_texto_consultas_avanzadas
            if QLineEdit.text() == ""
        ]

        if validacion_campos_nulos:  # Si hay campos nulos
            dialogo = QMessageBox.critical(
                self, "Error", "Debes de llenar todos los campos"
            )
        else:  # Si no hay campos nulos
            # Se obtienen los datos de la base de datos
            datos = QueriesBd.consulta_avanzada_naves(
                self, tipo_nave, anio_nave, pais_nave
            )

            # Se obtiene el número de filas
            filas = len(datos)

            # Se establece el número de filas
            self.tbl_consulta_avanzada.setRowCount(filas)

            # Se inicializa la fila
            fila_tabla = 0

            for fila in datos:
                self.tbl_consulta_avanzada.setItem(
                    fila_tabla, 0, QtWidgets.QTableWidgetItem(fila[0])
                )
                self.tbl_consulta_avanzada.setItem(
                    fila_tabla, 1, QtWidgets.QTableWidgetItem(fila[1])
                )
                self.tbl_consulta_avanzada.setItem(
                    fila_tabla, 2, QtWidgets.QTableWidgetItem(str(fila[2]) + " kg")
                )
                self.tbl_consulta_avanzada.setItem(
                    fila_tabla, 3, QtWidgets.QTableWidgetItem(str(fila[3]) + " km/s")
                )
                self.tbl_consulta_avanzada.setItem(
                    fila_tabla, 4, QtWidgets.QTableWidgetItem(str(fila[4]))
                )

                # Se incrementa la fila
                fila_tabla += 1

            # Se limpian los cuadros de texto
            for QLineEdit in self.cuadros_texto_consultas_avanzadas:
                QLineEdit.clear()
