# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog_Login.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QCommandLinkButton, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.resize(483, 224)
        self.verticalLayout_10 = QVBoxLayout(Dialog)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_Login = QVBoxLayout()
        self.verticalLayout_Login.setSpacing(0)
        self.verticalLayout_Login.setObjectName(u"verticalLayout_Login")
        self.verticalLayout_Login.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_Login = QWidget()
        self.tab_Login.setObjectName(u"tab_Login")
        self.verticalLayout_3 = QVBoxLayout(self.tab_Login)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_Login = QFrame(self.tab_Login)
        self.frame_Login.setObjectName(u"frame_Login")
        self.frame_Login.setFrameShape(QFrame.StyledPanel)
        self.frame_Login.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_Login)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_welcome = QLabel(self.frame_Login)
        self.label_welcome.setObjectName(u"label_welcome")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_welcome.sizePolicy().hasHeightForWidth())
        self.label_welcome.setSizePolicy(sizePolicy)
        self.label_welcome.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_welcome.setFont(font)
        self.label_welcome.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label_welcome)

        self.username_and_password = QFrame(self.frame_Login)
        self.username_and_password.setObjectName(u"username_and_password")
        self.username_and_password.setMaximumSize(QSize(16777215, 200))
        self.gridLayout_3 = QGridLayout(self.username_and_password)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_username = QLabel(self.username_and_password)
        self.label_username.setObjectName(u"label_username")
        font1 = QFont()
        font1.setBold(True)
        self.label_username.setFont(font1)
        self.label_username.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_username, 0, 0, 1, 1)

        self.lineEdit_username = QLineEdit(self.username_and_password)
        self.lineEdit_username.setObjectName(u"lineEdit_username")

        self.gridLayout_3.addWidget(self.lineEdit_username, 0, 1, 1, 1)

        self.label_password = QLabel(self.username_and_password)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setFont(font1)
        self.label_password.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_password, 1, 0, 1, 1)

        self.lineEdit_password = QLineEdit(self.username_and_password)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lineEdit_password, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.username_and_password)

        self.frame = QFrame(self.frame_Login)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButton_clear_username_and_password = QPushButton(self.frame)
        self.pushButton_clear_username_and_password.setObjectName(u"pushButton_clear_username_and_password")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.pushButton_clear_username_and_password.sizePolicy().hasHeightForWidth())
        self.pushButton_clear_username_and_password.setSizePolicy(sizePolicy2)
        self.pushButton_clear_username_and_password.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_3.addWidget(self.pushButton_clear_username_and_password)


        self.verticalLayout.addWidget(self.frame)

        self.frame_agreement = QFrame(self.frame_Login)
        self.frame_agreement.setObjectName(u"frame_agreement")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_agreement.sizePolicy().hasHeightForWidth())
        self.frame_agreement.setSizePolicy(sizePolicy3)
        self.frame_agreement.setMaximumSize(QSize(16777215, 50))
        self.frame_agreement.setFrameShape(QFrame.StyledPanel)
        self.frame_agreement.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_agreement)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.commandLinkButton_goto_read_agreement = QCommandLinkButton(self.frame_agreement)
        self.commandLinkButton_goto_read_agreement.setObjectName(u"commandLinkButton_goto_read_agreement")
        sizePolicy3.setHeightForWidth(self.commandLinkButton_goto_read_agreement.sizePolicy().hasHeightForWidth())
        self.commandLinkButton_goto_read_agreement.setSizePolicy(sizePolicy3)
        self.commandLinkButton_goto_read_agreement.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setUnderline(True)
        self.commandLinkButton_goto_read_agreement.setFont(font2)
        self.commandLinkButton_goto_read_agreement.setLayoutDirection(Qt.LeftToRight)
        self.commandLinkButton_goto_read_agreement.setIconSize(QSize(16, 20))

        self.horizontalLayout.addWidget(self.commandLinkButton_goto_read_agreement)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.checkBox_agree_agreement = QCheckBox(self.frame_agreement)
        self.checkBox_agree_agreement.setObjectName(u"checkBox_agree_agreement")
        self.checkBox_agree_agreement.setFont(font1)

        self.horizontalLayout.addWidget(self.checkBox_agree_agreement)


        self.verticalLayout.addWidget(self.frame_agreement)

        self.line = QFrame(self.frame_Login)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.frame_buttons = QFrame(self.frame_Login)
        self.frame_buttons.setObjectName(u"frame_buttons")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(2)
        sizePolicy4.setHeightForWidth(self.frame_buttons.sizePolicy().hasHeightForWidth())
        self.frame_buttons.setSizePolicy(sizePolicy4)
        self.frame_buttons.setMaximumSize(QSize(16777215, 100))
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_buttons)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_goto_registration = QPushButton(self.frame_buttons)
        self.pushButton_goto_registration.setObjectName(u"pushButton_goto_registration")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_goto_registration.sizePolicy().hasHeightForWidth())
        self.pushButton_goto_registration.setSizePolicy(sizePolicy5)
        self.pushButton_goto_registration.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton_goto_registration)

        self.pushButton_goto_forgot_password = QPushButton(self.frame_buttons)
        self.pushButton_goto_forgot_password.setObjectName(u"pushButton_goto_forgot_password")
        sizePolicy5.setHeightForWidth(self.pushButton_goto_forgot_password.sizePolicy().hasHeightForWidth())
        self.pushButton_goto_forgot_password.setSizePolicy(sizePolicy5)
        self.pushButton_goto_forgot_password.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton_goto_forgot_password)

        self.line_2 = QFrame(self.frame_buttons)
        self.line_2.setObjectName(u"line_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy6)
        self.line_2.setMaximumSize(QSize(50, 16777215))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.pushButton_login = QPushButton(self.frame_buttons)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setEnabled(True)
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(2)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pushButton_login.sizePolicy().hasHeightForWidth())
        self.pushButton_login.setSizePolicy(sizePolicy7)
        self.pushButton_login.setMinimumSize(QSize(0, 50))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        self.pushButton_login.setFont(font3)
        self.pushButton_login.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.pushButton_login)


        self.verticalLayout.addWidget(self.frame_buttons)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.frame_Login)

        self.tabWidget.addTab(self.tab_Login, "")
        self.tab_registration = QWidget()
        self.tab_registration.setObjectName(u"tab_registration")
        self.verticalLayout_7 = QVBoxLayout(self.tab_registration)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_registration = QFrame(self.tab_registration)
        self.frame_registration.setObjectName(u"frame_registration")
        self.frame_registration.setFrameShape(QFrame.StyledPanel)
        self.frame_registration.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_registration)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_username_in_registration = QLabel(self.frame_registration)
        self.label_username_in_registration.setObjectName(u"label_username_in_registration")

        self.gridLayout.addWidget(self.label_username_in_registration, 1, 0, 1, 1)

        self.label_repeat_password_in_registration = QLabel(self.frame_registration)
        self.label_repeat_password_in_registration.setObjectName(u"label_repeat_password_in_registration")

        self.gridLayout.addWidget(self.label_repeat_password_in_registration, 7, 0, 1, 1)

        self.lineEdit_phone_or_email_number_in_registration = QLineEdit(self.frame_registration)
        self.lineEdit_phone_or_email_number_in_registration.setObjectName(u"lineEdit_phone_or_email_number_in_registration")

        self.gridLayout.addWidget(self.lineEdit_phone_or_email_number_in_registration, 3, 1, 1, 1)

        self.label_hint_in_registration = QLabel(self.frame_registration)
        self.label_hint_in_registration.setObjectName(u"label_hint_in_registration")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_hint_in_registration.sizePolicy().hasHeightForWidth())
        self.label_hint_in_registration.setSizePolicy(sizePolicy8)

        self.gridLayout.addWidget(self.label_hint_in_registration, 8, 0, 1, 3)

        self.label_verify_code_in_registration = QLabel(self.frame_registration)
        self.label_verify_code_in_registration.setObjectName(u"label_verify_code_in_registration")

        self.gridLayout.addWidget(self.label_verify_code_in_registration, 4, 0, 1, 1)

        self.label_set_password_in_registration = QLabel(self.frame_registration)
        self.label_set_password_in_registration.setObjectName(u"label_set_password_in_registration")

        self.gridLayout.addWidget(self.label_set_password_in_registration, 6, 0, 1, 1)

        self.lineEdit_verify_code_in_registration = QLineEdit(self.frame_registration)
        self.lineEdit_verify_code_in_registration.setObjectName(u"lineEdit_verify_code_in_registration")

        self.gridLayout.addWidget(self.lineEdit_verify_code_in_registration, 4, 1, 1, 2)

        self.lineEdit_set_password_in_registration = QLineEdit(self.frame_registration)
        self.lineEdit_set_password_in_registration.setObjectName(u"lineEdit_set_password_in_registration")

        self.gridLayout.addWidget(self.lineEdit_set_password_in_registration, 6, 1, 1, 2)

        self.lineEdit_username_in_registration = QLineEdit(self.frame_registration)
        self.lineEdit_username_in_registration.setObjectName(u"lineEdit_username_in_registration")

        self.gridLayout.addWidget(self.lineEdit_username_in_registration, 1, 1, 1, 2)

        self.label_phone_or_email_number_in_registration = QLabel(self.frame_registration)
        self.label_phone_or_email_number_in_registration.setObjectName(u"label_phone_or_email_number_in_registration")

        self.gridLayout.addWidget(self.label_phone_or_email_number_in_registration, 3, 0, 1, 1)

        self.lineEdit_repeat_password_in_registration = QLineEdit(self.frame_registration)
        self.lineEdit_repeat_password_in_registration.setObjectName(u"lineEdit_repeat_password_in_registration")

        self.gridLayout.addWidget(self.lineEdit_repeat_password_in_registration, 7, 1, 1, 2)

        self.pushButton_goback_login_in_registration = QPushButton(self.frame_registration)
        self.pushButton_goback_login_in_registration.setObjectName(u"pushButton_goback_login_in_registration")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(2)
        sizePolicy9.setHeightForWidth(self.pushButton_goback_login_in_registration.sizePolicy().hasHeightForWidth())
        self.pushButton_goback_login_in_registration.setSizePolicy(sizePolicy9)
        self.pushButton_goback_login_in_registration.setMaximumSize(QSize(200, 100))

        self.gridLayout.addWidget(self.pushButton_goback_login_in_registration, 9, 2, 1, 1)

        self.pushButton_registration_in_registration = QPushButton(self.frame_registration)
        self.pushButton_registration_in_registration.setObjectName(u"pushButton_registration_in_registration")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(2)
        sizePolicy10.setHeightForWidth(self.pushButton_registration_in_registration.sizePolicy().hasHeightForWidth())
        self.pushButton_registration_in_registration.setSizePolicy(sizePolicy10)
        self.pushButton_registration_in_registration.setMaximumSize(QSize(16777215, 100))

        self.gridLayout.addWidget(self.pushButton_registration_in_registration, 9, 0, 1, 2)

        self.label_registration = QLabel(self.frame_registration)
        self.label_registration.setObjectName(u"label_registration")
        sizePolicy8.setHeightForWidth(self.label_registration.sizePolicy().hasHeightForWidth())
        self.label_registration.setSizePolicy(sizePolicy8)
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.label_registration.setFont(font4)
        self.label_registration.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_registration, 0, 0, 1, 3)

        self.pushButton_send_verify_code_in_registration = QPushButton(self.frame_registration)
        self.pushButton_send_verify_code_in_registration.setObjectName(u"pushButton_send_verify_code_in_registration")
        sizePolicy2.setHeightForWidth(self.pushButton_send_verify_code_in_registration.sizePolicy().hasHeightForWidth())
        self.pushButton_send_verify_code_in_registration.setSizePolicy(sizePolicy2)
        self.pushButton_send_verify_code_in_registration.setMaximumSize(QSize(200, 100))

        self.gridLayout.addWidget(self.pushButton_send_verify_code_in_registration, 3, 2, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_registration)

        self.tabWidget.addTab(self.tab_registration, "")
        self.tab_forgot_password = QWidget()
        self.tab_forgot_password.setObjectName(u"tab_forgot_password")
        self.verticalLayout_8 = QVBoxLayout(self.tab_forgot_password)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_forgot_password = QFrame(self.tab_forgot_password)
        self.frame_forgot_password.setObjectName(u"frame_forgot_password")
        self.frame_forgot_password.setFrameShape(QFrame.StyledPanel)
        self.frame_forgot_password.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_forgot_password)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_verify_code_in_forgot_password = QLineEdit(self.frame_forgot_password)
        self.lineEdit_verify_code_in_forgot_password.setObjectName(u"lineEdit_verify_code_in_forgot_password")

        self.gridLayout_2.addWidget(self.lineEdit_verify_code_in_forgot_password, 3, 1, 1, 2)

        self.pushButton_save_new_password_in_forgot_password = QPushButton(self.frame_forgot_password)
        self.pushButton_save_new_password_in_forgot_password.setObjectName(u"pushButton_save_new_password_in_forgot_password")
        sizePolicy9.setHeightForWidth(self.pushButton_save_new_password_in_forgot_password.sizePolicy().hasHeightForWidth())
        self.pushButton_save_new_password_in_forgot_password.setSizePolicy(sizePolicy9)
        self.pushButton_save_new_password_in_forgot_password.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_2.addWidget(self.pushButton_save_new_password_in_forgot_password, 7, 0, 1, 2)

        self.label_verify_code_in_forgot_password = QLabel(self.frame_forgot_password)
        self.label_verify_code_in_forgot_password.setObjectName(u"label_verify_code_in_forgot_password")

        self.gridLayout_2.addWidget(self.label_verify_code_in_forgot_password, 3, 0, 1, 1)

        self.label_repeat_password_in_forgot_password = QLabel(self.frame_forgot_password)
        self.label_repeat_password_in_forgot_password.setObjectName(u"label_repeat_password_in_forgot_password")

        self.gridLayout_2.addWidget(self.label_repeat_password_in_forgot_password, 5, 0, 1, 1)

        self.pushButton_send_verify_code_in_forgot_password = QPushButton(self.frame_forgot_password)
        self.pushButton_send_verify_code_in_forgot_password.setObjectName(u"pushButton_send_verify_code_in_forgot_password")
        sizePolicy2.setHeightForWidth(self.pushButton_send_verify_code_in_forgot_password.sizePolicy().hasHeightForWidth())
        self.pushButton_send_verify_code_in_forgot_password.setSizePolicy(sizePolicy2)
        self.pushButton_send_verify_code_in_forgot_password.setMaximumSize(QSize(200, 100))

        self.gridLayout_2.addWidget(self.pushButton_send_verify_code_in_forgot_password, 2, 2, 1, 1)

        self.lineEdit_username__in_forgot_password = QLineEdit(self.frame_forgot_password)
        self.lineEdit_username__in_forgot_password.setObjectName(u"lineEdit_username__in_forgot_password")

        self.gridLayout_2.addWidget(self.lineEdit_username__in_forgot_password, 1, 1, 1, 2)

        self.label_hint_in_forgot_password = QLabel(self.frame_forgot_password)
        self.label_hint_in_forgot_password.setObjectName(u"label_hint_in_forgot_password")
        sizePolicy8.setHeightForWidth(self.label_hint_in_forgot_password.sizePolicy().hasHeightForWidth())
        self.label_hint_in_forgot_password.setSizePolicy(sizePolicy8)

        self.gridLayout_2.addWidget(self.label_hint_in_forgot_password, 6, 0, 1, 3)

        self.label_forgot_password = QLabel(self.frame_forgot_password)
        self.label_forgot_password.setObjectName(u"label_forgot_password")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(1)
        sizePolicy11.setHeightForWidth(self.label_forgot_password.sizePolicy().hasHeightForWidth())
        self.label_forgot_password.setSizePolicy(sizePolicy11)
        self.label_forgot_password.setFont(font4)
        self.label_forgot_password.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.label_forgot_password, 0, 0, 1, 3)

        self.lineEdit_new_password_in_forgot_password = QLineEdit(self.frame_forgot_password)
        self.lineEdit_new_password_in_forgot_password.setObjectName(u"lineEdit_new_password_in_forgot_password")

        self.gridLayout_2.addWidget(self.lineEdit_new_password_in_forgot_password, 4, 1, 1, 2)

        self.lineEdit_repeat_password_in_forgot_password = QLineEdit(self.frame_forgot_password)
        self.lineEdit_repeat_password_in_forgot_password.setObjectName(u"lineEdit_repeat_password_in_forgot_password")

        self.gridLayout_2.addWidget(self.lineEdit_repeat_password_in_forgot_password, 5, 1, 1, 2)

        self.label_phone_or_email_number_in_forgot_password = QLabel(self.frame_forgot_password)
        self.label_phone_or_email_number_in_forgot_password.setObjectName(u"label_phone_or_email_number_in_forgot_password")

        self.gridLayout_2.addWidget(self.label_phone_or_email_number_in_forgot_password, 2, 0, 1, 1)

        self.lineEdit_phone_or_email_number_in_forgot_password = QLineEdit(self.frame_forgot_password)
        self.lineEdit_phone_or_email_number_in_forgot_password.setObjectName(u"lineEdit_phone_or_email_number_in_forgot_password")

        self.gridLayout_2.addWidget(self.lineEdit_phone_or_email_number_in_forgot_password, 2, 1, 1, 1)

        self.label_username__in_forgot_password = QLabel(self.frame_forgot_password)
        self.label_username__in_forgot_password.setObjectName(u"label_username__in_forgot_password")

        self.gridLayout_2.addWidget(self.label_username__in_forgot_password, 1, 0, 1, 1)

        self.label_new_password_in_forgot_password = QLabel(self.frame_forgot_password)
        self.label_new_password_in_forgot_password.setObjectName(u"label_new_password_in_forgot_password")

        self.gridLayout_2.addWidget(self.label_new_password_in_forgot_password, 4, 0, 1, 1)

        self.pushButton_goback_login_in_forgot_password = QPushButton(self.frame_forgot_password)
        self.pushButton_goback_login_in_forgot_password.setObjectName(u"pushButton_goback_login_in_forgot_password")
        sizePolicy9.setHeightForWidth(self.pushButton_goback_login_in_forgot_password.sizePolicy().hasHeightForWidth())
        self.pushButton_goback_login_in_forgot_password.setSizePolicy(sizePolicy9)
        self.pushButton_goback_login_in_forgot_password.setMaximumSize(QSize(200, 100))

        self.gridLayout_2.addWidget(self.pushButton_goback_login_in_forgot_password, 7, 2, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_forgot_password)

        self.tabWidget.addTab(self.tab_forgot_password, "")
        self.tab_agreement = QWidget()
        self.tab_agreement.setObjectName(u"tab_agreement")
        self.verticalLayout_5 = QVBoxLayout(self.tab_agreement)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_agreement_details = QFrame(self.tab_agreement)
        self.frame_agreement_details.setObjectName(u"frame_agreement_details")
        self.frame_agreement_details.setFrameShape(QFrame.StyledPanel)
        self.frame_agreement_details.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_agreement_details)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_agreement = QLabel(self.frame_agreement_details)
        self.label_agreement.setObjectName(u"label_agreement")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.label_agreement.sizePolicy().hasHeightForWidth())
        self.label_agreement.setSizePolicy(sizePolicy12)
        self.label_agreement.setFont(font4)
        self.label_agreement.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_4.addWidget(self.label_agreement)

        self.textBrowser_agreement_details_in_agreement_details = QTextBrowser(self.frame_agreement_details)
        self.textBrowser_agreement_details_in_agreement_details.setObjectName(u"textBrowser_agreement_details_in_agreement_details")
        sizePolicy2.setHeightForWidth(self.textBrowser_agreement_details_in_agreement_details.sizePolicy().hasHeightForWidth())
        self.textBrowser_agreement_details_in_agreement_details.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.textBrowser_agreement_details_in_agreement_details)

        self.pushButton_goback_login_in_agreement_details = QPushButton(self.frame_agreement_details)
        self.pushButton_goback_login_in_agreement_details.setObjectName(u"pushButton_goback_login_in_agreement_details")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.pushButton_goback_login_in_agreement_details.sizePolicy().hasHeightForWidth())
        self.pushButton_goback_login_in_agreement_details.setSizePolicy(sizePolicy13)
        self.pushButton_goback_login_in_agreement_details.setMinimumSize(QSize(0, 50))
        self.pushButton_goback_login_in_agreement_details.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_4.addWidget(self.pushButton_goback_login_in_agreement_details)


        self.verticalLayout_5.addWidget(self.frame_agreement_details)

        self.tabWidget.addTab(self.tab_agreement, "")
        self.tab_about = QWidget()
        self.tab_about.setObjectName(u"tab_about")
        self.verticalLayout_6 = QVBoxLayout(self.tab_about)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_about = QFrame(self.tab_about)
        self.frame_about.setObjectName(u"frame_about")
        self.frame_about.setFrameShape(QFrame.StyledPanel)
        self.frame_about.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_about)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_abuot = QLabel(self.frame_about)
        self.label_abuot.setObjectName(u"label_abuot")
        sizePolicy8.setHeightForWidth(self.label_abuot.sizePolicy().hasHeightForWidth())
        self.label_abuot.setSizePolicy(sizePolicy8)
        self.label_abuot.setFont(font4)
        self.label_abuot.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_9.addWidget(self.label_abuot)

        self.textBrowser_agreement_details_in_agreement_details_2 = QTextBrowser(self.frame_about)
        self.textBrowser_agreement_details_in_agreement_details_2.setObjectName(u"textBrowser_agreement_details_in_agreement_details_2")
        sizePolicy2.setHeightForWidth(self.textBrowser_agreement_details_in_agreement_details_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_agreement_details_in_agreement_details_2.setSizePolicy(sizePolicy2)

        self.verticalLayout_9.addWidget(self.textBrowser_agreement_details_in_agreement_details_2)

        self.pushButton_goback_login_in_about = QPushButton(self.frame_about)
        self.pushButton_goback_login_in_about.setObjectName(u"pushButton_goback_login_in_about")
        sizePolicy13.setHeightForWidth(self.pushButton_goback_login_in_about.sizePolicy().hasHeightForWidth())
        self.pushButton_goback_login_in_about.setSizePolicy(sizePolicy13)
        self.pushButton_goback_login_in_about.setMinimumSize(QSize(0, 50))
        self.pushButton_goback_login_in_about.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_9.addWidget(self.pushButton_goback_login_in_about)


        self.verticalLayout_6.addWidget(self.frame_about)

        self.tabWidget.addTab(self.tab_about, "")

        self.verticalLayout_Login.addWidget(self.tabWidget)


        self.verticalLayout_10.addLayout(self.verticalLayout_Login)

#if QT_CONFIG(shortcut)
        self.label_username.setBuddy(self.lineEdit_username)
        self.label_password.setBuddy(self.lineEdit_password)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Dialog)
        self.pushButton_clear_username_and_password.clicked.connect(self.lineEdit_username.clear)
        self.pushButton_clear_username_and_password.clicked.connect(self.lineEdit_password.clear)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u6b22\u8fce\u4f7f\u7528\uff0c\u8bf7\u5148\u767b\u5f55", None))
        self.label_welcome.setText(QCoreApplication.translate("Dialog", u"\u6b22\u8fce\u4f7f\u7528\uff0c\u8bf7\u5148\u767b\u5f55", None))
        self.label_username.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u540d(&N)\uff1a", None))
        self.label_password.setText(QCoreApplication.translate("Dialog", u"\u5bc6\u7801(&P)\uff1a", None))
        self.pushButton_clear_username_and_password.setText(QCoreApplication.translate("Dialog", u"\u6e05\u7a7a(C)", None))
