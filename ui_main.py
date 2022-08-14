# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_uiJbAsRZ.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPlainTextEdit, QProgressBar, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(626, 355)
        self.sync_button = QPushButton(Dialog)
        self.sync_button.setObjectName(u"sync_button")
        self.sync_button.setGeometry(QRect(500, 90, 75, 23))
        self.server_ip_input = QLineEdit(Dialog)
        self.server_ip_input.setObjectName(u"server_ip_input")
        self.server_ip_input.setGeometry(QRect(30, 50, 113, 20))
        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 320, 451, 23))
        self.progressBar.setValue(24)
        self.server_port_input = QLineEdit(Dialog)
        self.server_port_input.setObjectName(u"server_port_input")
        self.server_port_input.setGeometry(QRect(160, 50, 113, 20))
        self.server_ip_text = QLabel(Dialog)
        self.server_ip_text.setObjectName(u"server_ip_text")
        self.server_ip_text.setGeometry(QRect(30, 30, 56, 12))
        self.port_text = QLabel(Dialog)
        self.port_text.setObjectName(u"port_text")
        self.port_text.setGeometry(QRect(160, 30, 56, 12))
        self.server_connect_button = QPushButton(Dialog)
        self.server_connect_button.setObjectName(u"server_connect_button")
        self.server_connect_button.setGeometry(QRect(280, 50, 75, 23))
        self.output_area = QPlainTextEdit(Dialog)
        self.output_area.setObjectName(u"output_area")
        self.output_area.setGeometry(QRect(30, 90, 411, 211))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.sync_button.setText(QCoreApplication.translate("Dialog", u"\ub3d9\uae30\ud654", None))
        self.server_ip_text.setText(QCoreApplication.translate("Dialog", u"Server IP", None))
        self.port_text.setText(QCoreApplication.translate("Dialog", u"Port", None))
        self.server_connect_button.setText(QCoreApplication.translate("Dialog", u"connect", None))
    # retranslateUi

