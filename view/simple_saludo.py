# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simple_saludo.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 150)
        Form.setMinimumSize(QSize(300, 150))
        Form.setMaximumSize(QSize(300, 150))
        Form.setSizeIncrement(QSize(300, 150))
        Form.setBaseSize(QSize(300, 150))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_name = QLineEdit(self.groupBox)
        self.line_name.setObjectName(u"line_name")
        self.line_name.setMaxLength(15)
        self.line_name.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.line_name, 0, 0, 1, 1)

        self.btn = QPushButton(self.groupBox)
        self.btn.setObjectName(u"btn")

        self.gridLayout_2.addWidget(self.btn, 1, 0, 1, 1)

        self.label_saludo = QLabel(self.groupBox)
        self.label_saludo.setObjectName(u"label_saludo")

        self.gridLayout_2.addWidget(self.label_saludo, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"main", None))
        self.line_name.setText("")
        self.line_name.setPlaceholderText(QCoreApplication.translate("Form", u"Tu Nombre ...", None))
        self.btn.setText(QCoreApplication.translate("Form", u"ok!", None))
        self.label_saludo.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">-------</span></p></body></html>", None))
    # retranslateUi

