# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CustomTitleBarAndIcon_In_QtDesigner.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import Icon_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(371, 87)
        Form.setSizeIncrement(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon_label = QLabel(Form)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setStyleSheet(u"")
        self.icon_label.setPixmap(QPixmap(u":/Icon/assets/appicon.ico"))

        self.horizontalLayout.addWidget(self.icon_label)

        self.customtitle = QLabel(Form)
        self.customtitle.setObjectName(u"customtitle")

        self.horizontalLayout.addWidget(self.customtitle)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.minimize_button = QPushButton(Form)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setMaximumSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.minimize_button)

        self.maximize_botton = QPushButton(Form)
        self.maximize_botton.setObjectName(u"maximize_botton")
        self.maximize_botton.setMaximumSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.maximize_botton)

        self.close_button = QPushButton(Form)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMaximumSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.close_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)
        self.minimize_button.clicked.connect(Form.showMinimized)
        self.close_button.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Custom Title Bar Example", None))
        self.icon_label.setText("")
        self.customtitle.setText(QCoreApplication.translate("Form", u"Custom Title", None))
        self.minimize_button.setText(QCoreApplication.translate("Form", u"-", None))
        self.maximize_botton.setText(QCoreApplication.translate("Form", u"[]", None))
        self.close_button.setText(QCoreApplication.translate("Form", u"X", None))
    # retranslateUi

