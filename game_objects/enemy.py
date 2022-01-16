from PyQt5.QtCore import QRectF, QPointF
from PyQt5.QtGui import QPixmap, QPainterPath
from PyQt5.Qt import QTransform
from PyQt5.QtWidgets import QGraphicsItem
from math import atan2, sin, cos

import settings

class Enemy(QGraphicsItem):
#QGraphicsRectItem
    def __init__(self, position = QPointF(100, 100)):
        super(Enemy, self).__init__()
        self.rect = QRectF(-settings.ENEMY_SIZE, -settings.ENEMY_SIZE, 2 * settings.ENEMY_SIZE, 2 * settings.ENEMY_SIZE)
        self.sprite_image = QPixmap("assets/enemy.png")
        self.sprite_image = self.sprite_image.transformed(QTransform().rotate(180))
        self.horizontal_speed = 0
        self.vertical_speed = 0
        self.hit = False
        self.position = position
        self.destination = position
        self.angle = 90.0
        self.setPos(self.position)
    def boundingRect(self):
        return self.rect
    def shape(self):
        path = QPainterPath()
        path.addRect(self.rect)
        return path
    def paint(self, painter, option, widget):
        painter.drawPixmap(self.rect, self.sprite_image, QRectF(0, 0, 0, 0))

    def advance(self, phase):
        if phase == 0:
            return
        self.angle = atan2(self.destination.x() - self.x(), self.destination.y() - self.y())
        if self.destination != self.pos():
            self.setPos(self.x() + sin(self.angle) * settings.ENEMY_SPEED, self.y() + cos(self.angle) * settings.ENEMY_SPEED)
