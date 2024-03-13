# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Calc.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import Icon_rc

class Ui_Calc(object):
    def setupUi(self, Calc):
        if not Calc.objectName():
            Calc.setObjectName(u"Calc")
        Calc.resize(329, 433)
        icon = QIcon()
        icon.addFile(u":/Icon/assets/appicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Calc.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Calc)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.custom_title_bar = QHBoxLayout()
        self.custom_title_bar.setObjectName(u"custom_title_bar")
        self.icon_label = QLabel(Calc)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setStyleSheet(u"")
        self.icon_label.setPixmap(QPixmap(u":/Icon/assets/appicon.ico"))

        self.custom_title_bar.addWidget(self.icon_label)

        self.customtitle = QLabel(Calc)
        self.customtitle.setObjectName(u"customtitle")

        self.custom_title_bar.addWidget(self.customtitle)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.custom_title_bar.addItem(self.horizontalSpacer)

        self.minimize_button = QPushButton(Calc)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.minimize_button.setFont(font)

        self.custom_title_bar.addWidget(self.minimize_button)

        self.maximize_botton = QPushButton(Calc)
        self.maximize_botton.setObjectName(u"maximize_botton")
        self.maximize_botton.setMaximumSize(QSize(25, 25))
        self.maximize_botton.setFont(font)

        self.custom_title_bar.addWidget(self.maximize_botton)

        self.close_button = QPushButton(Calc)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMaximumSize(QSize(25, 25))
        self.close_button.setFont(font)

        self.custom_title_bar.addWidget(self.close_button)


        self.verticalLayout.addLayout(self.custom_title_bar)

        self.number_pad = QGridLayout()
        self.number_pad.setObjectName(u"number_pad")
        self.pushButton_8 = QPushButton(Calc)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QSize(0, 0))
        self.pushButton_8.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        self.pushButton_8.setFont(font1)

        self.number_pad.addWidget(self.pushButton_8, 4, 3, 1, 1)

        self.pushButton_Backspace = QPushButton(Calc)
        self.pushButton_Backspace.setObjectName(u"pushButton_Backspace")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.pushButton_Backspace.sizePolicy().hasHeightForWidth())
        self.pushButton_Backspace.setSizePolicy(sizePolicy1)
        self.pushButton_Backspace.setMinimumSize(QSize(0, 0))
        self.pushButton_Backspace.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        self.pushButton_Backspace.setFont(font2)

        self.number_pad.addWidget(self.pushButton_Backspace, 3, 3, 1, 2)

        self.pushButton_Dot = QPushButton(Calc)
        self.pushButton_Dot.setObjectName(u"pushButton_Dot")
        sizePolicy1.setHeightForWidth(self.pushButton_Dot.sizePolicy().hasHeightForWidth())
        self.pushButton_Dot.setSizePolicy(sizePolicy1)
        self.pushButton_Dot.setMinimumSize(QSize(0, 0))
        self.pushButton_Dot.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_Dot.setFont(font1)

        self.number_pad.addWidget(self.pushButton_Dot, 7, 0, 1, 1)

        self.pushButton_0 = QPushButton(Calc)
        self.pushButton_0.setObjectName(u"pushButton_0")
        sizePolicy.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy)
        self.pushButton_0.setMinimumSize(QSize(0, 0))
        self.pushButton_0.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_0.setFont(font1)

        self.number_pad.addWidget(self.pushButton_0, 7, 2, 1, 2)

        self.pushButton_9 = QPushButton(Calc)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QSize(0, 0))
        self.pushButton_9.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_9.setFont(font1)

        self.number_pad.addWidget(self.pushButton_9, 4, 4, 1, 1)

        self.pushButton_5 = QPushButton(Calc)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QSize(0, 0))
        self.pushButton_5.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_5.setFont(font1)

        self.number_pad.addWidget(self.pushButton_5, 5, 3, 1, 1)

        self.pushButton_Div = QPushButton(Calc)
        self.pushButton_Div.setObjectName(u"pushButton_Div")
        sizePolicy1.setHeightForWidth(self.pushButton_Div.sizePolicy().hasHeightForWidth())
        self.pushButton_Div.setSizePolicy(sizePolicy1)
        self.pushButton_Div.setMinimumSize(QSize(0, 0))
        self.pushButton_Div.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_Div.setFont(font1)

        self.number_pad.addWidget(self.pushButton_Div, 3, 0, 1, 1)

        self.line = QFrame(Calc)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.number_pad.addWidget(self.line, 2, 0, 1, 5)

        self.pushButton_3 = QPushButton(Calc)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QSize(0, 0))
        self.pushButton_3.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_3.setFont(font1)

        self.number_pad.addWidget(self.pushButton_3, 6, 4, 1, 1)

        self.pushButton_7 = QPushButton(Calc)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QSize(0, 0))
        self.pushButton_7.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_7.setFont(font1)

        self.number_pad.addWidget(self.pushButton_7, 4, 2, 1, 1)

        self.label_number_keyboard = QLabel(Calc)
        self.label_number_keyboard.setObjectName(u"label_number_keyboard")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_number_keyboard.sizePolicy().hasHeightForWidth())
        self.label_number_keyboard.setSizePolicy(sizePolicy2)
        self.label_number_keyboard.setFont(font2)

        self.number_pad.addWidget(self.label_number_keyboard, 3, 2, 1, 1)

        self.pushButton_6 = QPushButton(Calc)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QSize(0, 0))
        self.pushButton_6.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_6.setFont(font1)

        self.number_pad.addWidget(self.pushButton_6, 5, 4, 1, 1)

        self.pushButton_Enter = QPushButton(Calc)
        self.pushButton_Enter.setObjectName(u"pushButton_Enter")
        sizePolicy.setHeightForWidth(self.pushButton_Enter.sizePolicy().hasHeightForWidth())
        self.pushButton_Enter.setSizePolicy(sizePolicy)
        self.pushButton_Enter.setMinimumSize(QSize(0, 0))
        self.pushButton_Enter.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_Enter.setFont(font1)

        self.number_pad.addWidget(self.pushButton_Enter, 7, 4, 1, 1)

        self.line_2 = QFrame(Calc)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.number_pad.addWidget(self.line_2, 3, 1, 5, 1)

        self.pushButton_Add = QPushButton(Calc)
        self.pushButton_Add.setObjectName(u"pushButton_Add")
        sizePolicy1.setHeightForWidth(self.pushButton_Add.sizePolicy().hasHeightForWidth())
        self.pushButton_Add.setSizePolicy(sizePolicy1)
        self.pushButton_Add.setMinimumSize(QSize(0, 0))
        self.pushButton_Add.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_Add.setFont(font1)

        self.number_pad.addWidget(self.pushButton_Add, 6, 0, 1, 1)

        self.pushButton_4 = QPushButton(Calc)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QSize(0, 0))
        self.pushButton_4.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_4.setFont(font1)

        self.number_pad.addWidget(self.pushButton_4, 5, 2, 1, 1)

        self.pushButton_2 = QPushButton(Calc)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(0, 0))
        self.pushButton_2.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_2.setFont(font1)

        self.number_pad.addWidget(self.pushButton_2, 6, 3, 1, 1)

        self.pushButton_Sub = QPushButton(Calc)
        self.pushButton_Sub.setObjectName(u"pushButton_Sub")
        sizePolicy1.setHeightForWidth(self.pushButton_Sub.sizePolicy().hasHeightForWidth())
        self.pushButton_Sub.setSizePolicy(sizePolicy1)
        self.pushButton_Sub.setMinimumSize(QSize(0, 0))
        self.pushButton_Sub.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_Sub.setFont(font1)

        self.number_pad.addWidget(self.pushButton_Sub, 5, 0, 1, 1)

        self.pushButton_1 = QPushButton(Calc)
        self.pushButton_1.setObjectName(u"pushButton_1")
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setMinimumSize(QSize(0, 0))
        self.pushButton_1.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_1.setFont(font1)

        self.number_pad.addWidget(self.pushButton_1, 6, 2, 1, 1)

        self.pushButton_Muti = QPushButton(Calc)
        self.pushButton_Muti.setObjectName(u"pushButton_Muti")
        sizePolicy1.setHeightForWidth(self.pushButton_Muti.sizePolicy().hasHeightForWidth())
        self.pushButton_Muti.setSizePolicy(sizePolicy1)
        self.pushButton_Muti.setMinimumSize(QSize(0, 0))
        self.pushButton_Muti.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_Muti.setFont(font1)

        self.number_pad.addWidget(self.pushButton_Muti, 4, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(Calc)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy3)
        self.plainTextEdit.setMinimumSize(QSize(0, 0))
        self.plainTextEdit.setMaximumSize(QSize(16777215, 53))
        font3 = QFont()
        font3.setPointSize(25)
        self.plainTextEdit.setFont(font3)

        self.number_pad.addWidget(self.plainTextEdit, 0, 0, 1, 5)

        self.pushButton_LeftBracket = QPushButton(Calc)
        self.pushButton_LeftBracket.setObjectName(u"pushButton_LeftBracket")
        sizePolicy1.setHeightForWidth(self.pushButton_LeftBracket.sizePolicy().hasHeightForWidth())
        self.pushButton_LeftBracket.setSizePolicy(sizePolicy1)
        self.pushButton_LeftBracket.setMinimumSize(QSize(0, 0))
        self.pushButton_LeftBracket.setMaximumSize(QSize(16777215, 200))
        self.pushButton_LeftBracket.setFont(font1)

        self.number_pad.addWidget(self.pushButton_LeftBracket, 1, 0, 1, 2)

        self.pushButton_RightBracket = QPushButton(Calc)
        self.pushButton_RightBracket.setObjectName(u"pushButton_RightBracket")
        sizePolicy1.setHeightForWidth(self.pushButton_RightBracket.sizePolicy().hasHeightForWidth())
        self.pushButton_RightBracket.setSizePolicy(sizePolicy1)
        self.pushButton_RightBracket.setMinimumSize(QSize(0, 0))
        self.pushButton_RightBracket.setMaximumSize(QSize(16777215, 200))
        self.pushButton_RightBracket.setFont(font1)

        self.number_pad.addWidget(self.pushButton_RightBracket, 1, 2, 1, 1)

        self.pushButton_Clear = QPushButton(Calc)
        self.pushButton_Clear.setObjectName(u"pushButton_Clear")
        sizePolicy1.setHeightForWidth(self.pushButton_Clear.sizePolicy().hasHeightForWidth())
        self.pushButton_Clear.setSizePolicy(sizePolicy1)
        self.pushButton_Clear.setMinimumSize(QSize(0, 0))
        self.pushButton_Clear.setMaximumSize(QSize(16777215, 200))
        self.pushButton_Clear.setFont(font1)

        self.number_pad.addWidget(self.pushButton_Clear, 1, 3, 1, 2)


        self.verticalLayout.addLayout(self.number_pad)


        self.retranslateUi(Calc)
        self.minimize_button.clicked.connect(Calc.showMinimized)
        self.close_button.clicked.connect(Calc.close)

        QMetaObject.connectSlotsByName(Calc)
    # setupUi

    def retranslateUi(self, Calc):
        Calc.setWindowTitle(QCoreApplication.translate("Calc", u"\u8ba1\u7b97\u5668", None))
        self.icon_label.setText("")
        self.customtitle.setText(QCoreApplication.translate("Calc", u"\u8ba1\u7b97\u5668", None))
        self.minimize_button.setText(QCoreApplication.translate("Calc", u"-", None))
