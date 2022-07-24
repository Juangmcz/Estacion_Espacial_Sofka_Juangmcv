# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowbNCpVt.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(944, 602)
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-image: url(:/imagenes/recursos/jeremy-perkins-uhjiu8FjnsQ-unsplash.jpg);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_encabezado = QFrame(self.frame)
        self.frame_encabezado.setObjectName(u"frame_encabezado")
        self.frame_encabezado.setStyleSheet(u"QPushButton{\n"
"background-color: #000000ff;\n"
"border-radius:20px;\n"
"}\n"
"QPushButtonhover{\n"
"background-color: rgb(61,61,61);\n"
"border-radius:20px;\n"
"}")
        self.frame_encabezado.setFrameShape(QFrame.StyledPanel)
        self.frame_encabezado.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_encabezado)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_menu = QPushButton(self.frame_encabezado)
        self.btn_menu.setObjectName(u"btn_menu")
        icon = QIcon()
        icon.addFile(u":/iconos/recursos/icons8-men\u00fa-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(100, 38))

        self.horizontalLayout_2.addWidget(self.btn_menu)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_minimizar = QPushButton(self.frame_encabezado)
        self.btn_minimizar.setObjectName(u"btn_minimizar")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/recursos/icons8-menos-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimizar.setIcon(icon1)
        self.btn_minimizar.setIconSize(QSize(38, 38))

        self.horizontalLayout_2.addWidget(self.btn_minimizar)

        self.btn_reducir = QPushButton(self.frame_encabezado)
        self.btn_reducir.setObjectName(u"btn_reducir")
        icon2 = QIcon()
        icon2.addFile(u":/iconos/recursos/icons8-achicar-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reducir.setIcon(icon2)
        self.btn_reducir.setIconSize(QSize(38, 38))

        self.horizontalLayout_2.addWidget(self.btn_reducir)

        self.btn_ampliar = QPushButton(self.frame_encabezado)
        self.btn_ampliar.setObjectName(u"btn_ampliar")
        icon3 = QIcon()
        icon3.addFile(u":/iconos/recursos/icons8-expandir-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ampliar.setIcon(icon3)
        self.btn_ampliar.setIconSize(QSize(38, 38))

        self.horizontalLayout_2.addWidget(self.btn_ampliar)

        self.btn_cerrar = QPushButton(self.frame_encabezado)
        self.btn_cerrar.setObjectName(u"btn_cerrar")
        icon4 = QIcon()
        icon4.addFile(u":/iconos/recursos/icons8-cerrar-ventana-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cerrar.setIcon(icon4)
        self.btn_cerrar.setIconSize(QSize(38, 38))

        self.horizontalLayout_2.addWidget(self.btn_cerrar)


        self.verticalLayout.addWidget(self.frame_encabezado)

        self.frame_contenido = QFrame(self.frame)
        self.frame_contenido.setObjectName(u"frame_contenido")
        self.frame_contenido.setFrameShape(QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_contenido)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.frame_control = QFrame(self.frame_contenido)
        self.frame_control.setObjectName(u"frame_control")
        self.frame_control.setMinimumSize(QSize(200, 0))
        self.frame_control.setMaximumSize(QSize(0, 16777215))
        self.frame_control.setStyleSheet(u"QFrame{\n"
"background-color: white;\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(61, 61, 61);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 77 10pt \"Arial Black\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"color: rgb(0, 0, 0);\n"
"font: 77 10pt \"Arial Black\";\n"
"}")
        self.frame_control.setFrameShape(QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_control)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.consultar_nave = QPushButton(self.frame_control)
        self.consultar_nave.setObjectName(u"consultar_nave")
        self.consultar_nave.setMinimumSize(QSize(0, 40))
        self.consultar_nave.setStyleSheet(u"QPushButton{\n"
"background-color: white;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/iconos/recursos/icons8-search-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.consultar_nave.setIcon(icon5)
        self.consultar_nave.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.consultar_nave)

        self.crear_tripulada = QPushButton(self.frame_control)
        self.crear_tripulada.setObjectName(u"crear_tripulada")
        self.crear_tripulada.setMinimumSize(QSize(0, 40))
        self.crear_tripulada.setStyleSheet(u"QPushButton{\n"
"background-color: white;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/iconos/recursos/icons8-ciencia-ficci\u00f3n-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.crear_tripulada.setIcon(icon6)
        self.crear_tripulada.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.crear_tripulada)

        self.crear_lanzadera = QPushButton(self.frame_control)
        self.crear_lanzadera.setObjectName(u"crear_lanzadera")
        self.crear_lanzadera.setMinimumSize(QSize(0, 40))
        self.crear_lanzadera.setStyleSheet(u"QPushButton{\n"
"background-color: white;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/iconos/recursos/icons8-cohete-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.crear_lanzadera.setIcon(icon7)
        self.crear_lanzadera.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.crear_lanzadera)

        self.crear_no_tripulada = QPushButton(self.frame_control)
        self.crear_no_tripulada.setObjectName(u"crear_no_tripulada")
        self.crear_no_tripulada.setMinimumSize(QSize(0, 40))
        self.crear_no_tripulada.setStyleSheet(u"QPushButton{\n"
"background-color: white;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/iconos/recursos/icons8-satelite-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.crear_no_tripulada.setIcon(icon8)
        self.crear_no_tripulada.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.crear_no_tripulada)


        self.horizontalLayout_3.addWidget(self.frame_control)

        self.frame_ventanas = QFrame(self.frame_contenido)
        self.frame_ventanas.setObjectName(u"frame_ventanas")
        self.frame_ventanas.setStyleSheet(u"QFrame{\n"
"background-color: rgb(61, 61, 61);\n"
"}\n"
"QLabel{\n"
"font: 87 12pt\"Arial Black\";\n"
"background-color: #000000ff;\n"
"color: rgb(0, 206, 151);\n"
"border: 0px solid #14C8DC;\n"
"}\n"
"QLineEdit{\n"
"border:0px;\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 2px solid rgb(61, 61, 61);\n"
"font: 75 10pt\"Arial Black\";\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"font: 77 10pt\"Arial Black\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 206, 151);\n"
"border-radius: 15px;\n"
"color: rgb(0, 0, 0);\n"
"font: 77 10pt\"Arial Black\";\n"
"}\n"
"QTableWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 206, 151);\n"
"font-size: 12pt;\n"
"color: #000000;\n"
"}\n"
"QHeaderView::section{\n"
"background-color: rgb(0, 206, 151);\n"
"border: 1px solid rgb(0, 0, 0);\n"
"font-size: 12pt;\n"
"}\n"
"QTableWidgetQTableCornerButton::section{\n"
"background-color: rgb(0, 0"
                        ", 0); \n"
"border: 1px solid rgb(0, 206, 151);\n"
"}")
        self.frame_ventanas.setFrameShape(QFrame.StyledPanel)
        self.frame_ventanas.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_ventanas)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_ventanas)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pg_crear_no_tripulada = QWidget()
        self.pg_crear_no_tripulada.setObjectName(u"pg_crear_no_tripulada")
        self.verticalLayout_6 = QVBoxLayout(self.pg_crear_no_tripulada)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_nave_no_tripulada = QLabel(self.pg_crear_no_tripulada)
        self.lbl_nave_no_tripulada.setObjectName(u"lbl_nave_no_tripulada")
        self.lbl_nave_no_tripulada.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lbl_nave_no_tripulada)

        self.verticalSpacer_3 = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lbl_nombre_no_tripulada = QLabel(self.pg_crear_no_tripulada)
        self.lbl_nombre_no_tripulada.setObjectName(u"lbl_nombre_no_tripulada")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lbl_nombre_no_tripulada)

        self.lbl_pais_no_tripulada = QLabel(self.pg_crear_no_tripulada)
        self.lbl_pais_no_tripulada.setObjectName(u"lbl_pais_no_tripulada")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lbl_pais_no_tripulada)

        self.lbl_peso_no_tripulada = QLabel(self.pg_crear_no_tripulada)
        self.lbl_peso_no_tripulada.setObjectName(u"lbl_peso_no_tripulada")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.lbl_peso_no_tripulada)

        self.lbl_empuje_no_tripulada = QLabel(self.pg_crear_no_tripulada)
        self.lbl_empuje_no_tripulada.setObjectName(u"lbl_empuje_no_tripulada")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.lbl_empuje_no_tripulada)

        self.lbl_velocidad_no_tripulada = QLabel(self.pg_crear_no_tripulada)
        self.lbl_velocidad_no_tripulada.setObjectName(u"lbl_velocidad_no_tripulada")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.lbl_velocidad_no_tripulada)

        self.lbl_combustible_no_tripulada = QLabel(self.pg_crear_no_tripulada)
        self.lbl_combustible_no_tripulada.setObjectName(u"lbl_combustible_no_tripulada")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.lbl_combustible_no_tripulada)

        self.lbl_cantidad_motores_no_tripulada = QLabel(self.pg_crear_no_tripulada)
        self.lbl_cantidad_motores_no_tripulada.setObjectName(u"lbl_cantidad_motores_no_tripulada")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.lbl_cantidad_motores_no_tripulada)

        self.lbl_planeta_exploracion_no_tripulada = QLabel(self.pg_crear_no_tripulada)
        self.lbl_planeta_exploracion_no_tripulada.setObjectName(u"lbl_planeta_exploracion_no_tripulada")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.lbl_planeta_exploracion_no_tripulada)

        self.ql_nombre_no_tripulada = QLineEdit(self.pg_crear_no_tripulada)
        self.ql_nombre_no_tripulada.setObjectName(u"ql_nombre_no_tripulada")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.ql_nombre_no_tripulada)

        self.ql_pais_no_tripulada = QLineEdit(self.pg_crear_no_tripulada)
        self.ql_pais_no_tripulada.setObjectName(u"ql_pais_no_tripulada")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.ql_pais_no_tripulada)

        self.ql_peso_no_tripulada = QLineEdit(self.pg_crear_no_tripulada)
        self.ql_peso_no_tripulada.setObjectName(u"ql_peso_no_tripulada")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.ql_peso_no_tripulada)

        self.ql_empuje_no_tripulada = QLineEdit(self.pg_crear_no_tripulada)
        self.ql_empuje_no_tripulada.setObjectName(u"ql_empuje_no_tripulada")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.ql_empuje_no_tripulada)

        self.ql_velocidad_no_tripulada = QLineEdit(self.pg_crear_no_tripulada)
        self.ql_velocidad_no_tripulada.setObjectName(u"ql_velocidad_no_tripulada")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.ql_velocidad_no_tripulada)

        self.ql_combustible_no_tripulada = QLineEdit(self.pg_crear_no_tripulada)
        self.ql_combustible_no_tripulada.setObjectName(u"ql_combustible_no_tripulada")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.ql_combustible_no_tripulada)

        self.ql_cantidad_motores_no_tripulada = QLineEdit(self.pg_crear_no_tripulada)
        self.ql_cantidad_motores_no_tripulada.setObjectName(u"ql_cantidad_motores_no_tripulada")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.ql_cantidad_motores_no_tripulada)

        self.ql_planeta_exploracion_no_tripulada = QLineEdit(self.pg_crear_no_tripulada)
        self.ql_planeta_exploracion_no_tripulada.setObjectName(u"ql_planeta_exploracion_no_tripulada")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.ql_planeta_exploracion_no_tripulada)

        self.lbl_anio_no_tripulada = QLabel(self.pg_crear_no_tripulada)
        self.lbl_anio_no_tripulada.setObjectName(u"lbl_anio_no_tripulada")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lbl_anio_no_tripulada)

        self.ql_anio_no_tripulada = QLineEdit(self.pg_crear_no_tripulada)
        self.ql_anio_no_tripulada.setObjectName(u"ql_anio_no_tripulada")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.ql_anio_no_tripulada)


        self.verticalLayout_6.addLayout(self.formLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 57, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.btn_registrar_no_tripulada = QPushButton(self.pg_crear_no_tripulada)
        self.btn_registrar_no_tripulada.setObjectName(u"btn_registrar_no_tripulada")

        self.horizontalLayout_6.addWidget(self.btn_registrar_no_tripulada)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)

        self.stackedWidget.addWidget(self.pg_crear_no_tripulada)
        self.pg_consultas = QWidget()
        self.pg_consultas.setObjectName(u"pg_consultas")
        self.verticalLayout_4 = QVBoxLayout(self.pg_consultas)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_consulta_general = QLabel(self.pg_consultas)
        self.lbl_consulta_general.setObjectName(u"lbl_consulta_general")
        self.lbl_consulta_general.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_consulta_general)

        self.tbl_consulta_sencilla = QTableWidget(self.pg_consultas)
        if (self.tbl_consulta_sencilla.columnCount() < 6):
            self.tbl_consulta_sencilla.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_consulta_sencilla.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_consulta_sencilla.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_consulta_sencilla.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_consulta_sencilla.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_consulta_sencilla.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_consulta_sencilla.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tbl_consulta_sencilla.setObjectName(u"tbl_consulta_sencilla")
        self.tbl_consulta_sencilla.setMinimumSize(QSize(700, 178))
        self.tbl_consulta_sencilla.setMaximumSize(QSize(700, 178))

        self.verticalLayout_4.addWidget(self.tbl_consulta_sencilla)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.btn_consulta_sencilla = QPushButton(self.pg_consultas)
        self.btn_consulta_sencilla.setObjectName(u"btn_consulta_sencilla")
        self.btn_consulta_sencilla.setMinimumSize(QSize(100, 40))
        self.btn_consulta_sencilla.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_4.addWidget(self.btn_consulta_sencilla)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.lbl_consulta_avanzada = QLabel(self.pg_consultas)
        self.lbl_consulta_avanzada.setObjectName(u"lbl_consulta_avanzada")
        self.lbl_consulta_avanzada.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_consulta_avanzada)

        self.tbl_consulta_avanzada = QTableWidget(self.pg_consultas)
        if (self.tbl_consulta_avanzada.columnCount() < 6):
            self.tbl_consulta_avanzada.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbl_consulta_avanzada.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbl_consulta_avanzada.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbl_consulta_avanzada.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbl_consulta_avanzada.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbl_consulta_avanzada.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tbl_consulta_avanzada.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.tbl_consulta_avanzada.setObjectName(u"tbl_consulta_avanzada")
        self.tbl_consulta_avanzada.setMinimumSize(QSize(700, 0))
        self.tbl_consulta_avanzada.setMaximumSize(QSize(700, 166))

        self.verticalLayout_4.addWidget(self.tbl_consulta_avanzada)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.ql_ano_nave = QLineEdit(self.pg_consultas)
        self.ql_ano_nave.setObjectName(u"ql_ano_nave")

        self.gridLayout.addWidget(self.ql_ano_nave, 1, 1, 1, 1)

        self.btn_consulta_avanzada = QPushButton(self.pg_consultas)
        self.btn_consulta_avanzada.setObjectName(u"btn_consulta_avanzada")
        self.btn_consulta_avanzada.setMinimumSize(QSize(100, 40))
        self.btn_consulta_avanzada.setMaximumSize(QSize(100, 40))

        self.gridLayout.addWidget(self.btn_consulta_avanzada, 1, 3, 1, 1)

        self.ql_tipo_nave = QLineEdit(self.pg_consultas)
        self.ql_tipo_nave.setObjectName(u"ql_tipo_nave")

        self.gridLayout.addWidget(self.ql_tipo_nave, 1, 0, 1, 1)

        self.ql_pais_nave = QLineEdit(self.pg_consultas)
        self.ql_pais_nave.setObjectName(u"ql_pais_nave")

        self.gridLayout.addWidget(self.ql_pais_nave, 1, 2, 1, 1)

        self.lbl_tipo_nave = QLabel(self.pg_consultas)
        self.lbl_tipo_nave.setObjectName(u"lbl_tipo_nave")

        self.gridLayout.addWidget(self.lbl_tipo_nave, 0, 0, 1, 1)

        self.lbl_ano = QLabel(self.pg_consultas)
        self.lbl_ano.setObjectName(u"lbl_ano")

        self.gridLayout.addWidget(self.lbl_ano, 0, 1, 1, 1)

        self.lbl_pais_nave = QLabel(self.pg_consultas)
        self.lbl_pais_nave.setObjectName(u"lbl_pais_nave")

        self.gridLayout.addWidget(self.lbl_pais_nave, 0, 2, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.pg_consultas)
        self.lbl_consulta_general.raise_()
        self.tbl_consulta_sencilla.raise_()
        self.tbl_consulta_avanzada.raise_()
        self.lbl_consulta_avanzada.raise_()
        self.pg_crear_lanzadera = QWidget()
        self.pg_crear_lanzadera.setObjectName(u"pg_crear_lanzadera")
        self.verticalLayout_7 = QVBoxLayout(self.pg_crear_lanzadera)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_lanzadera = QLabel(self.pg_crear_lanzadera)
        self.label_lanzadera.setObjectName(u"label_lanzadera")
        self.label_lanzadera.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_lanzadera)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.lbl_nombre_lanzadera = QLabel(self.pg_crear_lanzadera)
        self.lbl_nombre_lanzadera.setObjectName(u"lbl_nombre_lanzadera")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.lbl_nombre_lanzadera)

        self.ql_nombre_lanzadera = QLineEdit(self.pg_crear_lanzadera)
        self.ql_nombre_lanzadera.setObjectName(u"ql_nombre_lanzadera")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.ql_nombre_lanzadera)

        self.lbl_pais_lanzadera = QLabel(self.pg_crear_lanzadera)
        self.lbl_pais_lanzadera.setObjectName(u"lbl_pais_lanzadera")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.lbl_pais_lanzadera)

        self.ql_pais_lanzadera = QLineEdit(self.pg_crear_lanzadera)
        self.ql_pais_lanzadera.setObjectName(u"ql_pais_lanzadera")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.ql_pais_lanzadera)

        self.lbl_peso_lanzadera = QLabel(self.pg_crear_lanzadera)
        self.lbl_peso_lanzadera.setObjectName(u"lbl_peso_lanzadera")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.lbl_peso_lanzadera)

        self.ql_peso_lanzadera = QLineEdit(self.pg_crear_lanzadera)
        self.ql_peso_lanzadera.setObjectName(u"ql_peso_lanzadera")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.ql_peso_lanzadera)

        self.lbl_altura_lanzadera = QLabel(self.pg_crear_lanzadera)
        self.lbl_altura_lanzadera.setObjectName(u"lbl_altura_lanzadera")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.lbl_altura_lanzadera)

        self.ql_altura_lanzadera = QLineEdit(self.pg_crear_lanzadera)
        self.ql_altura_lanzadera.setObjectName(u"ql_altura_lanzadera")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.ql_altura_lanzadera)

        self.lbl_potencia_lanzadera = QLabel(self.pg_crear_lanzadera)
        self.lbl_potencia_lanzadera.setObjectName(u"lbl_potencia_lanzadera")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.lbl_potencia_lanzadera)

        self.ql_potencia_lanzadera = QLineEdit(self.pg_crear_lanzadera)
        self.ql_potencia_lanzadera.setObjectName(u"ql_potencia_lanzadera")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.ql_potencia_lanzadera)

        self.lbl_velocidad_lanzadera = QLabel(self.pg_crear_lanzadera)
        self.lbl_velocidad_lanzadera.setObjectName(u"lbl_velocidad_lanzadera")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.lbl_velocidad_lanzadera)

        self.ql_velocidad_lanzadera = QLineEdit(self.pg_crear_lanzadera)
        self.ql_velocidad_lanzadera.setObjectName(u"ql_velocidad_lanzadera")

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.ql_velocidad_lanzadera)

        self.lbl_carga_util_lanzadera = QLabel(self.pg_crear_lanzadera)
        self.lbl_carga_util_lanzadera.setObjectName(u"lbl_carga_util_lanzadera")

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.lbl_carga_util_lanzadera)

        self.ql_carga_util_lanzadera = QLineEdit(self.pg_crear_lanzadera)
        self.ql_carga_util_lanzadera.setObjectName(u"ql_carga_util_lanzadera")

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.ql_carga_util_lanzadera)

        self.lbl_autonomia_lanzadera = QLabel(self.pg_crear_lanzadera)
        self.lbl_autonomia_lanzadera.setObjectName(u"lbl_autonomia_lanzadera")

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.lbl_autonomia_lanzadera)

        self.ql_autonomia_lanzadera = QLineEdit(self.pg_crear_lanzadera)
        self.ql_autonomia_lanzadera.setObjectName(u"ql_autonomia_lanzadera")

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.ql_autonomia_lanzadera)

        self.lbl_combustible_lanzadera = QLabel(self.pg_crear_lanzadera)
        self.lbl_combustible_lanzadera.setObjectName(u"lbl_combustible_lanzadera")

        self.formLayout_3.setWidget(9, QFormLayout.LabelRole, self.lbl_combustible_lanzadera)

        self.ql_combustible_lanzadera = QLineEdit(self.pg_crear_lanzadera)
        self.ql_combustible_lanzadera.setObjectName(u"ql_combustible_lanzadera")

        self.formLayout_3.setWidget(9, QFormLayout.FieldRole, self.ql_combustible_lanzadera)

        self.lbl_anio_lanzadera = QLabel(self.pg_crear_lanzadera)
        self.lbl_anio_lanzadera.setObjectName(u"lbl_anio_lanzadera")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.lbl_anio_lanzadera)

        self.ql_anio_lanzadera = QLineEdit(self.pg_crear_lanzadera)
        self.ql_anio_lanzadera.setObjectName(u"ql_anio_lanzadera")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.ql_anio_lanzadera)


        self.verticalLayout_7.addLayout(self.formLayout_3)

        self.verticalSpacer_7 = QSpacerItem(20, 41, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.btn_registrar_lanzadera = QPushButton(self.pg_crear_lanzadera)
        self.btn_registrar_lanzadera.setObjectName(u"btn_registrar_lanzadera")

        self.horizontalLayout_7.addWidget(self.btn_registrar_lanzadera)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_8)

        self.stackedWidget.addWidget(self.pg_crear_lanzadera)
        self.pg_crear_tripulada = QWidget()
        self.pg_crear_tripulada.setObjectName(u"pg_crear_tripulada")
        self.verticalLayout_3 = QVBoxLayout(self.pg_crear_tripulada)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_nave_tripulada = QLabel(self.pg_crear_tripulada)
        self.lbl_nave_tripulada.setObjectName(u"lbl_nave_tripulada")
        self.lbl_nave_tripulada.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_nave_tripulada)

        self.verticalSpacer = QSpacerItem(20, 61, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_nombre_tripulada = QLabel(self.pg_crear_tripulada)
        self.lbl_nombre_tripulada.setObjectName(u"lbl_nombre_tripulada")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_nombre_tripulada)

        self.lbl_pais_tripulada = QLabel(self.pg_crear_tripulada)
        self.lbl_pais_tripulada.setObjectName(u"lbl_pais_tripulada")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_pais_tripulada)

        self.lbl_peso_tripulada = QLabel(self.pg_crear_tripulada)
        self.lbl_peso_tripulada.setObjectName(u"lbl_peso_tripulada")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_peso_tripulada)

        self.lbl_orbita_tripulada = QLabel(self.pg_crear_tripulada)
        self.lbl_orbita_tripulada.setObjectName(u"lbl_orbita_tripulada")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lbl_orbita_tripulada)

        self.lbl_capacidad_tripulada = QLabel(self.pg_crear_tripulada)
        self.lbl_capacidad_tripulada.setObjectName(u"lbl_capacidad_tripulada")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lbl_capacidad_tripulada)

        self.lbl_velocidad_tripulada = QLabel(self.pg_crear_tripulada)
        self.lbl_velocidad_tripulada.setObjectName(u"lbl_velocidad_tripulada")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lbl_velocidad_tripulada)

        self.lbl_tipo_mision_tripulada = QLabel(self.pg_crear_tripulada)
        self.lbl_tipo_mision_tripulada.setObjectName(u"lbl_tipo_mision_tripulada")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.lbl_tipo_mision_tripulada)

        self.lbl_nombre_mision_tripulada = QLabel(self.pg_crear_tripulada)
        self.lbl_nombre_mision_tripulada.setObjectName(u"lbl_nombre_mision_tripulada")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.lbl_nombre_mision_tripulada)

        self.ql_nombre_tripulada = QLineEdit(self.pg_crear_tripulada)
        self.ql_nombre_tripulada.setObjectName(u"ql_nombre_tripulada")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ql_nombre_tripulada)

        self.ql_pais_tripulada = QLineEdit(self.pg_crear_tripulada)
        self.ql_pais_tripulada.setObjectName(u"ql_pais_tripulada")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.ql_pais_tripulada)

        self.ql_peso_tripulada = QLineEdit(self.pg_crear_tripulada)
        self.ql_peso_tripulada.setObjectName(u"ql_peso_tripulada")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.ql_peso_tripulada)

        self.ql_orbita_tripulada = QLineEdit(self.pg_crear_tripulada)
        self.ql_orbita_tripulada.setObjectName(u"ql_orbita_tripulada")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.ql_orbita_tripulada)

        self.ql_capacidad_tripulada = QLineEdit(self.pg_crear_tripulada)
        self.ql_capacidad_tripulada.setObjectName(u"ql_capacidad_tripulada")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.ql_capacidad_tripulada)

        self.ql_velocidad_tripulada = QLineEdit(self.pg_crear_tripulada)
        self.ql_velocidad_tripulada.setObjectName(u"ql_velocidad_tripulada")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.ql_velocidad_tripulada)

        self.ql_tipo_mision_tripulada = QLineEdit(self.pg_crear_tripulada)
        self.ql_tipo_mision_tripulada.setObjectName(u"ql_tipo_mision_tripulada")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.ql_tipo_mision_tripulada)

        self.ql_nombre_mision_tripulada = QLineEdit(self.pg_crear_tripulada)
        self.ql_nombre_mision_tripulada.setObjectName(u"ql_nombre_mision_tripulada")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.ql_nombre_mision_tripulada)

        self.lbl_anio_tripulada = QLabel(self.pg_crear_tripulada)
        self.lbl_anio_tripulada.setObjectName(u"lbl_anio_tripulada")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_anio_tripulada)

        self.ql_anio_tripulada = QLineEdit(self.pg_crear_tripulada)
        self.ql_anio_tripulada.setObjectName(u"ql_anio_tripulada")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ql_anio_tripulada)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 62, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.btn_registrar_tripulada = QPushButton(self.pg_crear_tripulada)
        self.btn_registrar_tripulada.setObjectName(u"btn_registrar_tripulada")

        self.horizontalLayout_5.addWidget(self.btn_registrar_tripulada)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.stackedWidget.addWidget(self.pg_crear_tripulada)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.frame_ventanas)

        self.frame_ventanas.raise_()
        self.frame_control.raise_()

        self.verticalLayout.addWidget(self.frame_contenido)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)

        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Nave Espacial Sofka", None))
        self.btn_menu.setText("")
        self.btn_minimizar.setText("")
        self.btn_reducir.setText("")
        self.btn_ampliar.setText("")
        self.btn_cerrar.setText("")
        self.consultar_nave.setText(QCoreApplication.translate("MainWindow", u"Consultar Naves", None))
        self.crear_tripulada.setText(QCoreApplication.translate("MainWindow", u"Crear Tripulada", None))
        self.crear_lanzadera.setText(QCoreApplication.translate("MainWindow", u"Crear Lanzadera", None))
        self.crear_no_tripulada.setText(QCoreApplication.translate("MainWindow", u"Crear No Tripulada", None))
        self.lbl_nave_no_tripulada.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR NAVE NO TRIPULADA", None))
        self.lbl_nombre_no_tripulada.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.lbl_pais_no_tripulada.setText(QCoreApplication.translate("MainWindow", u"Pais", None))
        self.lbl_peso_no_tripulada.setText(QCoreApplication.translate("MainWindow", u"Peso", None))
        self.lbl_empuje_no_tripulada.setText(QCoreApplication.translate("MainWindow", u"Empuje", None))
        self.lbl_velocidad_no_tripulada.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.lbl_combustible_no_tripulada.setText(QCoreApplication.translate("MainWindow", u"Combustible", None))
        self.lbl_cantidad_motores_no_tripulada.setText(QCoreApplication.translate("MainWindow", u"Cantidad de motores", None))
        self.lbl_planeta_exploracion_no_tripulada.setText(QCoreApplication.translate("MainWindow", u"Planeta de exploraci\u00f3n", None))
        self.lbl_anio_no_tripulada.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None))
        self.btn_registrar_no_tripulada.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
        self.lbl_consulta_general.setText(QCoreApplication.translate("MainWindow", u"CONSULTA GENERAL", None))
        ___qtablewidgetitem = self.tbl_consulta_sencilla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem1 = self.tbl_consulta_sencilla.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Pais", None));
        ___qtablewidgetitem2 = self.tbl_consulta_sencilla.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Peso", None));
        ___qtablewidgetitem3 = self.tbl_consulta_sencilla.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None));
        ___qtablewidgetitem4 = self.tbl_consulta_sencilla.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"TipoNave", None));
        ___qtablewidgetitem5 = self.tbl_consulta_sencilla.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None));
        self.btn_consulta_sencilla.setText(QCoreApplication.translate("MainWindow", u"CONSULTAR", None))
        self.lbl_consulta_avanzada.setText(QCoreApplication.translate("MainWindow", u"CONSULTA AVANZADA", None))
        ___qtablewidgetitem6 = self.tbl_consulta_avanzada.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem7 = self.tbl_consulta_avanzada.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Pais", None));
        ___qtablewidgetitem8 = self.tbl_consulta_avanzada.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Peso", None));
        ___qtablewidgetitem9 = self.tbl_consulta_avanzada.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None));
        ___qtablewidgetitem10 = self.tbl_consulta_avanzada.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"TipoNave", None));
        ___qtablewidgetitem11 = self.tbl_consulta_avanzada.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None));
        self.btn_consulta_avanzada.setText(QCoreApplication.translate("MainWindow", u"CONSULTAR", None))
        self.lbl_tipo_nave.setText(QCoreApplication.translate("MainWindow", u"Tipo de Nave", None))
        self.lbl_ano.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None))
        self.lbl_pais_nave.setText(QCoreApplication.translate("MainWindow", u"Pa\u00eds", None))
        self.label_lanzadera.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR LANZADERA", None))
        self.lbl_nombre_lanzadera.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.lbl_pais_lanzadera.setText(QCoreApplication.translate("MainWindow", u"Pais", None))
        self.lbl_peso_lanzadera.setText(QCoreApplication.translate("MainWindow", u"Peso", None))
        self.lbl_altura_lanzadera.setText(QCoreApplication.translate("MainWindow", u"Altura", None))
        self.lbl_potencia_lanzadera.setText(QCoreApplication.translate("MainWindow", u"Potencia", None))
        self.lbl_velocidad_lanzadera.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.lbl_carga_util_lanzadera.setText(QCoreApplication.translate("MainWindow", u"Carga \u00datil", None))
        self.lbl_autonomia_lanzadera.setText(QCoreApplication.translate("MainWindow", u"Autonomia", None))
        self.lbl_combustible_lanzadera.setText(QCoreApplication.translate("MainWindow", u"Combustible", None))
        self.lbl_anio_lanzadera.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None))
        self.btn_registrar_lanzadera.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
        self.lbl_nave_tripulada.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR NAVE TRIPULADA", None))
        self.lbl_nombre_tripulada.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.lbl_pais_tripulada.setText(QCoreApplication.translate("MainWindow", u"Pais", None))
        self.lbl_peso_tripulada.setText(QCoreApplication.translate("MainWindow", u"Peso", None))
        self.lbl_orbita_tripulada.setText(QCoreApplication.translate("MainWindow", u"Orbita", None))
        self.lbl_capacidad_tripulada.setText(QCoreApplication.translate("MainWindow", u"Capacidad", None))
        self.lbl_velocidad_tripulada.setText(QCoreApplication.translate("MainWindow", u"Valocidad", None))
        self.lbl_tipo_mision_tripulada.setText(QCoreApplication.translate("MainWindow", u"Tipo de Misi\u00f3n", None))
        self.lbl_nombre_mision_tripulada.setText(QCoreApplication.translate("MainWindow", u"Nombre de la Misi\u00f3n", None))
        self.lbl_anio_tripulada.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None))
        self.btn_registrar_tripulada.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
    # retranslateUi

