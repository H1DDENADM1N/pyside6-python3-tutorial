# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'base64.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow_base64_encode_decode(object):
    def setupUi(self, MainWindow_base64_encode_decode):
        if not MainWindow_base64_encode_decode.objectName():
            MainWindow_base64_encode_decode.setObjectName(u"MainWindow_base64_encode_decode")
        MainWindow_base64_encode_decode.resize(604, 579)
        self.action_new = QAction(MainWindow_base64_encode_decode)
        self.action_new.setObjectName(u"action_new")
        self.action_open = QAction(MainWindow_base64_encode_decode)
        self.action_open.setObjectName(u"action_open")
        self.action_close = QAction(MainWindow_base64_encode_decode)
        self.action_close.setObjectName(u"action_close")
        self.action_save = QAction(MainWindow_base64_encode_decode)
        self.action_save.setObjectName(u"action_save")
        self.action_save.setMenuRole(QAction.NoRole)
        self.action_save_as = QAction(MainWindow_base64_encode_decode)
        self.action_save_as.setObjectName(u"action_save_as")
        self.action_save_as.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow_base64_encode_decode)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_file_name = QWidget()
        self.tab_file_name.setObjectName(u"tab_file_name")
        self.verticalLayout_2 = QVBoxLayout(self.tab_file_name)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_file_content = QGroupBox(self.tab_file_name)
        self.groupBox_file_content.setObjectName(u"groupBox_file_content")
        self.verticalLayout = QVBoxLayout(self.groupBox_file_content)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plainTextEdit = QPlainTextEdit(self.groupBox_file_content)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)


        self.verticalLayout_2.addWidget(self.groupBox_file_content)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_encode = QPushButton(self.tab_file_name)
        self.pushButton_encode.setObjectName(u"pushButton_encode")

        self.horizontalLayout.addWidget(self.pushButton_encode)

        self.pushButton_decode = QPushButton(self.tab_file_name)
        self.pushButton_decode.setObjectName(u"pushButton_decode")

        self.horizontalLayout.addWidget(self.pushButton_decode)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.groupBox_file_result = QGroupBox(self.tab_file_name)
        self.groupBox_file_result.setObjectName(u"groupBox_file_result")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_file_result)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.plainTextEdit_result = QPlainTextEdit(self.groupBox_file_result)
        self.plainTextEdit_result.setObjectName(u"plainTextEdit_result")

        self.verticalLayout_3.addWidget(self.plainTextEdit_result)


        self.verticalLayout_2.addWidget(self.groupBox_file_result)

        self.tabWidget.addTab(self.tab_file_name, "")

        self.verticalLayout_4.addWidget(self.tabWidget)

        MainWindow_base64_encode_decode.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow_base64_encode_decode)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 604, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow_base64_encode_decode.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow_base64_encode_decode)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow_base64_encode_decode.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow_base64_encode_decode)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow_base64_encode_decode.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_new)
        self.menu.addAction(self.action_open)
        self.menu.addAction(self.action_save)
        self.menu.addAction(self.action_save_as)
        self.menu.addAction(self.action_close)
        self.toolBar.addAction(self.action_new)
        self.toolBar.addAction(self.action_open)
        self.toolBar.addAction(self.action_close)

        self.retranslateUi(MainWindow_base64_encode_decode)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow_base64_encode_decode)
    # setupUi

    def retranslateUi(self, MainWindow_base64_encode_decode):
        MainWindow_base64_encode_decode.setWindowTitle(QCoreApplication.translate("MainWindow_base64_encode_decode", u"Base64\u7f16\u89e3\u7801\u5668", None))
        self.action_new.setText(QCoreApplication.translate("MainWindow_base64_encode_decode", u"\u65b0\u5efa", None))
#if QT_CONFIG(shortcut)
        self.action_new.setShortcut(QCoreApplication.translate("MainWindow_base64_encode_decode", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_open.setText(QCoreApplication.translate("MainWindow_base64_encode_decode", u"\u6253\u5f00", None))
#if QT_CONFIG(shortcut)
        self.action_open.setShortcut(QCoreApplication.translate("MainWindow_base64_encode_decode", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_close.setText(QCoreApplication.translate("MainWindow_base64_encode_decode", u"\u5173\u95ed", None))
#if QT_CONFIG(shortcut)
        self.action_close.setShortcut(QCoreApplication.translate("MainWindow_base64_encode_decode", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.action_save.setText(QCoreApplication.translate("MainWindow_base64_encode_decode", u"\u4fdd\u5b58", None))
#if QT_CONFIG(shortcut)
        self.action_save.setShortcut(QCoreApplication.translate("MainWindow_base64_encode_decode", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_save_as.setText(QCoreApplication.translate("MainWindow_base64_encode_decode", u"\u53e6\u5b58\u4e3a", None))
#if QT_CONFIG(shortcut)
        self.action_save_as.setShortcut(QCoreApplication.translate("MainWindow_base64_encode_decode", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_file_content.setTitle(QCoreApplication.translate("MainWindow_base64_encode_decode", u"\u6587\u4ef6\u5185\u5bb9", None))
        self.pushButton_encode.setText(QCoreApplication.translate("MainWindow_base64_encode_decode", u"\u7f16\u7801(E)", None))
#if QT_CONFIG(shortcut)
        self.pushButton_encode.setShortcut(QCoreApplication.translate("MainWindow_base64_encode_decode", u"Alt+E", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_decode.setText(QCoreApplication.translate("MainWindow_base64_encode_decode", u"\u89e3\u7801(D)", None))
#if QT_CONFIG(shortcut)
        self.pushButton_decode.setShortcut(QCoreApplication.translate("MainWindow_base64_encode_decode", u"Alt+D", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_file_result.setTitle(QCoreApplication.translate("MainWindow_base64_encode_decode", u"\u7ed3\u679c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_file_name), QCoreApplication.translate("MainWindow_base64_encode_decode", u"\u6587\u4ef6\u540d", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow_base64_encode_decode", u"\u6587\u4ef6", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow_base64_encode_decode", u"toolBar", None))
    # retranslateUi

