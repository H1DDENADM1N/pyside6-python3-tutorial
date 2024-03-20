# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TableView.ui'
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

class Ui_TableView(object):
    def setupUi(self, TableView):
        if not TableView.objectName():
            TableView.setObjectName(u"TableView")
        TableView.resize(523, 787)
        self.verticalLayout = QVBoxLayout(TableView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_data_filter = QLabel(TableView)
        self.label_data_filter.setObjectName(u"label_data_filter")

        self.horizontalLayout.addWidget(self.label_data_filter)

        self.lineEdit_data_filter = QLineEdit(TableView)
        self.lineEdit_data_filter.setObjectName(u"lineEdit_data_filter")

        self.horizontalLayout.addWidget(self.lineEdit_data_filter)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label = QLabel(TableView)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.tableView = QTableView(TableView)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(TableView)

        QMetaObject.connectSlotsByName(TableView)
    # setupUi

    def retranslateUi(self, TableView):
        TableView.setWindowTitle(QCoreApplication.translate("TableView", u"\u8868\u683c\u89c6\u56fe", None))
        self.label_data_filter.setText(QCoreApplication.translate("TableView", u"\u6570\u636e\u8fc7\u6ee4", None))
        self.lineEdit_data_filter.setText(QCoreApplication.translate("TableView", u"/*", None))
        self.label.setText(QCoreApplication.translate("TableView", u"\u8868\u683c\u89c6\u56fe", None))
    # retranslateUi

