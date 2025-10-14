from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi primera app con PySide6")
        self.setGeometry(100, 100, 300, 200)

        etiqueta = QLabel("¡Hola Mundo desde PySide6!", self)

        layout = QVBoxLayout()
        layout.addWidget(etiqueta)
        self.setLayout(layout)
