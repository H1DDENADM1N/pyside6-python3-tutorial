# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Numpad.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import Icon_rc

class Ui_NumPad(object):
    def setupUi(self, NumPad):
        if not NumPad.objectName():
            NumPad.setObjectName(u"NumPad")
        NumPad.resize(257, 300)
        icon = QIcon()
        icon.addFile(u":/Icon/assets/appicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        NumPad.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(NumPad)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.custom_title_bar = QHBoxLayout()
        self.custom_title_bar.setObjectName(u"custom_title_bar")
        self.icon_label = QLabel(NumPad)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setStyleSheet(u"")
        self.icon_label.setPixmap(QPixmap(u":/Icon/assets/appicon.ico"))

        self.custom_title_bar.addWidget(self.icon_label)

        self.customtitle = QLabel(NumPad)
        self.customtitle.setObjectName(u"customtitle")

        self.custom_title_bar.addWidget(self.customtitle)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.custom_title_bar.addItem(self.horizontalSpacer)

        self.minimize_button = QPushButton(NumPad)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.minimize_button.setFont(font)

        self.custom_title_bar.addWidget(self.minimize_button)

        self.maximize_botton = QPushButton(NumPad)
        self.maximize_botton.setObjectName(u"maximize_botton")
        self.maximize_botton.setMaximumSize(QSize(25, 25))
        self.maximize_botton.setFont(font)

        self.custom_title_bar.addWidget(self.maximize_botton)

        self.close_button = QPushButton(NumPad)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMaximumSize(QSize(25, 25))
        self.close_button.setFont(font)

        self.custom_title_bar.addWidget(self.close_button)


        self.verticalLayout.addLayout(self.custom_title_bar)

        self.number_pad = QGridLayout()
        self.number_pad.setObjectName(u"number_pad")
        self.label_number_keyboard = QLabel(NumPad)
        self.label_number_keyboard.setObjectName(u"label_number_keyboard")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_number_keyboard.sizePolicy().hasHeightForWidth())
        self.label_number_keyboard.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(10)
        self.label_number_keyboard.setFont(font1)

        self.number_pad.addWidget(self.label_number_keyboard, 0, 0, 1, 1)

        self.pushButton_4 = QPushButton(NumPad)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setMinimumSize(QSize(0, 0))
        self.pushButton_4.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        self.pushButton_4.setFont(font2)

        self.number_pad.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_0 = QPushButton(NumPad)
        self.pushButton_0.setObjectName(u"pushButton_0")
        sizePolicy1.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy1)
        self.pushButton_0.setMinimumSize(QSize(0, 0))
        self.pushButton_0.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_0.setFont(font2)

        self.number_pad.addWidget(self.pushButton_0, 4, 0, 1, 2)

        self.pushButton_2 = QPushButton(NumPad)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(0, 0))
        self.pushButton_2.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_2.setFont(font2)

        self.number_pad.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.pushButton_3 = QPushButton(NumPad)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setMinimumSize(QSize(0, 0))
        self.pushButton_3.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_3.setFont(font2)

        self.number_pad.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.pushButton_7 = QPushButton(NumPad)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy1.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy1)
        self.pushButton_7.setMinimumSize(QSize(0, 0))
        self.pushButton_7.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_7.setFont(font2)

        self.number_pad.addWidget(self.pushButton_7, 1, 0, 1, 1)

        self.pushButton_1 = QPushButton(NumPad)
        self.pushButton_1.setObjectName(u"pushButton_1")
        sizePolicy1.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy1)
        self.pushButton_1.setMinimumSize(QSize(0, 0))
        self.pushButton_1.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_1.setFont(font2)

        self.number_pad.addWidget(self.pushButton_1, 3, 0, 1, 1)

        self.pushButton_Backspace = QPushButton(NumPad)
        self.pushButton_Backspace.setObjectName(u"pushButton_Backspace")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.pushButton_Backspace.sizePolicy().hasHeightForWidth())
        self.pushButton_Backspace.setSizePolicy(sizePolicy2)
        self.pushButton_Backspace.setMinimumSize(QSize(0, 0))
        self.pushButton_Backspace.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_Backspace.setFont(font1)

        self.number_pad.addWidget(self.pushButton_Backspace, 0, 1, 1, 2)

        self.pushButton_6 = QPushButton(NumPad)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)
        self.pushButton_6.setMinimumSize(QSize(0, 0))
        self.pushButton_6.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_6.setFont(font2)

        self.number_pad.addWidget(self.pushButton_6, 2, 1, 1, 1)

        self.pushButton_9 = QPushButton(NumPad)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy1.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy1)
        self.pushButton_9.setMinimumSize(QSize(0, 0))
        self.pushButton_9.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_9.setFont(font2)

        self.number_pad.addWidget(self.pushButton_9, 1, 1, 1, 1)

        self.pushButton_Enter = QPushButton(NumPad)
        self.pushButton_Enter.setObjectName(u"pushButton_Enter")
        sizePolicy1.setHeightForWidth(self.pushButton_Enter.sizePolicy().hasHeightForWidth())
        self.pushButton_Enter.setSizePolicy(sizePolicy1)
        self.pushButton_Enter.setMinimumSize(QSize(0, 0))
        self.pushButton_Enter.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_Enter.setFont(font1)

        self.number_pad.addWidget(self.pushButton_Enter, 4, 2, 1, 1)

        self.pushButton_8 = QPushButton(NumPad)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy1.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy1)
        self.pushButton_8.setMinimumSize(QSize(0, 0))
        self.pushButton_8.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_8.setFont(font2)

        self.number_pad.addWidget(self.pushButton_8, 1, 2, 1, 1)

        self.pushButton_5 = QPushButton(NumPad)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setMinimumSize(QSize(0, 0))
        self.pushButton_5.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_5.setFont(font2)

        self.number_pad.addWidget(self.pushButton_5, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.number_pad)


        self.retranslateUi(NumPad)
        self.minimize_button.clicked.connect(NumPad.showMinimized)
        self.close_button.clicked.connect(NumPad.close)

        QMetaObject.connectSlotsByName(NumPad)
    # setupUi

    def retranslateUi(self, NumPad):
        NumPad.setWindowTitle(QCoreApplication.translate("NumPad", u"\u6570\u5b57\u952e\u76d8", None))
        self.icon_label.setText("")
        self.customtitle.setText(QCoreApplication.translate("NumPad", u"\u6570\u5b57\u952e\u76d8", None))
        self.minimize_button.setText(QCoreApplication.translate("NumPad", u"-", None))
