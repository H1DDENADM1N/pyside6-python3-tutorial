# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWinLogin.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QCommandLinkButton, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(527, 346)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_Login = QFrame(self.centralwidget)
        self.frame_Login.setObjectName(u"frame_Login")
        self.frame_Login.setFrameShape(QFrame.StyledPanel)
        self.frame_Login.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_Login)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_welcome = QLabel(self.frame_Login)
        self.label_welcome.setObjectName(u"label_welcome")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_welcome.sizePolicy().hasHeightForWidth())
        self.label_welcome.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_welcome.setFont(font)
        self.label_welcome.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_welcome)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_username = QLabel(self.frame_Login)
        self.label_username.setObjectName(u"label_username")
        font1 = QFont()
        font1.setBold(True)
        self.label_username.setFont(font1)
        self.label_username.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_username)

        self.lineEdit_username = QLineEdit(self.frame_Login)
        self.lineEdit_username.setObjectName(u"lineEdit_username")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_username)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_password = QHBoxLayout()
        self.horizontalLayout_password.setObjectName(u"horizontalLayout_password")
        self.label_password = QLabel(self.frame_Login)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setFont(font1)
        self.label_password.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_password.addWidget(self.label_password)

        self.plainTextEdit_password = QPlainTextEdit(self.frame_Login)
        self.plainTextEdit_password.setObjectName(u"plainTextEdit_password")

        self.horizontalLayout_password.addWidget(self.plainTextEdit_password)


        self.verticalLayout.addLayout(self.horizontalLayout_password)

        self.frame = QFrame(self.frame_Login)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButton_clear = QPushButton(self.frame)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.horizontalLayout_3.addWidget(self.pushButton_clear)


        self.verticalLayout.addWidget(self.frame)

        self.frame_agreement = QFrame(self.frame_Login)
        self.frame_agreement.setObjectName(u"frame_agreement")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_agreement.sizePolicy().hasHeightForWidth())
        self.frame_agreement.setSizePolicy(sizePolicy1)
        self.frame_agreement.setFrameShape(QFrame.StyledPanel)
        self.frame_agreement.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_agreement)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.commandLinkButton = QCommandLinkButton(self.frame_agreement)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        sizePolicy1.setHeightForWidth(self.commandLinkButton.sizePolicy().hasHeightForWidth())
        self.commandLinkButton.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setUnderline(True)
        self.commandLinkButton.setFont(font2)

        self.horizontalLayout.addWidget(self.commandLinkButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.checkBox_agreement = QCheckBox(self.frame_agreement)
        self.checkBox_agreement.setObjectName(u"checkBox_agreement")
        self.checkBox_agreement.setFont(font1)

        self.horizontalLayout.addWidget(self.checkBox_agreement)


        self.verticalLayout.addWidget(self.frame_agreement)

        self.line = QFrame(self.frame_Login)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.frame_buttons = QFrame(self.frame_Login)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_buttons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_registration = QPushButton(self.frame_buttons)
        self.pushButton_registration.setObjectName(u"pushButton_registration")

        self.horizontalLayout_2.addWidget(self.pushButton_registration)

        self.pushButton_forgot_password = QPushButton(self.frame_buttons)
        self.pushButton_forgot_password.setObjectName(u"pushButton_forgot_password")

        self.horizontalLayout_2.addWidget(self.pushButton_forgot_password)

        self.line_2 = QFrame(self.frame_buttons)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.pushButton_login = QPushButton(self.frame_buttons)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setEnabled(True)
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        self.pushButton_login.setFont(font3)
        self.pushButton_login.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.pushButton_login)


        self.verticalLayout.addWidget(self.frame_buttons)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.frame_Login)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label_username.setBuddy(self.lineEdit_username)
        self.label_password.setBuddy(self.plainTextEdit_password)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)
        self.pushButton_clear.pressed.connect(self.lineEdit_username.clear)
        self.pushButton_clear.pressed.connect(self.plainTextEdit_password.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_welcome.setText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u4f7f\u7528\uff0c\u8bf7\u5148\u767b\u5f55", None))
        self.label_username.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d(&N)\uff1a", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801(&P)\uff1a", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a(C)", None))
#if QT_CONFIG(shortcut)
        self.pushButton_clear.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u524d\uff0c\u8bf7\u5148\u9605\u8bfb\u5e76\u540c\u610f\u300a\u534f\u8bae\u300b", None))
        self.checkBox_agreement.setText(QCoreApplication.translate("MainWindow", u"\u6211\u5df2\u9605\u8bfb\u5e76\u540c\u610f \u300a\u534f\u8bae\u300b(Y)", None))
#if QT_CONFIG(shortcut)
        self.checkBox_agreement.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Y", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_registration.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c(R)", None))
#if QT_CONFIG(shortcut)
        self.pushButton_registration.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+R", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_forgot_password.setText(QCoreApplication.translate("MainWindow", u"\u5fd8\u8bb0\u5bc6\u7801(F)", None))
#if QT_CONFIG(shortcut)
        self.pushButton_forgot_password.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+F", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_login.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55(Enter)", None))
#if QT_CONFIG(shortcut)
        self.pushButton_login.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

