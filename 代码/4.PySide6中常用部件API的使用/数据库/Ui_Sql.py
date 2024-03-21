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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_Sql(object):
    def setupUi(self, Sql):
        if not Sql.objectName():
            Sql.setObjectName(u"Sql")
        Sql.resize(651, 856)
        self.verticalLayout_5 = QVBoxLayout(Sql)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_data_filter = QLabel(Sql)
        self.label_data_filter.setObjectName(u"label_data_filter")

        self.horizontalLayout.addWidget(self.label_data_filter)

        self.lineEdit_data_filter = QLineEdit(Sql)
        self.lineEdit_data_filter.setObjectName(u"lineEdit_data_filter")

        self.horizontalLayout.addWidget(self.lineEdit_data_filter)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_filter_range = QLabel(Sql)
        self.label_filter_range.setObjectName(u"label_filter_range")

        self.horizontalLayout_2.addWidget(self.label_filter_range)

        self.lineEdit_filter_range = QLineEdit(Sql)
        self.lineEdit_filter_range.setObjectName(u"lineEdit_filter_range")

        self.horizontalLayout_2.addWidget(self.lineEdit_filter_range)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(Sql)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.tableView = QTableView(Sql)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_4.addWidget(self.tableView)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(Sql)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_add_index = QLineEdit(self.groupBox)
        self.lineEdit_add_index.setObjectName(u"lineEdit_add_index")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_add_index.sizePolicy().hasHeightForWidth())
        self.lineEdit_add_index.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_add_index)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_add_name = QLineEdit(self.groupBox)
        self.lineEdit_add_name.setObjectName(u"lineEdit_add_name")
        sizePolicy.setHeightForWidth(self.lineEdit_add_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_add_name.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_add_name)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_add_address = QLineEdit(self.groupBox)
        self.lineEdit_add_address.setObjectName(u"lineEdit_add_address")
        sizePolicy.setHeightForWidth(self.lineEdit_add_address.sizePolicy().hasHeightForWidth())
        self.lineEdit_add_address.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_add_address)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_add_email = QLineEdit(self.groupBox)
        self.lineEdit_add_email.setObjectName(u"lineEdit_add_email")
        sizePolicy.setHeightForWidth(self.lineEdit_add_email.sizePolicy().hasHeightForWidth())
        self.lineEdit_add_email.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_add_email)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_add_name_pinyin = QLineEdit(self.groupBox)
        self.lineEdit_add_name_pinyin.setObjectName(u"lineEdit_add_name_pinyin")
        sizePolicy.setHeightForWidth(self.lineEdit_add_name_pinyin.sizePolicy().hasHeightForWidth())
        self.lineEdit_add_name_pinyin.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_add_name_pinyin)


        self.verticalLayout.addLayout(self.formLayout)

        self.pushButton_add = QPushButton(self.groupBox)
        self.pushButton_add.setObjectName(u"pushButton_add")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.pushButton_add)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Sql)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.lineEdit_remove_index = QLineEdit(self.groupBox_2)
        self.lineEdit_remove_index.setObjectName(u"lineEdit_remove_index")
        sizePolicy.setHeightForWidth(self.lineEdit_remove_index.sizePolicy().hasHeightForWidth())
        self.lineEdit_remove_index.setSizePolicy(sizePolicy)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_remove_index)


        self.verticalLayout_2.addLayout(self.formLayout_2)

        self.pushButton_remove = QPushButton(self.groupBox_2)
        self.pushButton_remove.setObjectName(u"pushButton_remove")
        sizePolicy1.setHeightForWidth(self.pushButton_remove.sizePolicy().hasHeightForWidth())
        self.pushButton_remove.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.pushButton_remove)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


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
        self.groupBox.setTitle(QCoreApplication.translate("Sql", u"\u589e", None))
        self.label_2.setText(QCoreApplication.translate("Sql", u"0 \u5e8f\u53f7 index", None))
        self.label_3.setText(QCoreApplication.translate("Sql", u"1 \u59d3\u540d name", None))
        self.label_4.setText(QCoreApplication.translate("Sql", u"2 \u5730\u5740 address", None))
        self.label_5.setText(QCoreApplication.translate("Sql", u"3 \u90ae\u7bb1 email", None))
        self.label_6.setText(QCoreApplication.translate("Sql", u"4 \u59d3\u540d\u62fc\u97f3", None))
        self.pushButton_add.setText(QCoreApplication.translate("Sql", u"\u65b0\u589e\u6570\u636e", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Sql", u"\u5220", None))
        self.label_7.setText(QCoreApplication.translate("Sql", u"0 \u5e8f\u53f7 index", None))
        self.pushButton_remove.setText(QCoreApplication.translate("Sql", u"\u5220\u9664\u6570\u636e", None))
    # retranslateUi

