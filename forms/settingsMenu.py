# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\settingsMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        settingsDialog.setObjectName("settingsDialog")
        settingsDialog.resize(180, 130)
        self.verticalLayout = QtWidgets.QVBoxLayout(settingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.easyButton = QtWidgets.QRadioButton(settingsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.easyButton.sizePolicy().hasHeightForWidth())
        self.easyButton.setSizePolicy(sizePolicy)
        self.easyButton.setObjectName("easyButton")
        self.buttonGroup = QtWidgets.QButtonGroup(settingsDialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.easyButton)
        self.verticalLayout.addWidget(self.easyButton)
        self.normalButton = QtWidgets.QRadioButton(settingsDialog)
        self.normalButton.setChecked(True)
        self.normalButton.setObjectName("normalButton")
        self.buttonGroup.addButton(self.normalButton)
        self.verticalLayout.addWidget(self.normalButton)
        self.hardButton = QtWidgets.QRadioButton(settingsDialog)
        self.hardButton.setObjectName("hardButton")
        self.buttonGroup.addButton(self.hardButton)
        self.verticalLayout.addWidget(self.hardButton)
        self.okButton = QtWidgets.QPushButton(settingsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okButton.sizePolicy().hasHeightForWidth())
        self.okButton.setSizePolicy(sizePolicy)
        self.okButton.setObjectName("okButton")
        self.verticalLayout.addWidget(self.okButton)

        self.retranslateUi(settingsDialog)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)

    def retranslateUi(self, settingsDialog):
        _translate = QtCore.QCoreApplication.translate
        settingsDialog.setWindowTitle(_translate("settingsDialog", "Settings"))
        self.easyButton.setText(_translate("settingsDialog", "Easy"))
        self.normalButton.setText(_translate("settingsDialog", "Normal"))
        self.hardButton.setText(_translate("settingsDialog", "Hard"))
        self.okButton.setText(_translate("settingsDialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settingsDialog = QtWidgets.QDialog()
    ui = Ui_settingsDialog()
    ui.setupUi(settingsDialog)
    settingsDialog.show()
    sys.exit(app.exec_())