#if QT_CONFIG(shortcut)
        self.minimize_button.setShortcut(QCoreApplication.translate("Calc", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.maximize_botton.setText(QCoreApplication.translate("Calc", u"[]", None))
        self.close_button.setText(QCoreApplication.translate("Calc", u"X", None))
        self.pushButton_8.setText(QCoreApplication.translate("Calc", u"8", None))
#if QT_CONFIG(shortcut)
        self.pushButton_8.setShortcut(QCoreApplication.translate("Calc", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_Backspace.setText(QCoreApplication.translate("Calc", u"Backspace", None))
#if QT_CONFIG(shortcut)
        self.pushButton_Backspace.setShortcut(QCoreApplication.translate("Calc", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_Dot.setText(QCoreApplication.translate("Calc", u".", None))
#if QT_CONFIG(shortcut)
        self.pushButton_Dot.setShortcut(QCoreApplication.translate("Calc", u".", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_0.setText(QCoreApplication.translate("Calc", u"0", None))
#if QT_CONFIG(shortcut)
        self.pushButton_0.setShortcut(QCoreApplication.translate("Calc", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_9.setText(QCoreApplication.translate("Calc", u"9", None))
#if QT_CONFIG(shortcut)
        self.pushButton_9.setShortcut(QCoreApplication.translate("Calc", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_5.setText(QCoreApplication.translate("Calc", u"5", None))
#if QT_CONFIG(shortcut)
        self.pushButton_5.setShortcut(QCoreApplication.translate("Calc", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_Div.setText(QCoreApplication.translate("Calc", u"/", None))
#if QT_CONFIG(shortcut)
        self.pushButton_Div.setShortcut(QCoreApplication.translate("Calc", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_3.setText(QCoreApplication.translate("Calc", u"3", None))
#if QT_CONFIG(shortcut)
        self.pushButton_3.setShortcut(QCoreApplication.translate("Calc", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_7.setText(QCoreApplication.translate("Calc", u"7", None))
#if QT_CONFIG(shortcut)
        self.pushButton_7.setShortcut(QCoreApplication.translate("Calc", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.label_number_keyboard.setText(QCoreApplication.translate("Calc", u"History", None))
        self.pushButton_6.setText(QCoreApplication.translate("Calc", u"6", None))
#if QT_CONFIG(shortcut)
        self.pushButton_6.setShortcut(QCoreApplication.translate("Calc", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_Enter.setText(QCoreApplication.translate("Calc", u"=", None))
#if QT_CONFIG(shortcut)
        self.pushButton_Enter.setShortcut(QCoreApplication.translate("Calc", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_Add.setText(QCoreApplication.translate("Calc", u"+", None))
#if QT_CONFIG(shortcut)
        self.pushButton_Add.setShortcut(QCoreApplication.translate("Calc", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_4.setText(QCoreApplication.translate("Calc", u"4", None))
#if QT_CONFIG(shortcut)
        self.pushButton_4.setShortcut(QCoreApplication.translate("Calc", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_2.setText(QCoreApplication.translate("Calc", u"2", None))
#if QT_CONFIG(shortcut)
        self.pushButton_2.setShortcut(QCoreApplication.translate("Calc", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_Sub.setText(QCoreApplication.translate("Calc", u"-", None))
#if QT_CONFIG(shortcut)
        self.pushButton_Sub.setShortcut(QCoreApplication.translate("Calc", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_1.setText(QCoreApplication.translate("Calc", u"1", None))
#if QT_CONFIG(shortcut)
        self.pushButton_1.setShortcut(QCoreApplication.translate("Calc", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_Muti.setText(QCoreApplication.translate("Calc", u"*", None))
#if QT_CONFIG(shortcut)
        self.pushButton_Muti.setShortcut(QCoreApplication.translate("Calc", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Calc", u"Result", None))
        self.pushButton_LeftBracket.setText(QCoreApplication.translate("Calc", u"\uff08", None))
#if QT_CONFIG(shortcut)
        self.pushButton_LeftBracket.setShortcut(QCoreApplication.translate("Calc", u"(", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_RightBracket.setText(QCoreApplication.translate("Calc", u"\uff09", None))
#if QT_CONFIG(shortcut)
        self.pushButton_RightBracket.setShortcut(QCoreApplication.translate("Calc", u")", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_Clear.setText(QCoreApplication.translate("Calc", u"C", None))
#if QT_CONFIG(shortcut)
        self.pushButton_Clear.setShortcut(QCoreApplication.translate("Calc", u"C", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

