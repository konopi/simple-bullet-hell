from PyQt5.Qt import Qt
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QDialog

from forms import gameOver, gamePaused, settingsMenu

class OverDialog(QDialog):
    def __init__(self, score):
        super(OverDialog, self).__init__()
        self.ui = gameOver.Ui_GameOver()
        self.ui.setupUi(self)
        self.init_ui(score)

    def init_ui(self, score):
        self.setWindowFlags(Qt.WindowType.SplashScreen)
        _translate = QCoreApplication.translate
        self.ui.finalLabel.setText(_translate("GameOver", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Game Over<br/><br/>Final score<br/>" + str(score) + "</span></p></body></html>"))

class PauseDialog(QDialog):
    def __init__(self):
        super(PauseDialog, self).__init__()
        self.ui = gamePaused.Ui_pauseDialog()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowFlags(Qt.WindowType.SplashScreen)

class SettingsDialog(QDialog):
    def __init__(self):
        super(SettingsDialog, self).__init__()
        self.ui = settingsMenu.Ui_settingsDialog()
        self.ui.setupUi(self)
