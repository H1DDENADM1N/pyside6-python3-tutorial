# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWinVHLayout.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPlainTextEdit, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(352, 213)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_welcome = QLabel(self.centralwidget)
        self.label_welcome.setObjectName(u"label_welcome")

        self.verticalLayout.addWidget(self.label_welcome)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_username = QLabel(self.centralwidget)
        self.label_username.setObjectName(u"label_username")

        self.horizontalLayout.addWidget(self.label_username)

        self.lineEdit_username = QLineEdit(self.centralwidget)
        self.lineEdit_username.setObjectName(u"lineEdit_username")

        self.horizontalLayout.addWidget(self.lineEdit_username)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_password = QHBoxLayout()
        self.horizontalLayout_password.setObjectName(u"horizontalLayout_password")
        self.label_password = QLabel(self.centralwidget)
        self.label_password.setObjectName(u"label_password")

        self.horizontalLayout_password.addWidget(self.label_password)

        self.plainTextEdit_password = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_password.setObjectName(u"plainTextEdit_password")

        self.horizontalLayout_password.addWidget(self.plainTextEdit_password)


        self.verticalLayout.addLayout(self.horizontalLayout_password)

        self.buttonBox_OKorCancel = QDialogButtonBox(self.centralwidget)
        self.buttonBox_OKorCancel.setObjectName(u"buttonBox_OKorCancel")
        self.buttonBox_OKorCancel.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox_OKorCancel)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 352, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_welcome.setText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u4f7f\u7528\uff0c\u8bf7\u5148\u767b\u5f55", None))
        self.label_username.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d\uff1a", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801\uff1a", None))
    # retranslateUi

