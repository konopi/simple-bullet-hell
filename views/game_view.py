from PyQt5.Qt import Qt
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QWidget
from PyQt5.QtGui import QPixmap, QPainter, QBrush

from game_objects.player import Player
from game_objects.enemy import Enemy
from forms import gameView
import settings

class GameScene(QGraphicsScene):

    def __init__(self):
        super(GameScene, self).__init__()
        self.player = Player()
        self.enemy = Enemy()
        self.paused = False

    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_Up:
            self.player.going_up = True
        if e.key() == Qt.Key.Key_Down:
            self.player.going_down = True
        if e.key() == Qt.Key.Key_Left:
            self.player.going_left = True
        if e.key() == Qt.Key.Key_Right:
            self.player.going_right = True

        if e.key() == Qt.Key.Key_Shift:
            self.player.focused = True
        if e.key() == Qt.Key.Key_Z:
            self.player.shooting = True

        if e.key() == Qt.Key.Key_Escape:
            self.paused = True
        
    def keyReleaseEvent(self, e):
        if e.key() == Qt.Key.Key_Up:
            self.player.going_up = False
        if e.key() == Qt.Key.Key_Down:
            self.player.going_down = False
        if e.key() == Qt.Key.Key_Left:
            self.player.going_left = False
        if e.key() == Qt.Key.Key_Right:
            self.player.going_right = False

        if e.key() == Qt.Key.Key_Shift:
            self.player.focused = False
        if e.key() == Qt.Key.Key_Z:
            self.player.shooting = False

class GameWindow(QWidget):

    def __init__(self):
        super(GameWindow, self).__init__()
        self.ui = gameView.Ui_GameView()
        self.ui.setupUi(self)
        self.score = 0
        self.background_image = QPixmap("assets/back.png")
        self.init_ui()

    def init_ui(self):
        #self.setFixedSize(self.size())
        # resizeEvent

        self.scene = GameScene()
        self.scene.setSceneRect(0, 0, settings.PLAYING_FIELD_SIZE[0], settings.PLAYING_FIELD_SIZE[1])
        self.scene.setItemIndexMethod(QGraphicsScene.ItemIndexMethod.NoIndex)

        self.scene.addItem(self.scene.player)
        self.scene.addItem(self.scene.enemy)

        self.ui.playField.setScene(self.scene)
        self.ui.playField.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.ui.playField.setBackgroundBrush(QBrush(self.background_image))

        self.ui.playField.setCacheMode(QGraphicsView.CacheModeFlag.CacheBackground)
        self.ui.playField.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.BoundingRectViewportUpdate)
        self.ui.playField.setDragMode(QGraphicsView.DragMode.NoDrag)

    def update_score(self):
        _translate = QCoreApplication.translate
        self.ui.sPointsLabel.setText(_translate("GameView", "<html><head/><body><p align=\"right\"><span style=\" font-size:16pt;\">" + str(self.score) + "</span></p></body></html>"))
