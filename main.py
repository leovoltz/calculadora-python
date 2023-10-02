import sys

from main_window import MainWindow
from display import Display
from info import Info
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOWS_ICON_PATH
from styles import setupTheme
from buttons import ButtonsGrid


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
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Botões

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
