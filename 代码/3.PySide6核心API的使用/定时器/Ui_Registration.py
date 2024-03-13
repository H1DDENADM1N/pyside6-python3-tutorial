# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Registration.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Registration(object):
    def setupUi(self, Registration):
        if not Registration.objectName():
            Registration.setObjectName(u"Registration")
        Registration.resize(469, 272)
        self.verticalLayout = QVBoxLayout(Registration)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_registration = QFrame(Registration)
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_hint_in_registration.sizePolicy().hasHeightForWidth())
        self.label_hint_in_registration.setSizePolicy(sizePolicy)

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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.pushButton_goback_login_in_registration.sizePolicy().hasHeightForWidth())
        self.pushButton_goback_login_in_registration.setSizePolicy(sizePolicy1)
        self.pushButton_goback_login_in_registration.setMaximumSize(QSize(200, 100))

        self.gridLayout.addWidget(self.pushButton_goback_login_in_registration, 9, 2, 1, 1)

        self.pushButton_registration_in_registration = QPushButton(self.frame_registration)
        self.pushButton_registration_in_registration.setObjectName(u"pushButton_registration_in_registration")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.pushButton_registration_in_registration.sizePolicy().hasHeightForWidth())
        self.pushButton_registration_in_registration.setSizePolicy(sizePolicy2)
        self.pushButton_registration_in_registration.setMaximumSize(QSize(16777215, 100))

        self.gridLayout.addWidget(self.pushButton_registration_in_registration, 9, 0, 1, 2)

        self.label_registration = QLabel(self.frame_registration)
        self.label_registration.setObjectName(u"label_registration")
        sizePolicy.setHeightForWidth(self.label_registration.sizePolicy().hasHeightForWidth())
        self.label_registration.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_registration.setFont(font)
        self.label_registration.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_registration, 0, 0, 1, 3)

        self.pushButton_send_verify_code_in_registration = QPushButton(self.frame_registration)
        self.pushButton_send_verify_code_in_registration.setObjectName(u"pushButton_send_verify_code_in_registration")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.pushButton_send_verify_code_in_registration.sizePolicy().hasHeightForWidth())
        self.pushButton_send_verify_code_in_registration.setSizePolicy(sizePolicy3)
        self.pushButton_send_verify_code_in_registration.setMaximumSize(QSize(200, 100))

        self.gridLayout.addWidget(self.pushButton_send_verify_code_in_registration, 3, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame_registration)


        self.retranslateUi(Registration)

        QMetaObject.connectSlotsByName(Registration)
    # setupUi

    def retranslateUi(self, Registration):
        Registration.setWindowTitle(QCoreApplication.translate("Registration", u"\u6ce8\u518c", None))
        self.label_username_in_registration.setText(QCoreApplication.translate("Registration", u"\u7528\u6237\u540d\uff1a", None))
        self.label_repeat_password_in_registration.setText(QCoreApplication.translate("Registration", u"\u518d\u6b21\u8f93\u5165\u5bc6\u7801\uff1a", None))
        self.label_hint_in_registration.setText(QCoreApplication.translate("Registration", u"\u63d0\u793a\uff1a\u624b\u673a\u53f7/\u90ae\u7bb1\u683c\u5f0f\u4e0d\u6b63\u786e", None))
        self.label_verify_code_in_registration.setText(QCoreApplication.translate("Registration", u"\u9a8c\u8bc1\u7801\uff1a", None))
        self.label_set_password_in_registration.setText(QCoreApplication.translate("Registration", u"\u8bbe\u7f6e\u5bc6\u7801\uff1a", None))
        self.label_phone_or_email_number_in_registration.setText(QCoreApplication.translate("Registration", u"\u624b\u673a\u53f7/\u90ae\u7bb1\uff1a", None))
        self.pushButton_goback_login_in_registration.setText(QCoreApplication.translate("Registration", u"\u8fd4\u56de(Esc)", None))
#if QT_CONFIG(shortcut)
        self.pushButton_goback_login_in_registration.setShortcut(QCoreApplication.translate("Registration", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_registration_in_registration.setText(QCoreApplication.translate("Registration", u"\u6ce8\u518c", None))
#if QT_CONFIG(shortcut)
        self.pushButton_registration_in_registration.setShortcut(QCoreApplication.translate("Registration", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_registration.setText(QCoreApplication.translate("Registration", u"\u6ce8\u518c", None))
        self.pushButton_send_verify_code_in_registration.setText(QCoreApplication.translate("Registration", u"\u53d1\u9001\u9a8c\u8bc1\u7801", None))
    # retranslateUi

