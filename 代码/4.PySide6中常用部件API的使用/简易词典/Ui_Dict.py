# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dict.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

class Ui_Dict(object):
    def setupUi(self, Dict):
        if not Dict.objectName():
            Dict.setObjectName(u"Dict")
        Dict.resize(1883, 793)
        self.verticalLayout = QVBoxLayout(Dict)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_en2cn = QLabel(Dict)
        self.label_en2cn.setObjectName(u"label_en2cn")

        self.horizontalLayout.addWidget(self.label_en2cn)

        self.lineEdit_en2cn = QLineEdit(Dict)
        self.lineEdit_en2cn.setObjectName(u"lineEdit_en2cn")

        self.horizontalLayout.addWidget(self.lineEdit_en2cn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_cn2en = QLabel(Dict)
        self.label_cn2en.setObjectName(u"label_cn2en")

        self.horizontalLayout_2.addWidget(self.label_cn2en)

        self.lineEdit_cn2en = QLineEdit(Dict)
        self.lineEdit_cn2en.setObjectName(u"lineEdit_cn2en")

        self.horizontalLayout_2.addWidget(self.lineEdit_cn2en)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(Dict)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.tableView = QTableView(Dict)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_4.addWidget(self.tableView)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.retranslateUi(Dict)

        QMetaObject.connectSlotsByName(Dict)
    # setupUi

    def retranslateUi(self, Dict):
        Dict.setWindowTitle(QCoreApplication.translate("Dict", u"\u7b80\u6613\u8bcd\u5178", None))
        self.label_en2cn.setText(QCoreApplication.translate("Dict", u"\u82f1->\u4e2d", None))
        self.lineEdit_en2cn.setText("")
        self.lineEdit_en2cn.setPlaceholderText(QCoreApplication.translate("Dict", u"hello", None))
        self.label_cn2en.setText(QCoreApplication.translate("Dict", u"\u4e2d->\u82f1", None))
        self.lineEdit_cn2en.setText("")
        self.lineEdit_cn2en.setPlaceholderText(QCoreApplication.translate("Dict", u"\u4f60\u597d", None))
        self.label.setText(QCoreApplication.translate("Dict", u"\u67e5\u8bcd\u7ed3\u679c", None))
    # retranslateUi

