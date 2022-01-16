from PyQt5.QtCore import QTimer, QPointF
from PyQt5.QtWidgets import QMainWindow
from math import degrees, atan2
from random import randint

from forms import mainMenu
from .game_view import GameWindow
from .dialogs import PauseDialog, OverDialog
from game_objects.bullet import Bullet, PlayerBullet
import settings

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = mainMenu.Ui_mainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.playButton.clicked.connect(self.play)

    def play(self):
        self.hide()

        self.game_window = GameWindow()
        self.game_window.show()

        self.timer = QTimer()
        self.shooting_timer = QTimer()
        self.enemy_timer = QTimer()
        self.timer.timeout.connect(self.game_window.scene.advance)
        self.timer.timeout.connect(self.game_window.update_score)
        self.timer.timeout.connect(self.handle_player_shooting)
        self.timer.timeout.connect(self.handle_pausing)
        self.timer.timeout.connect(self.handle_enemy_hit)
        self.timer.timeout.connect(self.handle_player_dead)
        self.timer.start(int(1000 / settings.FPS))

        self.enemy_timer.timeout.connect(self.handle_enemy_movement)
        self.enemy_timer.timeout.connect(self.handle_enemy_shooting)
        self.enemy_timer.start(int(settings.ENEMY_MOVEMENT_INTERVAL * 1000))

        self.shooting_timer.timeout.connect(self.generate_player_bullet)

    def end_game(self):
        self.game_window.destroy()
        self.game_window = None
        self.timer.stop()
        self.show()

    def handle_pausing(self):
        if self.game_window is None:
            return
        if self.game_window.scene.paused:
            self.enemy_timer.stop()
            dialog = PauseDialog()
            if dialog.exec():
                self.end_game()
            else:
                self.enemy_timer.start()
                self.game_window.scene.paused = False

    def handle_enemy_hit(self):
        if self.game_window is None:
            return
        if self.game_window.scene.enemy.hit:
            self.game_window.score += settings.SCORE_INCREASE
            self.game_window.scene.enemy.hit = False
    def handle_enemy_movement(self):
        if self.game_window is None:
            return
        enemy = self.game_window.scene.enemy
        '''if enemy.x() < settings.PLAYING_FIELD_SIZE[0] / 2:
            enemy.destination = QPointF(random.randint(settings.PLAYING_FIELD_SIZE[0] / 2, settings.PLAYING_FIELD_SIZE[0]), random.randint(settings.ENEMY_SIZE, int(settings.PLAYING_FIELD_SIZE[1] / 1.5)))
        else:
            enemy.destination = QPointF(random.randint(settings.ENEMY_SIZE, settings.PLAYING_FIELD_SIZE[0] / 2), random.randint(settings.ENEMY_SIZE, int(settings.PLAYING_FIELD_SIZE[1] / 1.5)))'''
        enemy.destination = QPointF(randint(settings.ENEMY_SIZE, settings.PLAYING_FIELD_SIZE[0]), randint(settings.ENEMY_SIZE, int(settings.PLAYING_FIELD_SIZE[1] / 1.5)))
    def handle_enemy_shooting(self):
        if self.game_window is None:
            return
        scene = self.game_window.scene
        for i in range(0, 8):
            self.game_window.scene.addItem(Bullet(scene.enemy.pos(), 360 * i / 8))
        self.game_window.scene.addItem(Bullet(scene.enemy.pos(), degrees(atan2(scene.player.x() - scene.enemy.x(), scene.player.y() - scene.enemy.y())), 5))

    def handle_player_dead(self):
        if self.game_window is None:
            return
        if self.game_window.scene.player.dead:
            dialog = OverDialog(self.game_window.score)
            dialog.exec()
            self.end_game()
    def handle_player_shooting(self):
        if self.game_window.scene.player.shooting and not self.shooting_timer.isActive():
            self.generate_player_bullet()
            self.shooting_timer.start(int(1000 / settings.PLAYER_ROF))
        elif self.game_window.scene.player.shooting and self.shooting_timer.isActive():
            pass
        else:
            self.shooting_timer.stop()
    def generate_player_bullet(self):
        if self.game_window is None:
            return
        self.game_window.scene.addItem(PlayerBullet(QPointF(self.game_window.scene.player.x(), self.game_window.scene.player.y() - settings.PLAYER_SIZE - settings.BULLET_SIZE - settings.PLAYER_SPEED)))
