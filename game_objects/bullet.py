from PyQt5.QtCore import QRectF, QPointF
from PyQt5.QtGui import QPainterPath, QColor, QPixmap
from PyQt5.QtWidgets import QGraphicsItem
from math import sin, cos, radians

import settings
from .enemy import Enemy

class Bullet(QGraphicsItem):

    def __init__(self, position = QPointF(0, 0), angle = 0.0, speed = 3):
        super(Bullet, self).__init__()
        self.size = settings.BULLET_SIZE
        self.angle = angle
        self.speed = speed
        self.rect = QRectF(-self.size, -self.size, 2 * self.size, 2 * self.size)
        self.setPos(position)
    def boundingRect(self):
        return self.rect
    def shape(self):
        path = QPainterPath()
        path.addRect(self.rect)
        return path
    def paint(self, painter, option, widget):
        painter.setBrush(QColor(0, 255, 255))
        painter.drawEllipse(self.rect)
    
    def advance(self, phase):
        if phase == 0:
            return
        rd_angle = radians(self.angle)
        self.setPos(self.x() + sin(rd_angle) * self.speed, self.y() + cos(rd_angle) * self.speed)
        if self.x() < -settings.BULLET_SIZE:
            self.scene().removeItem(self)
        elif self.y() < -settings.BULLET_SIZE:
            self.scene().removeItem(self)
        elif self.x() > settings.PLAYING_FIELD_SIZE[0] + settings.BULLET_SIZE:
            self.scene().removeItem(self)
        elif self.y() > settings.PLAYING_FIELD_SIZE[1] + settings.BULLET_SIZE:
            self.scene().removeItem(self)

class PlayerBullet(Bullet):

    def __init__(self, position):
        super(PlayerBullet, self).__init__(position, 180.0, 10)
        self.sprite_image = QPixmap("assets/laserBullet.png")
    
    def paint(self, painter, option, widget):
        painter.drawPixmap(self.rect, self.sprite_image, QRectF(0, 0, 0, 0))

    def advance(self, phase):
        super(PlayerBullet, self).advance(phase)
        if self.scene() != None:
            if self.scene().collidingItems(self):
                if isinstance(self.scene().collidingItems(self)[0], Enemy):
                    self.scene().collidingItems(self)[0].hit = True
                    self.scene().removeItem(self)
