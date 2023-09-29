import sys

from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOWS_ICON_PATH


if __name__ == '__main__':
    # Cria a aplicação.
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define o icone
    icon = QIcon(str(WINDOWS_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
