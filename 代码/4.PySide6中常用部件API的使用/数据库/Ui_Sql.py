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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_Sql(object):
    def setupUi(self, Sql):
        if not Sql.objectName():
            Sql.setObjectName(u"Sql")
        Sql.resize(575, 796)
        self.verticalLayout = QVBoxLayout(Sql)
        self.verticalLayout.setObjectName(u"verticalLayout")
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
        self.label.setText(QCoreApplication.translate("Sql", u"\u6570\u636e\u5e93", None))
    # retranslateUi

