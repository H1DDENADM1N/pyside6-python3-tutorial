# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'List.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Form_List(object):
    def setupUi(self, Form_List):
        if not Form_List.objectName():
            Form_List.setObjectName(u"Form_List")
        Form_List.resize(610, 1086)
        self.horizontalLayout_19 = QHBoxLayout(Form_List)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_title = QLabel(Form_List)
        self.label_title.setObjectName(u"label_title")

        self.horizontalLayout_15.addWidget(self.label_title)

        self.label_current_item = QLabel(Form_List)
        self.label_current_item.setObjectName(u"label_current_item")

        self.horizontalLayout_15.addWidget(self.label_current_item)

        self.label_check_state = QLabel(Form_List)
        self.label_check_state.setObjectName(u"label_check_state")

        self.horizontalLayout_15.addWidget(self.label_check_state)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_8)


        self.verticalLayout_10.addLayout(self.horizontalLayout_15)

        self.listWidget_List = QListWidget(Form_List)
        QListWidgetItem(self.listWidget_List)
        QListWidgetItem(self.listWidget_List)
        QListWidgetItem(self.listWidget_List)
        QListWidgetItem(self.listWidget_List)
        QListWidgetItem(self.listWidget_List)
        QListWidgetItem(self.listWidget_List)
        QListWidgetItem(self.listWidget_List)
        QListWidgetItem(self.listWidget_List)
        QListWidgetItem(self.listWidget_List)
        self.listWidget_List.setObjectName(u"listWidget_List")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.listWidget_List.sizePolicy().hasHeightForWidth())
        self.listWidget_List.setSizePolicy(sizePolicy)

        self.verticalLayout_10.addWidget(self.listWidget_List)


        self.horizontalLayout_19.addLayout(self.verticalLayout_10)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_3 = QGroupBox(Form_List)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.pushButton_print_all = QPushButton(self.groupBox_3)
        self.pushButton_print_all.setObjectName(u"pushButton_print_all")

        self.verticalLayout_11.addWidget(self.pushButton_print_all)

        self.plainTextEdit_print_all = QPlainTextEdit(self.groupBox_3)
        self.plainTextEdit_print_all.setObjectName(u"plainTextEdit_print_all")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.plainTextEdit_print_all.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_print_all.setSizePolicy(sizePolicy1)

        self.verticalLayout_11.addWidget(self.plainTextEdit_print_all)


        self.verticalLayout_6.addWidget(self.groupBox_3)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.groupBox_2 = QGroupBox(Form_List)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_17 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.label_2)

        self.radioButton_ascending_order = QRadioButton(self.groupBox_2)
        self.buttonGroup = QButtonGroup(Form_List)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_ascending_order)
        self.radioButton_ascending_order.setObjectName(u"radioButton_ascending_order")
        self.radioButton_ascending_order.setChecked(True)

        self.verticalLayout_4.addWidget(self.radioButton_ascending_order)

        self.radioButton_descending_order = QRadioButton(self.groupBox_2)
        self.buttonGroup.addButton(self.radioButton_descending_order)
        self.radioButton_descending_order.setObjectName(u"radioButton_descending_order")

        self.verticalLayout_4.addWidget(self.radioButton_descending_order)

        self.radioButton_max_order = QRadioButton(self.groupBox_2)
        self.buttonGroup.addButton(self.radioButton_max_order)
        self.radioButton_max_order.setObjectName(u"radioButton_max_order")

        self.verticalLayout_4.addWidget(self.radioButton_max_order)

        self.radioButton_min_order = QRadioButton(self.groupBox_2)
        self.buttonGroup.addButton(self.radioButton_min_order)
        self.radioButton_min_order.setObjectName(u"radioButton_min_order")

        self.verticalLayout_4.addWidget(self.radioButton_min_order)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_17.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_sort = QPushButton(self.groupBox_2)
        self.pushButton_sort.setObjectName(u"pushButton_sort")

        self.verticalLayout_5.addWidget(self.pushButton_sort)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.horizontalLayout_17.addLayout(self.verticalLayout_5)


        self.horizontalLayout_16.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(Form_List)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_18 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pushButton_copy_current_item = QPushButton(self.groupBox)
        self.pushButton_copy_current_item.setObjectName(u"pushButton_copy_current_item")

        self.verticalLayout_8.addWidget(self.pushButton_copy_current_item)

        self.pushButton_delete_current_row = QPushButton(self.groupBox)
        self.pushButton_delete_current_row.setObjectName(u"pushButton_delete_current_row")

        self.verticalLayout_8.addWidget(self.pushButton_delete_current_row)

        self.pushButton_checkable_current_row = QPushButton(self.groupBox)
        self.pushButton_checkable_current_row.setObjectName(u"pushButton_checkable_current_row")

        self.verticalLayout_8.addWidget(self.pushButton_checkable_current_row)

        self.pushButton_uncheckable_current_row = QPushButton(self.groupBox)
        self.pushButton_uncheckable_current_row.setObjectName(u"pushButton_uncheckable_current_row")

        self.verticalLayout_8.addWidget(self.pushButton_uncheckable_current_row)


        self.horizontalLayout_18.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pushButton_moveToTop = QPushButton(self.groupBox)
        self.pushButton_moveToTop.setObjectName(u"pushButton_moveToTop")

        self.verticalLayout_9.addWidget(self.pushButton_moveToTop)

        self.pushButton_moveUp = QPushButton(self.groupBox)
        self.pushButton_moveUp.setObjectName(u"pushButton_moveUp")

        self.verticalLayout_9.addWidget(self.pushButton_moveUp)

        self.pushButton_moveDown = QPushButton(self.groupBox)
        self.pushButton_moveDown.setObjectName(u"pushButton_moveDown")

        self.verticalLayout_9.addWidget(self.pushButton_moveDown)

        self.pushButton_moveToBottom = QPushButton(self.groupBox)
        self.pushButton_moveToBottom.setObjectName(u"pushButton_moveToBottom")

        self.verticalLayout_9.addWidget(self.pushButton_moveToBottom)


        self.horizontalLayout_18.addLayout(self.verticalLayout_9)


        self.horizontalLayout_16.addWidget(self.groupBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)


        self.verticalLayout_3.addLayout(self.verticalLayout_6)

        self.line_5 = QFrame(Form_List)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_5)

        self.groupBox_4 = QGroupBox(Form_List)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_add = QLineEdit(self.groupBox_4)
        self.lineEdit_add.setObjectName(u"lineEdit_add")

        self.horizontalLayout.addWidget(self.lineEdit_add)

        self.pushButton_add = QPushButton(self.groupBox_4)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.horizontalLayout.addWidget(self.pushButton_add)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit_add_s = QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit_add_s.setObjectName(u"plainTextEdit_add_s")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.plainTextEdit_add_s.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_add_s.setSizePolicy(sizePolicy3)

        self.horizontalLayout_11.addWidget(self.plainTextEdit_add_s)

        self.pushButton_add_s = QPushButton(self.groupBox_4)
        self.pushButton_add_s.setObjectName(u"pushButton_add_s")

        self.horizontalLayout_11.addWidget(self.pushButton_add_s)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_insert = QLineEdit(self.groupBox_4)
        self.lineEdit_insert.setObjectName(u"lineEdit_insert")

        self.horizontalLayout_2.addWidget(self.lineEdit_insert)

        self.spinBox_insert_position = QSpinBox(self.groupBox_4)
        self.spinBox_insert_position.setObjectName(u"spinBox_insert_position")

        self.horizontalLayout_2.addWidget(self.spinBox_insert_position)

        self.pushButton_insert = QPushButton(self.groupBox_4)
        self.pushButton_insert.setObjectName(u"pushButton_insert")

        self.horizontalLayout_2.addWidget(self.pushButton_insert)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.plainTextEdit_insert_s = QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit_insert_s.setObjectName(u"plainTextEdit_insert_s")
        sizePolicy3.setHeightForWidth(self.plainTextEdit_insert_s.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_insert_s.setSizePolicy(sizePolicy3)

        self.horizontalLayout_12.addWidget(self.plainTextEdit_insert_s)

        self.spinBox_insert_s_position = QSpinBox(self.groupBox_4)
        self.spinBox_insert_s_position.setObjectName(u"spinBox_insert_s_position")

        self.horizontalLayout_12.addWidget(self.spinBox_insert_s_position)

        self.pushButton_insert_s = QPushButton(self.groupBox_4)
        self.pushButton_insert_s.setObjectName(u"pushButton_insert_s")

        self.horizontalLayout_12.addWidget(self.pushButton_insert_s)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.line = QFrame(Form_List)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.groupBox_6 = QGroupBox(Form_List)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.radioButton_equal = QRadioButton(self.groupBox_6)
        self.buttonGroup_match = QButtonGroup(Form_List)
        self.buttonGroup_match.setObjectName(u"buttonGroup_match")
        self.buttonGroup_match.addButton(self.radioButton_equal)
        self.radioButton_equal.setObjectName(u"radioButton_equal")
        self.radioButton_equal.setChecked(True)

        self.verticalLayout_12.addWidget(self.radioButton_equal)

        self.radioButton_include = QRadioButton(self.groupBox_6)
        self.buttonGroup_match.addButton(self.radioButton_include)
        self.radioButton_include.setObjectName(u"radioButton_include")

        self.verticalLayout_12.addWidget(self.radioButton_include)

        self.radioButton_start_with = QRadioButton(self.groupBox_6)
        self.buttonGroup_match.addButton(self.radioButton_start_with)
        self.radioButton_start_with.setObjectName(u"radioButton_start_with")

        self.verticalLayout_12.addWidget(self.radioButton_start_with)

        self.radioButton_end_with = QRadioButton(self.groupBox_6)
        self.buttonGroup_match.addButton(self.radioButton_end_with)
        self.radioButton_end_with.setObjectName(u"radioButton_end_with")

        self.verticalLayout_12.addWidget(self.radioButton_end_with)

        self.radioButton_ignore_capltals = QRadioButton(self.groupBox_6)
        self.buttonGroup_match.addButton(self.radioButton_ignore_capltals)
        self.radioButton_ignore_capltals.setObjectName(u"radioButton_ignore_capltals")

        self.verticalLayout_12.addWidget(self.radioButton_ignore_capltals)

        self.radioButton_regular_expression = QRadioButton(self.groupBox_6)
        self.buttonGroup_match.addButton(self.radioButton_regular_expression)
        self.radioButton_regular_expression.setObjectName(u"radioButton_regular_expression")

        self.verticalLayout_12.addWidget(self.radioButton_regular_expression)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)


        self.horizontalLayout_14.addWidget(self.groupBox_6)

        self.line_4 = QFrame(Form_List)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_14.addWidget(self.line_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_5 = QGroupBox(Form_List)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_remove_by_position_result = QLabel(self.groupBox_5)
        self.label_remove_by_position_result.setObjectName(u"label_remove_by_position_result")

        self.horizontalLayout_3.addWidget(self.label_remove_by_position_result)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.spinBox_remove_by_position = QSpinBox(self.groupBox_5)
        self.spinBox_remove_by_position.setObjectName(u"spinBox_remove_by_position")

        self.horizontalLayout_3.addWidget(self.spinBox_remove_by_position)

        self.pushButton_remove_by_position = QPushButton(self.groupBox_5)
        self.pushButton_remove_by_position.setObjectName(u"pushButton_remove_by_position")

        self.horizontalLayout_3.addWidget(self.pushButton_remove_by_position)


        self.verticalLayout_13.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_remove_by_content_result = QLabel(self.groupBox_5)
        self.label_remove_by_content_result.setObjectName(u"label_remove_by_content_result")

        self.horizontalLayout_4.addWidget(self.label_remove_by_content_result)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.lineEdit_remove_by_content = QLineEdit(self.groupBox_5)
        self.lineEdit_remove_by_content.setObjectName(u"lineEdit_remove_by_content")

        self.horizontalLayout_4.addWidget(self.lineEdit_remove_by_content)

        self.pushButton_remove_by_content = QPushButton(self.groupBox_5)
        self.pushButton_remove_by_content.setObjectName(u"pushButton_remove_by_content")

        self.horizontalLayout_4.addWidget(self.pushButton_remove_by_content)


        self.verticalLayout_13.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_clear = QPushButton(self.groupBox_5)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.horizontalLayout_13.addWidget(self.pushButton_clear)


        self.verticalLayout_13.addLayout(self.horizontalLayout_13)


        self.verticalLayout.addWidget(self.groupBox_5)

        self.line_2 = QFrame(Form_List)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.groupBox_7 = QGroupBox(Form_List)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_modify_by_position_result = QLabel(self.groupBox_7)
        self.label_modify_by_position_result.setObjectName(u"label_modify_by_position_result")

        self.horizontalLayout_5.addWidget(self.label_modify_by_position_result)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.lineEdit_modify = QLineEdit(self.groupBox_7)
        self.lineEdit_modify.setObjectName(u"lineEdit_modify")

        self.horizontalLayout_5.addWidget(self.lineEdit_modify)

        self.spinBox_modify_position = QSpinBox(self.groupBox_7)
        self.spinBox_modify_position.setObjectName(u"spinBox_modify_position")

        self.horizontalLayout_5.addWidget(self.spinBox_modify_position)

        self.pushButton_modify = QPushButton(self.groupBox_7)
        self.pushButton_modify.setObjectName(u"pushButton_modify")

        self.horizontalLayout_5.addWidget(self.pushButton_modify)


        self.verticalLayout_14.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_replace_by_content_result = QLabel(self.groupBox_7)
        self.label_replace_by_content_result.setObjectName(u"label_replace_by_content_result")

        self.horizontalLayout_6.addWidget(self.label_replace_by_content_result)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.lineEdit_replace_old_content = QLineEdit(self.groupBox_7)
        self.lineEdit_replace_old_content.setObjectName(u"lineEdit_replace_old_content")

        self.horizontalLayout_6.addWidget(self.lineEdit_replace_old_content)

        self.lineEdit_replace_new_content = QLineEdit(self.groupBox_7)
        self.lineEdit_replace_new_content.setObjectName(u"lineEdit_replace_new_content")

        self.horizontalLayout_6.addWidget(self.lineEdit_replace_new_content)

        self.pushButton_replace = QPushButton(self.groupBox_7)
        self.pushButton_replace.setObjectName(u"pushButton_replace")

        self.horizontalLayout_6.addWidget(self.pushButton_replace)


        self.verticalLayout_14.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_change_position_result = QLabel(self.groupBox_7)
        self.label_change_position_result.setObjectName(u"label_change_position_result")

        self.horizontalLayout_7.addWidget(self.label_change_position_result)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.spinBox_change_position_1 = QSpinBox(self.groupBox_7)
        self.spinBox_change_position_1.setObjectName(u"spinBox_change_position_1")

        self.horizontalLayout_7.addWidget(self.spinBox_change_position_1)

        self.spinBox_change_position_2 = QSpinBox(self.groupBox_7)
        self.spinBox_change_position_2.setObjectName(u"spinBox_change_position_2")

        self.horizontalLayout_7.addWidget(self.spinBox_change_position_2)

        self.pushButton_change_position = QPushButton(self.groupBox_7)
        self.pushButton_change_position.setObjectName(u"pushButton_change_position")

        self.horizontalLayout_7.addWidget(self.pushButton_change_position)


        self.verticalLayout_14.addLayout(self.horizontalLayout_7)


        self.verticalLayout.addWidget(self.groupBox_7)

        self.line_3 = QFrame(Form_List)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.groupBox_8 = QGroupBox(Form_List)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_find_by_position_result = QLabel(self.groupBox_8)
        self.label_find_by_position_result.setObjectName(u"label_find_by_position_result")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_find_by_position_result.sizePolicy().hasHeightForWidth())
        self.label_find_by_position_result.setSizePolicy(sizePolicy4)

        self.horizontalLayout_8.addWidget(self.label_find_by_position_result)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.spinBox_find_result_position = QSpinBox(self.groupBox_8)
        self.spinBox_find_result_position.setObjectName(u"spinBox_find_result_position")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.spinBox_find_result_position.sizePolicy().hasHeightForWidth())
        self.spinBox_find_result_position.setSizePolicy(sizePolicy5)

        self.horizontalLayout_8.addWidget(self.spinBox_find_result_position)

        self.pushButton_find_by_position = QPushButton(self.groupBox_8)
        self.pushButton_find_by_position.setObjectName(u"pushButton_find_by_position")

        self.horizontalLayout_8.addWidget(self.pushButton_find_by_position)


        self.verticalLayout_15.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lineEdit_find_by_content = QLineEdit(self.groupBox_8)
        self.lineEdit_find_by_content.setObjectName(u"lineEdit_find_by_content")

        self.horizontalLayout_9.addWidget(self.lineEdit_find_by_content)

        self.label_find_by_content_result = QLabel(self.groupBox_8)
        self.label_find_by_content_result.setObjectName(u"label_find_by_content_result")

        self.horizontalLayout_9.addWidget(self.label_find_by_content_result)

        self.pushButton_find_by_content = QPushButton(self.groupBox_8)
        self.pushButton_find_by_content.setObjectName(u"pushButton_find_by_content")

        self.horizontalLayout_9.addWidget(self.pushButton_find_by_content)


        self.verticalLayout_15.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lineEdit_find_match = QLineEdit(self.groupBox_8)
        self.lineEdit_find_match.setObjectName(u"lineEdit_find_match")

        self.horizontalLayout_10.addWidget(self.lineEdit_find_match)

        self.pushButton_find_match = QPushButton(self.groupBox_8)
        self.pushButton_find_match.setObjectName(u"pushButton_find_match")

        self.horizontalLayout_10.addWidget(self.pushButton_find_match)


        self.verticalLayout_15.addLayout(self.horizontalLayout_10)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.plainTextEdit_find_include = QPlainTextEdit(self.groupBox_8)
        self.plainTextEdit_find_include.setObjectName(u"plainTextEdit_find_include")
        sizePolicy1.setHeightForWidth(self.plainTextEdit_find_include.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_find_include.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.plainTextEdit_find_include)


        self.verticalLayout_15.addLayout(self.verticalLayout_2)


        self.verticalLayout.addWidget(self.groupBox_8)


        self.horizontalLayout_14.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_19.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form_List)

        QMetaObject.connectSlotsByName(Form_List)
    # setupUi

    def retranslateUi(self, Form_List):
        Form_List.setWindowTitle(QCoreApplication.translate("Form_List", u"List", None))
        self.label_title.setText(QCoreApplication.translate("Form_List", u"\u5217\u8868", None))
        self.label_current_item.setText(QCoreApplication.translate("Form_List", u"\u5f53\u524d\u9879", None))
        self.label_check_state.setText(QCoreApplication.translate("Form_List", u"\u52fe\u9009\u72b6\u6001", None))

        __sortingEnabled = self.listWidget_List.isSortingEnabled()
        self.listWidget_List.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_List.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form_List", u"\u65b0\u5efa\u9879\u76ee0", None));
        ___qlistwidgetitem1 = self.listWidget_List.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form_List", u"\u65b0\u5efa\u9879\u76ee1", None));
        ___qlistwidgetitem2 = self.listWidget_List.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form_List", u"\u65b0\u5efa\u9879\u76ee2", None));
        ___qlistwidgetitem3 = self.listWidget_List.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Form_List", u"\u65b0\u5efa\u9879\u76ee3", None));
        ___qlistwidgetitem4 = self.listWidget_List.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Form_List", u"\u65b0\u5efa\u9879\u76ee4", None));
        ___qlistwidgetitem5 = self.listWidget_List.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Form_List", u"a", None));
        ___qlistwidgetitem6 = self.listWidget_List.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Form_List", u"A", None));
        ___qlistwidgetitem7 = self.listWidget_List.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("Form_List", u"aA", None));
        ___qlistwidgetitem8 = self.listWidget_List.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("Form_List", u"Aa", None));
        self.listWidget_List.setSortingEnabled(__sortingEnabled)

        self.groupBox_3.setTitle(QCoreApplication.translate("Form_List", u"\u8f93\u51fa\u5168\u90e8", None))
        self.pushButton_print_all.setText(QCoreApplication.translate("Form_List", u"\u8f93\u51fa\u5168\u90e8", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form_List", u"\u6392\u5e8f", None))
        self.label_2.setText(QCoreApplication.translate("Form_List", u"\u6392\u5e8f\u89c4\u5219", None))
        self.radioButton_ascending_order.setText(QCoreApplication.translate("Form_List", u"\u5347\u5e8f", None))
        self.radioButton_descending_order.setText(QCoreApplication.translate("Form_List", u"\u964d\u5e8f", None))
        self.radioButton_max_order.setText(QCoreApplication.translate("Form_List", u"\u5927\u6570\u4f18\u5148", None))
        self.radioButton_min_order.setText(QCoreApplication.translate("Form_List", u"\u5c0f\u6570\u4f18\u5148", None))
        self.pushButton_sort.setText(QCoreApplication.translate("Form_List", u"\u6392\u5e8f", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form_List", u"\u63a7\u5236\u9009\u4e2d\u9879", None))
        self.pushButton_copy_current_item.setText(QCoreApplication.translate("Form_List", u"\u590d\u5236\u5185\u5bb9", None))
        self.pushButton_delete_current_row.setText(QCoreApplication.translate("Form_List", u"\u5220\u9664", None))
        self.pushButton_checkable_current_row.setText(QCoreApplication.translate("Form_List", u"\u5141\u8bb8\u52fe\u9009", None))
        self.pushButton_uncheckable_current_row.setText(QCoreApplication.translate("Form_List", u"\u4e0d\u5141\u8bb8\u52fe\u9009", None))
        self.pushButton_moveToTop.setText(QCoreApplication.translate("Form_List", u"\u79fb\u81f3\u9876\u90e8", None))
        self.pushButton_moveUp.setText(QCoreApplication.translate("Form_List", u"\u4e0a\u79fb", None))
        self.pushButton_moveDown.setText(QCoreApplication.translate("Form_List", u"\u4e0b\u79fb", None))
        self.pushButton_moveToBottom.setText(QCoreApplication.translate("Form_List", u"\u79fb\u81f3\u5e95\u90e8", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form_List", u"\u589e", None))
        self.pushButton_add.setText(QCoreApplication.translate("Form_List", u"\u589e\u52a0", None))
        self.pushButton_add_s.setText(QCoreApplication.translate("Form_List", u"\u589e\u52a0\u591a\u4e2a", None))
        self.pushButton_insert.setText(QCoreApplication.translate("Form_List", u"\u63d2\u5165", None))
        self.pushButton_insert_s.setText(QCoreApplication.translate("Form_List", u"\u63d2\u5165\u591a\u4e2a", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form_List", u"\u5185\u5bb9\u5339\u914d\u89c4\u5219", None))
        self.radioButton_equal.setText(QCoreApplication.translate("Form_List", u"\u7cbe\u786e\u5339\u914d", None))
        self.radioButton_include.setText(QCoreApplication.translate("Form_List", u"\u5305\u542b*", None))
        self.radioButton_start_with.setText(QCoreApplication.translate("Form_List", u"\u4ee5*\u5f00\u5934", None))
        self.radioButton_end_with.setText(QCoreApplication.translate("Form_List", u"\u4ee5*\u7ed3\u5c3e", None))
        self.radioButton_ignore_capltals.setText(QCoreApplication.translate("Form_List", u"\u5ffd\u7565\u5927\u5c0f\u5199", None))
        self.radioButton_regular_expression.setText(QCoreApplication.translate("Form_List", u"\u6b63\u5219\u5339\u914d", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form_List", u"\u5220", None))
        self.label_remove_by_position_result.setText(QCoreApplication.translate("Form_List", u"\u4f9d\u4f4d\u7f6e\u5220\u9664 \u5220\u9664\u7ed3\u679c", None))
        self.pushButton_remove_by_position.setText(QCoreApplication.translate("Form_List", u"\u5220\u9664", None))
        self.label_remove_by_content_result.setText(QCoreApplication.translate("Form_List", u"\u4f9d\u5185\u5bb9\u5220\u9664 \u5220\u9664\u7ed3\u679c", None))
        self.pushButton_remove_by_content.setText(QCoreApplication.translate("Form_List", u"\u5185\u5bb9\u5339\u914d\u5220\u9664", None))
        self.pushButton_clear.setText(QCoreApplication.translate("Form_List", u"\u6e05\u7a7a\u5168\u90e8", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Form_List", u"\u6539", None))
        self.label_modify_by_position_result.setText(QCoreApplication.translate("Form_List", u"\u4f9d\u4f4d\u7f6e\u4fee\u6539 \u4fee\u6539\u7ed3\u679c", None))
        self.pushButton_modify.setText(QCoreApplication.translate("Form_List", u"\u4f9d\u4f4d\u7f6e\u4fee\u6539", None))
        self.label_replace_by_content_result.setText(QCoreApplication.translate("Form_List", u"\u4f9d\u5185\u5bb9\u66ff\u6362 \u66ff\u6362\u7ed3\u679c", None))
        self.pushButton_replace.setText(QCoreApplication.translate("Form_List", u"\u5185\u5bb9\u5339\u914d\u66ff\u6362", None))
        self.label_change_position_result.setText(QCoreApplication.translate("Form_List", u"\u4f9d\u4f4d\u7f6e\u4ea4\u6362 \u4ea4\u6362\u7ed3\u679c", None))
        self.pushButton_change_position.setText(QCoreApplication.translate("Form_List", u"\u4f9d\u4f4d\u7f6e\u4ea4\u6362", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Form_List", u"\u67e5", None))
        self.label_find_by_position_result.setText(QCoreApplication.translate("Form_List", u"\u4f9d\u4f4d\u7f6e\u67e5\u627e \u67e5\u627e\u7ed3\u679c", None))
        self.pushButton_find_by_position.setText(QCoreApplication.translate("Form_List", u"\u4f9d\u4f4d\u7f6e\u67e5\u627e", None))
        self.label_find_by_content_result.setText(QCoreApplication.translate("Form_List", u"\u4f9d\u5185\u5bb9\u67e5\u627e \u67e5\u627e\u7ed3\u679c", None))
        self.pushButton_find_by_content.setText(QCoreApplication.translate("Form_List", u"\u4f9d\u5185\u5bb9\u67e5\u627e", None))
        self.pushButton_find_match.setText(QCoreApplication.translate("Form_List", u"\u5185\u5bb9\u5339\u914d\u67e5\u627e", None))
        self.plainTextEdit_find_include.setPlainText(QCoreApplication.translate("Form_List", u"\u4f9d\u5185\u5bb9\u67e5\u627e \u5339\u914d\u7ed3\u679c", None))
    # retranslateUi

