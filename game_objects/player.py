from PyQt5.QtCore import QRectF, QPointF
from PyQt5.QtGui import QPixmap, QPainterPath
from PyQt5.QtWidgets import QGraphicsItem
from math import sqrt

import settings

class Player(QGraphicsItem):

    def __init__(self):
        super(Player, self).__init__()
        self.rect = QRectF(-settings.PLAYER_SIZE, -settings.PLAYER_SIZE, 2 * settings.PLAYER_SIZE, 2 * settings.PLAYER_SIZE)
        self.sprite_rect = QRectF(-settings.PLAYER_SIZE, -settings.PLAYER_SIZE, 2 * settings.PLAYER_SIZE, 2 * settings.PLAYER_SIZE)
        self.horizontal_speed = 0
        self.vertical_speed = 0
        self.position = QPointF(settings.PLAYING_FIELD_SIZE[0] / 2, settings.PLAYING_FIELD_SIZE[1] - 100)
        self.going_up = False
        self.going_down = False
        self.going_left = False
        self.going_right = False
        self.focused = False
        self.shooting = False
        self.dead = False
        self.setPos(self.position)
        self.sprite_image = QPixmap("assets/player.png")
    def boundingRect(self):
        return self.sprite_rect
    def shape(self):
        path = QPainterPath()
        path.addRect(self.sprite_rect)
        return path
    def paint(self, painter, option, widget):
        painter.drawPixmap(self.sprite_rect, self.sprite_image, QRectF(0, 0, 0, 0))
    
    def advance(self, phase):
        if phase == 0:
            return
        if self.going_up:
            self.vertical_speed = -settings.PLAYER_SPEED
        elif self.going_down:
            self.vertical_speed = settings.PLAYER_SPEED
        else:
            self.vertical_speed = 0
        if self.going_left:
            self.horizontal_speed = -settings.PLAYER_SPEED
        elif self.going_right:
            self.horizontal_speed = settings.PLAYER_SPEED
        else:
            self.horizontal_speed = 0
        if self.horizontal_speed != 0 and self.vertical_speed != 0:
            self.horizontal_speed /= sqrt(2)
            self.vertical_speed /= sqrt(2)

        if self.focused:
            self.horizontal_speed *= settings.PLAYER_FOCUS_SPEED_MULTIPLIER
            self.vertical_speed *= settings.PLAYER_FOCUS_SPEED_MULTIPLIER
        
        self.position.setX(self.position.x() + self.horizontal_speed)
        self.position.setY(self.position.y() + self.vertical_speed)

        if self.position.x() < settings.PLAYER_SIZE:
            self.position.setX(settings.PLAYER_SIZE)
        if self.position.y() < settings.PLAYER_SIZE:
            self.position.setY(settings.PLAYER_SIZE)
        if self.position.x() > settings.PLAYING_FIELD_SIZE[0] - settings.PLAYER_SIZE:
            self.position.setX(settings.PLAYING_FIELD_SIZE[0] - settings.PLAYER_SIZE)
        if self.position.y() > settings.PLAYING_FIELD_SIZE[1] - settings.PLAYER_SIZE:
            self.position.setY(settings.PLAYING_FIELD_SIZE[1] - settings.PLAYER_SIZE)

        self.setPos(self.position)

        if self.scene().collidingItems(self):
            self.dead = True
            self.scene().removeItem(self)
