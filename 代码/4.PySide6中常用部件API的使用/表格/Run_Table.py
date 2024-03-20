from Ui_Table import Ui_Table

from PySide6.QtWidgets import ( QApplication, QWidget,
                                QTableWidgetItem, QHeaderView)
from PySide6.QtGui import QAction, QDesktopServices, QColor
from PySide6.QtCore import Qt, QUrl
import re
import math

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Table()
        self.ui.setupUi(self)

        # 初始无查找结果高亮项
        self.highlighted_items = []
        # 默认不分页
        self.ui.pushButton_prev_page.setDisabled(True)
        self.ui.pushButton_next_page.setDisabled(True)
        self.ui.pushButton_split_page.setDisabled(True)
        self.ui.spinBox_every_page_row_number.setDisabled(True)
        self.current_page = 0
        self.total_page = 0
        self.page_size = int(self.ui.spinBox_every_page_row_number.text())
        self.data = []

        self.setup_context_menu()
        self.setup_signals()

    # 设置上下文菜单
    def setup_context_menu(self):
        # 给窗体添加上下文菜单
        self.about = QAction('了解更多')
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.addAction(self.about)
        self.about.triggered.connect(lambda: QDesktopServices.openUrl(QUrl("https://github.com/H1DDENADM1N/pyside6-python3-tutorial")))
        # 给控件添加上下文菜单
        # 复制
        self.copy_current_item = QAction('复制')
        self.ui.tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.ui.tableWidget.addAction(self.copy_current_item)
        self.copy_current_item.triggered.connect(self.copy_current_item_function)
        # 删除
        self.delete_current_item = QAction('删除')
        self.ui.tableWidget.addAction(self.delete_current_item)
        self.delete_current_item.triggered.connect(self.delete_current_item_function)
        

    # 连接信号/槽
    def setup_signals(self):
        # 设置表格
        self.ui.pushButton_set_row_count.clicked.connect(self.set_row_count)
        self.ui.pushButton_set_col_count.clicked.connect(self.set_col_count)
        self.ui.pushButton_set_header.clicked.connect(self.set_header)
        self.ui.pushButton_set_header_resize.clicked.connect(self.set_header_resize)
        self.ui.checkBox_sortable.stateChanged.connect(self.set_sortable)
        self.ui.pushButton_span.clicked.connect(self.set_span)

        # 增 & 改
        self.ui.pushButton_add_item.clicked.connect(self.add_item)
        self.ui.pushButton_background_color.clicked.connect(self.set_background_color)
        self.ui.pushButton_foreground_color.clicked.connect(self.set_foreground_color)
        self.ui.pushButton_add_A1_to_Z26.clicked.connect(self.add_A1_to_Z26)
        self.ui.pushButton_add_1_to_million.clicked.connect(self.add_1_to_million)
        # 删
        self.ui.pushButton_remove.clicked.connect(self.remove_item)
        # 查
        self.ui.pushButton_find_match.clicked.connect(self.find_match)
        # 当前项
        self.ui.tableWidget.cellClicked.connect(self.cell_clicked)  # 传递 row 和 col
        # self.ui.tableWidget.itemClicked.connect(self.item_clicked)  # 传递 item
        # 输出选中项
        self.ui.pushButton_print_selected.clicked.connect(self.print_selected)
        # 分页
        self.ui.checkBox_split_page.stateChanged.connect(self.set_split_page)
        self.ui.pushButton_prev_page.clicked.connect(self.prev_page)
        self.ui.pushButton_next_page.clicked.connect(self.next_page)
        self.ui.pushButton_next_page.clicked.connect(self.next_page)
        self.ui.pushButton_split_page.clicked.connect(self.set_split_page)


    '''
    -----------------------------------------------------------------------------------------------------------------------------------
    设置表格
    -----------------------------------------------------------------------------------------------------------------------------------
    '''

    # 行数
    def set_row_count(self):
        row = self.ui.spinBox_set_row_count.value()
        self.ui.tableWidget.setRowCount(row)

    # 列数
    def set_col_count(self):
        col = self.ui.spinBox_set_col_count.value()
        self.ui.tableWidget.setColumnCount(col)

    # 表头
    def set_header(self):
        text = self.ui.lineEdit_set_header.text()
        list = text.split(",")
        self.ui.tableWidget.setHorizontalHeaderLabels(list)

    # 列宽
    def set_header_resize(self):
        if self.ui.radioButton_interactive.isChecked():
            self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)  # 手动调整列宽
        elif self.ui.radioButton_fixed.isChecked():
            self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)  # 固定值列宽
            resize_header_value = self.ui.spinBox_resize_header_value.value()
            for col in range(self.ui.tableWidget.columnCount()):
                self.ui.tableWidget.horizontalHeader().resizeSection(col, resize_header_value)
        elif self.ui.radioButton_stretch.isChecked():
            self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 自动调整列宽-伸展
        elif self.ui.radioButton_resize_to_contents.isChecked():
            self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  # 自动调整列宽-调整到内容大小

    # 可否排序
    def set_sortable(self):
        if self.ui.checkBox_sortable.isChecked():
            self.ui.tableWidget.setSortingEnabled(True)
        else:
            self.ui.tableWidget.setSortingEnabled(False)

    # 合并单元格
    def set_span(self):
        row = self.ui.spinBox_span_row.text()  # 行
        col = self.ui.spinBox_span_col.text()  # 列
        rowSpan = self.ui.spinBox_span_rowspan.text()  # 占几行
        colSpan = self.ui.spinBox_span_colspan.text()  # 占几列
        self.ui.tableWidget.setSpan(int(row), int(col), int(rowSpan), int(colSpan))  # 行、列、占几行、占几列

    # 分页
    def set_split_page(self):
        # 如果分页复选框被选中
        if self.ui.checkBox_split_page.isChecked():
            # 启用上一页和下一页的按钮
            self.ui.pushButton_prev_page.setDisabled(False)
            self.ui.pushButton_next_page.setDisabled(False)
            # 启用分页按钮
            self.ui.pushButton_split_page.setDisabled(False)
            # 启用每页行数的设置框
            self.ui.spinBox_every_page_row_number.setDisabled(False)
            # 获取用户设定的每页行数
            self.page_size = int(self.ui.spinBox_every_page_row_number.text())
            # 更新表格数据
            self.update_table()
            # 更新当前页码和总页码的显示
            self.ui.label_current_page.setText(f"{str(self.current_page + 1)} / {str(self.total_page)}")
        else:
            # 如果分页复选框未被选中，禁用分页功能相关控件
            self.ui.pushButton_prev_page.setDisabled(True)
            self.ui.pushButton_next_page.setDisabled(True)
            self.ui.pushButton_split_page.setDisabled(True)
            self.ui.spinBox_every_page_row_number.setDisabled(True)
            # 更新当前页码和总页码的显示
            self.ui.label_current_page.setText(f"分页已停用")
            # 恢复分页前表格
            self.restore_table()

    # 更新分页后表格
    def update_table(self):
        # 计算当前页数据在数据集中的起始和结束索引
        start = self.current_page * self.page_size
        end = start + self.page_size
        # 计算总页数，使用向上取整确保能显示所有数据
        self.total_page = math.ceil(len(self.data) / self.page_size)
        # 获取当前页需要显示的数据
        page_data = self.data[start:end]
        # 设置表格的行数为当前页数据的数量
        self.ui.tableWidget.setRowCount(len(page_data))
        # 设置数据
        for rowIndex, row in enumerate(page_data):
            for colIndex, col in enumerate(row):
                if isinstance(col, str):
                    # col 是字符串
                    self.ui.tableWidget.setItem(rowIndex, colIndex, QTableWidgetItem(col))
                else:
                    # col 不是字符串
                    self.ui.tableWidget.setItem(rowIndex, colIndex, QTableWidgetItem(str(col)))

    # 恢复分页前表格
    def restore_table(self):
        # 设置表格的行数为数据集的数量
        self.ui.tableWidget.setRowCount(len(self.data))
        # 设置数据
        for rowIndex, row in enumerate(self.data):
            for colIndex, col in enumerate(row):
                if isinstance(col, str):
                    # col 是字符串
                    self.ui.tableWidget.setItem(rowIndex, colIndex, QTableWidgetItem(col))
                else:
                    # col 不是字符串
                    self.ui.tableWidget.setItem(rowIndex, colIndex, QTableWidgetItem(str(col)))

    # 上一页
    def prev_page(self):
        # 如果当前页不是第一页，则减少当前页码
        if self.current_page > 0:
            self.current_page -= 1
            # 更新表格显示
            self.update_table()
        # 更新页码显示
        self.ui.label_current_page.setText(f"{str(self.current_page + 1)} / {str(self.total_page)}")

    # 下一页
    def next_page(self):
        # 如果当前页不是最后一页，则增加当前页码
        if self.current_page+1 < self.total_page:
            self.current_page += 1
            # 更新表格显示
            self.update_table()
        # 更新页码显示
        self.ui.label_current_page.setText(f"{str(self.current_page + 1)} / {str(self.total_page)}")



    '''
    -----------------------------------------------------------------------------------------------------------------------------------
    增
    -----------------------------------------------------------------------------------------------------------------------------------
    '''

    # 增加一个元素
    def add_item(self):
        row = self.ui.spinBox_add_item_row.value()
        col = self.ui.spinBox_add_item_col.value()
        text = self.ui.lineEdit_add_item_content.text()
        item = QTableWidgetItem(text)
        self.ui.tableWidget.setItem(row, col, item)
        # self.ui.tableWidget.item(row, col).setText(text)  # 方法 二

    # 背景色
    def set_background_color(self):
        row = self.ui.spinBox_add_item_row.value()
        col = self.ui.spinBox_add_item_col.value()
        color = self.ui.lineEdit_background_color.text()
        self.ui.tableWidget.item(row, col).setBackground(QColor(color))

    # 前景色
    def set_foreground_color(self):
        row = self.ui.spinBox_add_item_row.value()
        col = self.ui.spinBox_add_item_col.value()
        color = self.ui.lineEdit_foreground_color.text()
        self.ui.tableWidget.item(row, col).setForeground(QColor(color))

    # 为表格增加初始值 A1-Z26
    def add_A1_to_Z26(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(26)
        self.ui.tableWidget.setColumnCount(26)
        # 设置数据
        self.data = [[col_letter + str(row_number) for col_letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'] for row_number in range(1, 27)]
        for rowIndex, row in enumerate(self.data):
            for colIndex, col in enumerate(row):
                if isinstance(col, str):
                    # col 是字符串
                    self.ui.tableWidget.setItem(rowIndex, colIndex, QTableWidgetItem(col))
                else:
                    # col 不是字符串
                    self.ui.tableWidget.setItem(rowIndex, colIndex, QTableWidgetItem(str(col)))
        # 设置表头
        self.ui.tableWidget.setHorizontalHeaderLabels([letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])
        # 重置搜索高亮列表
        self.highlight_list = []

    # # 为表格增加初始值 1-百万
    def add_1_to_million(self):
        self.ui.tableWidget.clear()
        # self.ui.tableWidget.setRowCount(20000)
        self.ui.tableWidget.setColumnCount(5)
        # 设置数据
        self.data = [list(range(1 + 5*i, 1 + 5*i + 5)) for i in range(1000000//5)]
        for rowIndex, row in enumerate(self.data):
            for colIndex, col in enumerate(row):
                if isinstance(col, str):
                    # col 是字符串
                    self.ui.tableWidget.setItem(rowIndex, colIndex, QTableWidgetItem(col))
                else:
                    # col 不是字符串
                    self.ui.tableWidget.setItem(rowIndex, colIndex, QTableWidgetItem(str(col)))
        # 启用分页
        self.ui.checkBox_split_page.setChecked(True)
        # 设置分页
        self.set_split_page()


    '''
    -----------------------------------------------------------------------------------------------------------------------------------
    删
    -----------------------------------------------------------------------------------------------------------------------------------
    '''

    # 删除一个元素
    def remove_item(self):
        row = self.ui.spinBox_remove_row.value()
        col = self.ui.spinBox_remove_col.value()
        self.ui.tableWidget.takeItem(row, col)


    '''
    -----------------------------------------------------------------------------------------------------------------------------------
    改
    -----------------------------------------------------------------------------------------------------------------------------------
    '''




    '''
    -----------------------------------------------------------------------------------------------------------------------------------
    查
    -----------------------------------------------------------------------------------------------------------------------------------
    '''

    # 查找匹配项
    def find_match(self):
        text = self.ui.lineEdit_find_match.text()
        if self.ui.radioButton_equal.isChecked():  # 精确匹配
            items = self.ui.tableWidget.findItems(text, Qt.MatchFlag.MatchExactly)
        elif self.ui.radioButton_include.isChecked():  # 模糊匹配 包含*
            items = self.ui.tableWidget.findItems(text, Qt.MatchFlag.MatchContains | Qt.MatchFlag.MatchCaseSensitive) # 大小写敏感
        elif self.ui.radioButton_start_with.isChecked():  # 模糊匹配 以*开头
            items = self.ui.tableWidget.findItems(text, Qt.MatchFlag.MatchStartsWith)
        elif self.ui.radioButton_end_with.isChecked():  # 模糊匹配 以*结尾
            items = self.ui.tableWidget.findItems(text, Qt.MatchFlag.MatchEndsWith)
        elif self.ui.radioButton_ignore_capltals.isChecked():  # 模糊匹配 忽略大小写
            items = self.ui.tableWidget.findItems(text, Qt.MatchFlag.MatchContains)
        elif self.ui.radioButton_regular_expression.isChecked():  # 正则匹配
            try:
                # 尝试编译正则表达式来检查语法
                re.compile(text)
                # 如果编译成功，设置索引规则
                items = self.ui.tableWidget.findItems(text, Qt.MatchFlag.MatchRegularExpression)
            except re.error as e:
                # 如果编译失败，显示错误信息
                self.ui.plainTextEdit_find_match.setPlainText(f"正则表达式{text}语法错误{e}")
                return
        result_list = [[index, item.column(), item.text()] for index, item in enumerate(items)]
        if result_list:
            self.ui.plainTextEdit_find_match.setPlainText('\n'.join(map(str, result_list)))
            # 高亮结果
            if self.ui.checkBox_highlight_find_result.isChecked():
                # 复原已高亮项
                if self.highlighted_items:
                    try:
                        for item in self.highlighted_items:
                            item.setBackground(QColor("#FFFFFF"))
                        self.highlighted_items = []
                    except Exception:
                        pass
                # 高亮查找结果
                for item in items:
                    item.setBackground(QColor("#FF0000"))
                self.highlighted_items = items
            else:
                # 复原已高亮项
                if self.highlighted_items:
                    try:
                        for item in self.highlighted_items:
                            item.setBackground(QColor("#FFFFFF"))
                        self.highlighted_items = []
                    except Exception:
                        pass
            # 跳转到结果
            if self.ui.checkBox_scroll_to_find_match.isChecked():
                self.ui.tableWidget.scrollToItem(items[0])  # 必须用信号触发

        else:
            self.ui.plainTextEdit_find_match.setPlainText('没有找到匹配项')


    '''
    -----------------------------------------------------------------------------------------------------------------------------------
    当前项
    -----------------------------------------------------------------------------------------------------------------------------------
    '''

    # 单元格呗点击
    def cell_clicked(self, row, col):
        try:
            text = self.ui.tableWidget.item(row, col).text()
        except Exception:
            text = ''
        self.ui.label_current_item.setText(f"当前项：第{row}行，第{col}列，内容为{text}")

    # 元素被点击
    def item_clicked(self, item):
        self.ui.label_current_item.setText(f"当前项：第{item.row()}行，第{item.column()}列，内容为{item.text()}")

    # 输出 所选项
    def print_selected(self):
        selected_data = [[item.row(), item.column(), item.text()] for item in self.ui.tableWidget.selectedItems()]
        self.ui.plainTextEdit_print_selected.setPlainText('\n'.join(map(str, selected_data)))

    def copy_current_item_function(self):
        # 获取选中的单元格
        selected_items = self.ui.tableWidget.selectedItems()
        # 获取选中区域的起始和结束行
        start_row = selected_items[0].row()
        end_row = selected_items[-1].row()
        # 使用列表推导式按行组织文本
        rows_data = []
        for row in range(start_row, end_row + 1):
            # 获取当前行的所有选中单元格
            row_items = [self.ui.tableWidget.item(row, col) for col in range(self.ui.tableWidget.columnCount()) if self.ui.tableWidget.item(row, col) and self.ui.tableWidget.item(row, col).isSelected()]
            # 将选中单元格的文本提取出来并连接成字符串
            row_text = ' '.join(item.text() for item in row_items)
            # 将当前行的文本添加到结果列表中
            rows_data.append(row_text)
        # 将最终的文本连接起来，并添加到剪贴板
        QApplication.clipboard().setText('\n'.join(rows_data))

    def delete_current_item_function(self):
        # 获取选中的单元格
        selected_items = self.ui.tableWidget.selectedItems()
        for item in selected_items:
            self.ui.tableWidget.takeItem(item.row(), item.column())

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
