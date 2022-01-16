from PyQt5.QtWidgets import QApplication
import sys

from views.app import App

def run():
    app = QApplication(sys.argv)

    main = App()
    main.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