#if QT_CONFIG(shortcut)
        self.minimize_button.setShortcut(QCoreApplication.translate("NumPad", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.maximize_botton.setText(QCoreApplication.translate("NumPad", u"[]", None))
        self.close_button.setText(QCoreApplication.translate("NumPad", u"X", None))
        self.label_number_keyboard.setText(QCoreApplication.translate("NumPad", u"\u6570\u5b57\u952e\u76d8", None))
        self.pushButton_4.setText(QCoreApplication.translate("NumPad", u"4", None))
#if QT_CONFIG(shortcut)
        self.pushButton_4.setShortcut(QCoreApplication.translate("NumPad", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_0.setText(QCoreApplication.translate("NumPad", u"0", None))
#if QT_CONFIG(shortcut)
        self.pushButton_0.setShortcut(QCoreApplication.translate("NumPad", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_2.setText(QCoreApplication.translate("NumPad", u"2", None))
#if QT_CONFIG(shortcut)
        self.pushButton_2.setShortcut(QCoreApplication.translate("NumPad", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_3.setText(QCoreApplication.translate("NumPad", u"3", None))
#if QT_CONFIG(shortcut)
        self.pushButton_3.setShortcut(QCoreApplication.translate("NumPad", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_7.setText(QCoreApplication.translate("NumPad", u"7", None))
#if QT_CONFIG(shortcut)
        self.pushButton_7.setShortcut(QCoreApplication.translate("NumPad", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_1.setText(QCoreApplication.translate("NumPad", u"1", None))
#if QT_CONFIG(shortcut)
        self.pushButton_1.setShortcut(QCoreApplication.translate("NumPad", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_Backspace.setText(QCoreApplication.translate("NumPad", u"Backspace", None))
#if QT_CONFIG(shortcut)
        self.pushButton_Backspace.setShortcut(QCoreApplication.translate("NumPad", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_6.setText(QCoreApplication.translate("NumPad", u"5", None))
#if QT_CONFIG(shortcut)
        self.pushButton_6.setShortcut(QCoreApplication.translate("NumPad", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_9.setText(QCoreApplication.translate("NumPad", u"8", None))
#if QT_CONFIG(shortcut)
        self.pushButton_9.setShortcut(QCoreApplication.translate("NumPad", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_Enter.setText(QCoreApplication.translate("NumPad", u"Enter", None))
#if QT_CONFIG(shortcut)
        self.pushButton_Enter.setShortcut(QCoreApplication.translate("NumPad", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_8.setText(QCoreApplication.translate("NumPad", u"9", None))
#if QT_CONFIG(shortcut)
        self.pushButton_8.setShortcut(QCoreApplication.translate("NumPad", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_5.setText(QCoreApplication.translate("NumPad", u"6", None))
#if QT_CONFIG(shortcut)
        self.pushButton_5.setShortcut(QCoreApplication.translate("NumPad", u"6", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

