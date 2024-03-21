# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Sql.ui'
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

class Ui_Sql(object):
    def setupUi(self, Sql):
        if not Sql.objectName():
            Sql.setObjectName(u"Sql")
        Sql.resize(575, 796)
        self.verticalLayout = QVBoxLayout(Sql)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_data_filter = QLabel(Sql)
        self.label_data_filter.setObjectName(u"label_data_filter")

        self.horizontalLayout.addWidget(self.label_data_filter)

        self.lineEdit_data_filter = QLineEdit(Sql)
        self.lineEdit_data_filter.setObjectName(u"lineEdit_data_filter")

        self.horizontalLayout.addWidget(self.lineEdit_data_filter)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_filter_range = QLabel(Sql)
        self.label_filter_range.setObjectName(u"label_filter_range")

        self.horizontalLayout_2.addWidget(self.label_filter_range)

        self.lineEdit_filter_range = QLineEdit(Sql)
        self.lineEdit_filter_range.setObjectName(u"lineEdit_filter_range")

        self.horizontalLayout_2.addWidget(self.lineEdit_filter_range)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label = QLabel(Sql)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.tableView = QTableView(Sql)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(Sql)

        QMetaObject.connectSlotsByName(Sql)
    # setupUi

    def retranslateUi(self, Sql):
        Sql.setWindowTitle(QCoreApplication.translate("Sql", u"\u6570\u636e\u5e93", None))
        self.label_data_filter.setText(QCoreApplication.translate("Sql", u"\u6570\u636e\u8fc7\u6ee4", None))
        self.lineEdit_data_filter.setText(QCoreApplication.translate("Sql", u"/*", None))
        self.label_filter_range.setText(QCoreApplication.translate("Sql", u"\u8fc7\u6ee4\u9002\u7528\u8303\u56f4\uff08\u5217\uff09", None))
        self.lineEdit_filter_range.setText(QCoreApplication.translate("Sql", u"1,2", None))
        self.label.setText(QCoreApplication.translate("Sql", u"\u6570\u636e\u5e93", None))
    # retranslateUi

