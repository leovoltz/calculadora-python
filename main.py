import sys

from main_window import MainWindow
from display import Display
from info import Info
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOWS_ICON_PATH
from styles import setupTheme
from buttons import Button


if __name__ == '__main__':
    # Cria a aplicação.
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Define o icone
    icon = QIcon(str(WINDOWS_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addToVLayout(info)

    # Display
    display = Display()
    window.addToVLayout(display)

    # Botões
    button = Button('Texto do botão')
    window.addToVLayout(button)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
