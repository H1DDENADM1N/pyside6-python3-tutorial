# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWinFormLayout.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(334, 157)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_remark = QLabel(self.centralwidget)
        self.label_remark.setObjectName(u"label_remark")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_remark)

        self.lineEdit_remark = QLineEdit(self.centralwidget)
        self.lineEdit_remark.setObjectName(u"lineEdit_remark")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_remark)

        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_name)

        self.lineEdit_name = QLineEdit(self.centralwidget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_name)

        self.label_salaries = QLabel(self.centralwidget)
        self.label_salaries.setObjectName(u"label_salaries")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_salaries)

        self.lineEdit_salaries = QLineEdit(self.centralwidget)
        self.lineEdit_salaries.setObjectName(u"lineEdit_salaries")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_salaries)


        self.verticalLayout.addLayout(self.formLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 334, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_remark.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8\uff1a", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d\uff1a", None))
        self.label_salaries.setText(QCoreApplication.translate("MainWindow", u"\u85aa\u8d44\uff1a", None))
    # retranslateUi

