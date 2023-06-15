import sys
from PyQt5.QtWidgets import QApplication
from GUI.LogIn.LogIn import LogIn


def main():
    app = QApplication(sys.argv)
    # Crear la interfaz
    log_in = LogIn()
    log_in.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