#if QT_CONFIG(shortcut)
        self.pushButton_clear_username_and_password.setShortcut(QCoreApplication.translate("Dialog", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
        self.commandLinkButton_goto_read_agreement.setText(QCoreApplication.translate("Dialog", u"\u4f7f\u7528\u524d\uff0c\u8bf7\u5148\u9605\u8bfb\u5e76\u540c\u610f\u300a\u534f\u8bae\u300b", None))
        self.checkBox_agree_agreement.setText(QCoreApplication.translate("Dialog", u"\u6211\u5df2\u9605\u8bfb\u5e76\u540c\u610f \u300a\u534f\u8bae\u300b(Y)", None))
#if QT_CONFIG(shortcut)
        self.checkBox_agree_agreement.setShortcut(QCoreApplication.translate("Dialog", u"Alt+Y", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_goto_registration.setText(QCoreApplication.translate("Dialog", u"\u6ce8\u518c(R)", None))
#if QT_CONFIG(shortcut)
        self.pushButton_goto_registration.setShortcut(QCoreApplication.translate("Dialog", u"Alt+R", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_goto_forgot_password.setText(QCoreApplication.translate("Dialog", u"\u5fd8\u8bb0\u5bc6\u7801(F)", None))
#if QT_CONFIG(shortcut)
        self.pushButton_goto_forgot_password.setShortcut(QCoreApplication.translate("Dialog", u"Alt+F", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButton_login.setToolTip(QCoreApplication.translate("Dialog", u"\u52fe\u9009\u540c\u610f\u300a\u534f\u8bae\u300b\u624d\u80fd\u767b\u5f55", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_login.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pushButton_login.setText(QCoreApplication.translate("Dialog", u"\u767b\u5f55(Enter)", None))
#if QT_CONFIG(shortcut)
        self.pushButton_login.setShortcut(QCoreApplication.translate("Dialog", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Login), QCoreApplication.translate("Dialog", u"\u767b\u5f55", None))
        self.label_username_in_registration.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u540d\uff1a", None))
        self.label_repeat_password_in_registration.setText(QCoreApplication.translate("Dialog", u"\u518d\u6b21\u8f93\u5165\u5bc6\u7801\uff1a", None))
        self.label_hint_in_registration.setText(QCoreApplication.translate("Dialog", u"\u63d0\u793a\uff1a\u624b\u673a\u53f7/\u90ae\u7bb1\u683c\u5f0f\u4e0d\u6b63\u786e", None))
        self.label_verify_code_in_registration.setText(QCoreApplication.translate("Dialog", u"\u9a8c\u8bc1\u7801\uff1a", None))
        self.label_set_password_in_registration.setText(QCoreApplication.translate("Dialog", u"\u8bbe\u7f6e\u5bc6\u7801\uff1a", None))
        self.label_phone_or_email_number_in_registration.setText(QCoreApplication.translate("Dialog", u"\u624b\u673a\u53f7/\u90ae\u7bb1\uff1a", None))
        self.pushButton_goback_login_in_registration.setText(QCoreApplication.translate("Dialog", u"\u8fd4\u56de(Esc)", None))
#if QT_CONFIG(shortcut)
        self.pushButton_goback_login_in_registration.setShortcut(QCoreApplication.translate("Dialog", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_registration_in_registration.setText(QCoreApplication.translate("Dialog", u"\u6ce8\u518c", None))
#if QT_CONFIG(shortcut)
        self.pushButton_registration_in_registration.setShortcut(QCoreApplication.translate("Dialog", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_registration.setText(QCoreApplication.translate("Dialog", u"\u6ce8\u518c", None))
        self.pushButton_send_verify_code_in_registration.setText(QCoreApplication.translate("Dialog", u"\u53d1\u9001\u9a8c\u8bc1\u7801", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_registration), QCoreApplication.translate("Dialog", u"\u6ce8\u518c", None))
        self.pushButton_save_new_password_in_forgot_password.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58\u8bbe\u7f6e", None))
#if QT_CONFIG(shortcut)
        self.pushButton_save_new_password_in_forgot_password.setShortcut(QCoreApplication.translate("Dialog", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_verify_code_in_forgot_password.setText(QCoreApplication.translate("Dialog", u"\u9a8c\u8bc1\u7801\uff1a", None))
        self.label_repeat_password_in_forgot_password.setText(QCoreApplication.translate("Dialog", u"\u518d\u6b21\u8f93\u5165\u5bc6\u7801\uff1a", None))
        self.pushButton_send_verify_code_in_forgot_password.setText(QCoreApplication.translate("Dialog", u"\u53d1\u9001\u9a8c\u8bc1\u7801", None))
        self.label_hint_in_forgot_password.setText(QCoreApplication.translate("Dialog", u"\u63d0\u793a\uff1a\u624b\u673a\u53f7/\u90ae\u7bb1\u683c\u5f0f\u4e0d\u6b63\u786e", None))
        self.label_forgot_password.setText(QCoreApplication.translate("Dialog", u"\u5fd8\u8bb0\u5bc6\u7801", None))
        self.label_phone_or_email_number_in_forgot_password.setText(QCoreApplication.translate("Dialog", u"\u624b\u673a\u53f7/\u90ae\u7bb1\uff1a", None))
        self.label_username__in_forgot_password.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u540d\uff1a", None))
        self.label_new_password_in_forgot_password.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5bc6\u7801\uff1a", None))
        self.pushButton_goback_login_in_forgot_password.setText(QCoreApplication.translate("Dialog", u"\u8fd4\u56de(Esc)", None))
#if QT_CONFIG(shortcut)
        self.pushButton_goback_login_in_forgot_password.setShortcut(QCoreApplication.translate("Dialog", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_forgot_password), QCoreApplication.translate("Dialog", u"\u5fd8\u8bb0\u5bc6\u7801", None))
        self.label_agreement.setText(QCoreApplication.translate("Dialog", u"\u300aXXX \u534f\u8bae\u300b", None))
        self.textBrowser_agreement_details_in_agreement_details.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae"
                        "\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f"
                        "\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9"
                        "\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185"
                        "\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae"
                        "\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f"
                        "\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9"
                        "\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185"
                        "\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae"
                        "\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f"
                        "\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9"
                        "\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185"
                        "\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9\u534f\u8bae\u5185\u5bb9</p></body></html>", None))
        self.pushButton_goback_login_in_agreement_details.setText(QCoreApplication.translate("Dialog", u"\u8fd4\u56de(Esc)", None))
#if QT_CONFIG(shortcut)
        self.pushButton_goback_login_in_agreement_details.setShortcut(QCoreApplication.translate("Dialog", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_agreement), QCoreApplication.translate("Dialog", u"\u534f\u8bae", None))
        self.label_abuot.setText(QCoreApplication.translate("Dialog", u"\u5173\u4e8e", None))
        self.textBrowser_agreement_details_in_agreement_details_2.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e"
                        "\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9\u5173\u4e8e\u5185\u5bb9</p></body></html>", None))
        self.pushButton_goback_login_in_about.setText(QCoreApplication.translate("Dialog", u"\u8fd4\u56de(Esc)", None))
#if QT_CONFIG(shortcut)
        self.pushButton_goback_login_in_about.setShortcut(QCoreApplication.translate("Dialog", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_about), QCoreApplication.translate("Dialog", u"\u5173\u4e8e", None))
    # retranslateUi

