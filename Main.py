from PyQt5.QtWidgets import QApplication

from src.user_interface.UI import Main_UI


def main():
    app = QApplication([])
    window = Main_UI()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
