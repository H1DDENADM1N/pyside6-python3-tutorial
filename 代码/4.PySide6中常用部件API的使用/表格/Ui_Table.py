# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Table.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Table(object):
    def setupUi(self, Table):
        if not Table.objectName():
            Table.setObjectName(u"Table")
        Table.resize(643, 699)
        self.verticalLayout_11 = QVBoxLayout(Table)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_title = QLabel(Table)
        self.label_title.setObjectName(u"label_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.label_title)

        self.label_current_item = QLabel(Table)
        self.label_current_item.setObjectName(u"label_current_item")

        self.horizontalLayout_11.addWidget(self.label_current_item)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.tableWidget = QTableWidget(Table)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)

        self.horizontalLayout_17.addWidget(self.tableWidget)

        self.groupBox_4 = QGroupBox(Table)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_print_selected = QPushButton(self.groupBox_4)
        self.pushButton_print_selected.setObjectName(u"pushButton_print_selected")

        self.verticalLayout_7.addWidget(self.pushButton_print_selected)

        self.plainTextEdit_print_selected = QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit_print_selected.setObjectName(u"plainTextEdit_print_selected")

        self.verticalLayout_7.addWidget(self.plainTextEdit_print_selected)


        self.horizontalLayout_17.addWidget(self.groupBox_4)


        self.verticalLayout_11.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.groupBox_2 = QGroupBox(Table)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.spinBox_set_row_count = QSpinBox(self.groupBox_2)
        self.spinBox_set_row_count.setObjectName(u"spinBox_set_row_count")

        self.horizontalLayout_2.addWidget(self.spinBox_set_row_count)

        self.pushButton_set_row_count = QPushButton(self.groupBox_2)
        self.pushButton_set_row_count.setObjectName(u"pushButton_set_row_count")

        self.horizontalLayout_2.addWidget(self.pushButton_set_row_count)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.spinBox_set_col_count = QSpinBox(self.groupBox_2)
        self.spinBox_set_col_count.setObjectName(u"spinBox_set_col_count")

        self.horizontalLayout_3.addWidget(self.spinBox_set_col_count)

        self.pushButton_set_col_count = QPushButton(self.groupBox_2)
        self.pushButton_set_col_count.setObjectName(u"pushButton_set_col_count")

        self.horizontalLayout_3.addWidget(self.pushButton_set_col_count)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_set_header = QLineEdit(self.groupBox_2)
        self.lineEdit_set_header.setObjectName(u"lineEdit_set_header")

        self.horizontalLayout_4.addWidget(self.lineEdit_set_header)

        self.pushButton_set_header = QPushButton(self.groupBox_2)
        self.pushButton_set_header.setObjectName(u"pushButton_set_header")

        self.horizontalLayout_4.addWidget(self.pushButton_set_header)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.radioButton_interactive = QRadioButton(self.groupBox_2)
        self.buttonGroup = QButtonGroup(Table)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_interactive)
        self.radioButton_interactive.setObjectName(u"radioButton_interactive")
        self.radioButton_interactive.setChecked(True)

        self.verticalLayout_3.addWidget(self.radioButton_interactive)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.radioButton_fixed = QRadioButton(self.groupBox_2)
        self.buttonGroup.addButton(self.radioButton_fixed)
        self.radioButton_fixed.setObjectName(u"radioButton_fixed")

        self.horizontalLayout_6.addWidget(self.radioButton_fixed)

        self.spinBox_resize_header_value = QSpinBox(self.groupBox_2)
        self.spinBox_resize_header_value.setObjectName(u"spinBox_resize_header_value")
        self.spinBox_resize_header_value.setMaximum(200)
        self.spinBox_resize_header_value.setValue(50)

        self.horizontalLayout_6.addWidget(self.spinBox_resize_header_value)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.radioButton_stretch = QRadioButton(self.groupBox_2)
        self.buttonGroup.addButton(self.radioButton_stretch)
        self.radioButton_stretch.setObjectName(u"radioButton_stretch")
        self.radioButton_stretch.setChecked(False)

        self.verticalLayout_3.addWidget(self.radioButton_stretch)

        self.radioButton_resize_to_contents = QRadioButton(self.groupBox_2)
        self.buttonGroup.addButton(self.radioButton_resize_to_contents)
        self.radioButton_resize_to_contents.setObjectName(u"radioButton_resize_to_contents")

        self.verticalLayout_3.addWidget(self.radioButton_resize_to_contents)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.pushButton_set_header_resize = QPushButton(self.groupBox_2)
        self.pushButton_set_header_resize.setObjectName(u"pushButton_set_header_resize")

        self.horizontalLayout_5.addWidget(self.pushButton_set_header_resize)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.checkBox_sortable = QCheckBox(self.groupBox_3)
        self.checkBox_sortable.setObjectName(u"checkBox_sortable")

        self.horizontalLayout_10.addWidget(self.checkBox_sortable)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_8 = QGroupBox(self.groupBox_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_5)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.spinBox_span_colspan = QSpinBox(self.groupBox_8)
        self.spinBox_span_colspan.setObjectName(u"spinBox_span_colspan")
        self.spinBox_span_colspan.setMinimum(1)
        self.spinBox_span_colspan.setMaximum(999)

        self.gridLayout.addWidget(self.spinBox_span_colspan, 0, 2, 1, 1)

        self.spinBox_span_col = QSpinBox(self.groupBox_8)
        self.spinBox_span_col.setObjectName(u"spinBox_span_col")
        self.spinBox_span_col.setMaximum(999)

        self.gridLayout.addWidget(self.spinBox_span_col, 0, 1, 1, 1)

        self.spinBox_span_row = QSpinBox(self.groupBox_8)
        self.spinBox_span_row.setObjectName(u"spinBox_span_row")
        self.spinBox_span_row.setMaximum(999)

        self.gridLayout.addWidget(self.spinBox_span_row, 0, 0, 1, 1)

        self.spinBox_span_rowspan = QSpinBox(self.groupBox_8)
        self.spinBox_span_rowspan.setObjectName(u"spinBox_span_rowspan")
        self.spinBox_span_rowspan.setMinimum(1)
        self.spinBox_span_rowspan.setMaximum(999)

        self.gridLayout.addWidget(self.spinBox_span_rowspan, 1, 0, 1, 1)


        self.horizontalLayout_14.addLayout(self.gridLayout)

        self.pushButton_span = QPushButton(self.groupBox_8)
        self.pushButton_span.setObjectName(u"pushButton_span")

        self.horizontalLayout_14.addWidget(self.pushButton_span)


        self.verticalLayout_10.addLayout(self.horizontalLayout_14)


        self.verticalLayout_2.addWidget(self.groupBox_8)

        self.groupBox_10 = QGroupBox(self.groupBox_2)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.checkBox_split_page = QCheckBox(self.groupBox_10)
        self.checkBox_split_page.setObjectName(u"checkBox_split_page")

        self.horizontalLayout_18.addWidget(self.checkBox_split_page)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_6)

        self.label = QLabel(self.groupBox_10)
        self.label.setObjectName(u"label")

        self.horizontalLayout_18.addWidget(self.label)

        self.spinBox_every_page_row_number = QSpinBox(self.groupBox_10)
        self.spinBox_every_page_row_number.setObjectName(u"spinBox_every_page_row_number")
        self.spinBox_every_page_row_number.setMinimum(5)
        self.spinBox_every_page_row_number.setMaximum(1000)
        self.spinBox_every_page_row_number.setValue(20)

        self.horizontalLayout_18.addWidget(self.spinBox_every_page_row_number)

        self.pushButton_split_page = QPushButton(self.groupBox_10)
        self.pushButton_split_page.setObjectName(u"pushButton_split_page")

        self.horizontalLayout_18.addWidget(self.pushButton_split_page)


        self.verticalLayout_6.addLayout(self.horizontalLayout_18)

        self.label_current_page = QLabel(self.groupBox_10)
        self.label_current_page.setObjectName(u"label_current_page")

        self.verticalLayout_6.addWidget(self.label_current_page)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushButton_prev_page = QPushButton(self.groupBox_10)
        self.pushButton_prev_page.setObjectName(u"pushButton_prev_page")

        self.horizontalLayout_19.addWidget(self.pushButton_prev_page)

        self.pushButton_next_page = QPushButton(self.groupBox_10)
        self.pushButton_next_page.setObjectName(u"pushButton_next_page")

        self.horizontalLayout_19.addWidget(self.pushButton_next_page)


        self.verticalLayout_6.addLayout(self.horizontalLayout_19)


        self.verticalLayout_2.addWidget(self.groupBox_10)


        self.horizontalLayout_16.addWidget(self.groupBox_2)

        self.line_3 = QFrame(Table)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_16.addWidget(self.line_3)

        self.groupBox_9 = QGroupBox(Table)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox = QGroupBox(self.groupBox_9)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.spinBox_add_item_row = QSpinBox(self.groupBox)
        self.spinBox_add_item_row.setObjectName(u"spinBox_add_item_row")

        self.horizontalLayout.addWidget(self.spinBox_add_item_row)

        self.spinBox_add_item_col = QSpinBox(self.groupBox)
        self.spinBox_add_item_col.setObjectName(u"spinBox_add_item_col")

        self.horizontalLayout.addWidget(self.spinBox_add_item_col)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEdit_add_item_content = QLineEdit(self.groupBox)
        self.lineEdit_add_item_content.setObjectName(u"lineEdit_add_item_content")

        self.horizontalLayout_7.addWidget(self.lineEdit_add_item_content)

        self.pushButton_add_item = QPushButton(self.groupBox)
        self.pushButton_add_item.setObjectName(u"pushButton_add_item")

        self.horizontalLayout_7.addWidget(self.pushButton_add_item)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit_background_color = QLineEdit(self.groupBox)
        self.lineEdit_background_color.setObjectName(u"lineEdit_background_color")

        self.horizontalLayout_8.addWidget(self.lineEdit_background_color)

        self.pushButton_background_color = QPushButton(self.groupBox)
        self.pushButton_background_color.setObjectName(u"pushButton_background_color")

        self.horizontalLayout_8.addWidget(self.pushButton_background_color)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lineEdit_foreground_color = QLineEdit(self.groupBox)
        self.lineEdit_foreground_color.setObjectName(u"lineEdit_foreground_color")

        self.horizontalLayout_9.addWidget(self.lineEdit_foreground_color)

        self.pushButton_foreground_color = QPushButton(self.groupBox)
        self.pushButton_foreground_color.setObjectName(u"pushButton_foreground_color")

        self.horizontalLayout_9.addWidget(self.pushButton_foreground_color)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton_add_A1_to_Z26 = QPushButton(self.groupBox)
        self.pushButton_add_A1_to_Z26.setObjectName(u"pushButton_add_A1_to_Z26")

        self.verticalLayout.addWidget(self.pushButton_add_A1_to_Z26)

        self.pushButton_add_1_to_million = QPushButton(self.groupBox)
        self.pushButton_add_1_to_million.setObjectName(u"pushButton_add_1_to_million")

        self.verticalLayout.addWidget(self.pushButton_add_1_to_million)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.line = QFrame(self.groupBox_9)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.groupBox_7 = QGroupBox(self.groupBox_9)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.spinBox_remove_row = QSpinBox(self.groupBox_7)
        self.spinBox_remove_row.setObjectName(u"spinBox_remove_row")

        self.horizontalLayout_13.addWidget(self.spinBox_remove_row)

        self.spinBox_remove_col = QSpinBox(self.groupBox_7)
        self.spinBox_remove_col.setObjectName(u"spinBox_remove_col")

        self.horizontalLayout_13.addWidget(self.spinBox_remove_col)

        self.pushButton_remove = QPushButton(self.groupBox_7)
        self.pushButton_remove.setObjectName(u"pushButton_remove")

        self.horizontalLayout_13.addWidget(self.pushButton_remove)


        self.verticalLayout_9.addLayout(self.horizontalLayout_13)


        self.verticalLayout_5.addWidget(self.groupBox_7)

        self.line_2 = QFrame(self.groupBox_9)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_2)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.groupBox_6 = QGroupBox(self.groupBox_9)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.radioButton_equal = QRadioButton(self.groupBox_6)
        self.radioButton_equal.setObjectName(u"radioButton_equal")
        self.radioButton_equal.setChecked(True)

        self.verticalLayout_12.addWidget(self.radioButton_equal)

        self.radioButton_include = QRadioButton(self.groupBox_6)
        self.radioButton_include.setObjectName(u"radioButton_include")

        self.verticalLayout_12.addWidget(self.radioButton_include)

        self.radioButton_start_with = QRadioButton(self.groupBox_6)
        self.radioButton_start_with.setObjectName(u"radioButton_start_with")

        self.verticalLayout_12.addWidget(self.radioButton_start_with)

        self.radioButton_end_with = QRadioButton(self.groupBox_6)
        self.radioButton_end_with.setObjectName(u"radioButton_end_with")

        self.verticalLayout_12.addWidget(self.radioButton_end_with)

        self.radioButton_ignore_capltals = QRadioButton(self.groupBox_6)
        self.radioButton_ignore_capltals.setObjectName(u"radioButton_ignore_capltals")

        self.verticalLayout_12.addWidget(self.radioButton_ignore_capltals)

        self.radioButton_regular_expression = QRadioButton(self.groupBox_6)
        self.radioButton_regular_expression.setObjectName(u"radioButton_regular_expression")

        self.verticalLayout_12.addWidget(self.radioButton_regular_expression)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)


        self.horizontalLayout_15.addWidget(self.groupBox_6)

        self.groupBox_5 = QGroupBox(self.groupBox_9)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lineEdit_find_match = QLineEdit(self.groupBox_5)
        self.lineEdit_find_match.setObjectName(u"lineEdit_find_match")

        self.horizontalLayout_12.addWidget(self.lineEdit_find_match)

        self.pushButton_find_match = QPushButton(self.groupBox_5)
        self.pushButton_find_match.setObjectName(u"pushButton_find_match")

        self.horizontalLayout_12.addWidget(self.pushButton_find_match)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.checkBox_highlight_find_result = QCheckBox(self.groupBox_5)
        self.checkBox_highlight_find_result.setObjectName(u"checkBox_highlight_find_result")
        self.checkBox_highlight_find_result.setChecked(True)

        self.verticalLayout_8.addWidget(self.checkBox_highlight_find_result)

        self.checkBox_scroll_to_find_match = QCheckBox(self.groupBox_5)
        self.checkBox_scroll_to_find_match.setObjectName(u"checkBox_scroll_to_find_match")
        self.checkBox_scroll_to_find_match.setChecked(True)

        self.verticalLayout_8.addWidget(self.checkBox_scroll_to_find_match)

        self.plainTextEdit_find_match = QPlainTextEdit(self.groupBox_5)
        self.plainTextEdit_find_match.setObjectName(u"plainTextEdit_find_match")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.plainTextEdit_find_match.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_find_match.setSizePolicy(sizePolicy2)

        self.verticalLayout_8.addWidget(self.plainTextEdit_find_match)


        self.horizontalLayout_15.addWidget(self.groupBox_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_16.addWidget(self.groupBox_9)


        self.verticalLayout_11.addLayout(self.horizontalLayout_16)


        self.retranslateUi(Table)

        QMetaObject.connectSlotsByName(Table)
    # setupUi

    def retranslateUi(self, Table):
        Table.setWindowTitle(QCoreApplication.translate("Table", u"Table", None))
        self.label_title.setText(QCoreApplication.translate("Table", u"\u8868\u683c", None))
        self.label_current_item.setText(QCoreApplication.translate("Table", u"\u5f53\u524d\u9879", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Table", u"col0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Table", u"col1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Table", u"col2", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Table", u"row0", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Table", u"row1", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Table", u"row2", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Table", u"A1", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Table", u"B1", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Table", u"C1", None));
        ___qtablewidgetitem9 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Table", u"A2", None));
        ___qtablewidgetitem10 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Table", u"B2", None));
        ___qtablewidgetitem11 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Table", u"C2", None));
        ___qtablewidgetitem12 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Table", u"A3", None));
        ___qtablewidgetitem13 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Table", u"B3", None));
        ___qtablewidgetitem14 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Table", u"C3", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox_4.setTitle(QCoreApplication.translate("Table", u"\u8f93\u51fa\u9009\u4e2d\u9879", None))
        self.pushButton_print_selected.setText(QCoreApplication.translate("Table", u"\u8f93\u51fa\u9009\u4e2d\u9879", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Table", u"\u8bbe\u7f6e\u8868\u683c", None))
        self.pushButton_set_row_count.setText(QCoreApplication.translate("Table", u"\u8bbe\u7f6e\u884c\u6570", None))
        self.pushButton_set_col_count.setText(QCoreApplication.translate("Table", u"\u8bbe\u7f6e\u5217\u6570", None))
        self.lineEdit_set_header.setPlaceholderText(QCoreApplication.translate("Table", u"\u8868\u59341,\u8868\u59342,\u8868\u59343...", None))
        self.pushButton_set_header.setText(QCoreApplication.translate("Table", u"\u8bbe\u7f6e\u8868\u5934\u6807\u7b7e", None))
        self.radioButton_interactive.setText(QCoreApplication.translate("Table", u"\u624b\u52a8\u8c03\u6574\u5217\u5bbd", None))
        self.radioButton_fixed.setText(QCoreApplication.translate("Table", u"\u56fa\u5b9a\u503c\u5217\u5bbd", None))
        self.radioButton_stretch.setText(QCoreApplication.translate("Table", u"\u81ea\u52a8\u8c03\u6574\u5217\u5bbd-\u4f38\u5c55", None))
        self.radioButton_resize_to_contents.setText(QCoreApplication.translate("Table", u"\u81ea\u52a8\u8c03\u6574\u5217\u5bbd-\u8c03\u6574\u5230\u5185\u5bb9\u5927\u5c0f", None))
        self.pushButton_set_header_resize.setText(QCoreApplication.translate("Table", u"\u8bbe\u7f6e\u5217\u5bbd", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Table", u"\u6392\u5e8f", None))
        self.checkBox_sortable.setText(QCoreApplication.translate("Table", u"\u5141\u8bb8\u6392\u5e8f", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Table", u"\u5408\u5e76\u5355\u5143\u683c", None))
        self.pushButton_span.setText(QCoreApplication.translate("Table", u"\u5408\u5e76", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("Table", u"\u5206\u9875", None))
        self.checkBox_split_page.setText(QCoreApplication.translate("Table", u"\u5141\u8bb8\u5206\u9875", None))
        self.label.setText(QCoreApplication.translate("Table", u"\u6bcf\u9875\u884c\u6570\uff1a", None))
        self.pushButton_split_page.setText(QCoreApplication.translate("Table", u"\u5206\u9875", None))
        self.label_current_page.setText(QCoreApplication.translate("Table", u"\u5f53\u524d\u9875\u7801\uff1a", None))
        self.pushButton_prev_page.setText(QCoreApplication.translate("Table", u"\u4e0a\u4e00\u9875", None))
        self.pushButton_next_page.setText(QCoreApplication.translate("Table", u"\u4e0b\u4e00\u9875", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Table", u"\u8bbe\u7f6e\u6570\u636e", None))
        self.groupBox.setTitle(QCoreApplication.translate("Table", u"\u589e && \u6539", None))
        self.pushButton_add_item.setText(QCoreApplication.translate("Table", u"\u8d4b\u503c", None))
        self.lineEdit_background_color.setText(QCoreApplication.translate("Table", u"#00B294", None))
        self.pushButton_background_color.setText(QCoreApplication.translate("Table", u"\u80cc\u666f\u8272", None))
        self.lineEdit_foreground_color.setText(QCoreApplication.translate("Table", u"#FF0000", None))
        self.pushButton_foreground_color.setText(QCoreApplication.translate("Table", u"\u524d\u666f\u8272", None))
        self.pushButton_add_A1_to_Z26.setText(QCoreApplication.translate("Table", u"\u521d\u59cb\u503c\uff0cA1-Z26", None))
        self.pushButton_add_1_to_million.setText(QCoreApplication.translate("Table", u"\u521d\u59cb\u503c\uff0c1-1,000,000", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Table", u"\u5220", None))
        self.pushButton_remove.setText(QCoreApplication.translate("Table", u"\u5220\u9664", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Table", u"\u5185\u5bb9\u5339\u914d\u89c4\u5219", None))
        self.radioButton_equal.setText(QCoreApplication.translate("Table", u"\u7cbe\u786e\u5339\u914d", None))
        self.radioButton_include.setText(QCoreApplication.translate("Table", u"\u5305\u542b*", None))
        self.radioButton_start_with.setText(QCoreApplication.translate("Table", u"\u4ee5*\u5f00\u5934", None))
        self.radioButton_end_with.setText(QCoreApplication.translate("Table", u"\u4ee5*\u7ed3\u5c3e", None))
        self.radioButton_ignore_capltals.setText(QCoreApplication.translate("Table", u"\u5ffd\u7565\u5927\u5c0f\u5199", None))
        self.radioButton_regular_expression.setText(QCoreApplication.translate("Table", u"\u6b63\u5219\u5339\u914d", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Table", u"\u67e5", None))
        self.pushButton_find_match.setText(QCoreApplication.translate("Table", u"\u5185\u5bb9\u5339\u914d\u67e5\u627e", None))
        self.checkBox_highlight_find_result.setText(QCoreApplication.translate("Table", u"\u6807\u7ea2\u67e5\u627e\u7ed3\u679c", None))
        self.checkBox_scroll_to_find_match.setText(QCoreApplication.translate("Table", u"\u81ea\u52a8\u8df3\u8f6c\u5230\u67e5\u627e\u7ed3\u679c", None))
        self.plainTextEdit_find_match.setPlainText(QCoreApplication.translate("Table", u"\u4f9d\u5185\u5bb9\u67e5\u627e \u5339\u914d\u7ed3\u679c", None))
    # retranslateUi

