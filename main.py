import sys
from PySide6.QtWidgets import QApplication  # Importar la clase QApplication
from gui.interfaz import MainWindow  # Importar la clase MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crear la aplicacion
    window = MainWindow()  # Crear la ventana
    window.show()  # Mostrar la ventana
    sys.exit(app.exec())  # Ejecutar la aplicacion
