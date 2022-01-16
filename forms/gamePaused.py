# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\gamePaused.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pauseDialog(object):
    def setupUi(self, pauseDialog):
        pauseDialog.setObjectName("pauseDialog")
        pauseDialog.resize(200, 150)
        self.verticalLayout = QtWidgets.QVBoxLayout(pauseDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.resumeButton = QtWidgets.QPushButton(pauseDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resumeButton.sizePolicy().hasHeightForWidth())
        self.resumeButton.setSizePolicy(sizePolicy)
        self.resumeButton.setObjectName("resumeButton")
        self.verticalLayout.addWidget(self.resumeButton)
        self.exitButton = QtWidgets.QPushButton(pauseDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout.addWidget(self.exitButton)

        self.retranslateUi(pauseDialog)
        self.exitButton.clicked.connect(pauseDialog.accept)
        self.resumeButton.clicked.connect(pauseDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(pauseDialog)

    def retranslateUi(self, pauseDialog):
        _translate = QtCore.QCoreApplication.translate
        pauseDialog.setWindowTitle(_translate("pauseDialog", "Paused"))
        self.resumeButton.setText(_translate("pauseDialog", "Resume"))
        self.exitButton.setText(_translate("pauseDialog", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pauseDialog = QtWidgets.QDialog()
    ui = Ui_pauseDialog()
    ui.setupUi(pauseDialog)
    pauseDialog.show()
    sys.exit(app.exec_())