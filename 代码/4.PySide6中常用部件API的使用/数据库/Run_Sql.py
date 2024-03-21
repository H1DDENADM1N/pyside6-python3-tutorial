from Ui_Sql import Ui_Sql

from PySide6.QtWidgets import ( QApplication, QWidget,
                                QTableView, QHeaderView, QCompleter)

from PySide6.QtGui import QAction, QDesktopServices

from PySide6.QtCore import (    Qt, QUrl,
                                QSortFilterProxyModel, QStringListModel)

from PySide6.QtSql import ( QSqlDatabase,  # 连接数据库
                            QSqlQueryModel,  # 只读
                            QSqlTableModel)  # 可读写

import re
from pypinyin import lazy_pinyin

import os

# 切换到当前文件的目录
os.chdir(os.path.dirname(__file__))


# 自定义代理模型，按拼音排序，数据一多非常卡
class PinyinSortFilterProxyModel(QSortFilterProxyModel):
    def lessThan(self, left, right):
        left_data = self.sourceModel().data(left)
        right_data = self.sourceModel().data(right)

        # 获取拼音
        left_pinyin = ''.join(lazy_pinyin(left_data))
        right_pinyin = ''.join(lazy_pinyin(right_data))

        # 比较拼音
        return left_pinyin < right_pinyin



class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Sql()
        self.ui.setupUi(self)
        self.ui.pushButton_add.setText('0 序号 index 格式错误')
        self.ui.pushButton_add.setEnabled(False)
        self.ui.pushButton_remove.setText('0 序号 index 格式错误')
        self.ui.pushButton_remove.setEnabled(False)
        self.connect_db()  # 连接数据库
        self.setup_model()  # 设置模型
        self.setup_view()  # 设置视图
        # 设置控制
        self.setup_signals()
        self.setup_context_menu()


    '''
    -----------------------------------------------------------------------------------------------------------------------------------
    设置模型  Model
    -----------------------------------------------------------------------------------------------------------------------------------
    '''

    # 连接数据库
    def connect_db(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("./test.db")
        if not db.open():
            raise Exception("数据库打开失败")

    # 设置模型
    def setup_model(self):

        # 只读
        # self.model = QSqlQueryModel()
        # self.model.setQuery("select * from user")  # 从 user 表取全部数据
        # self.model.setQuery("select * from user_with_pinyin")  # 从 user_with_pinyin 表取全部数据

        # 可读写
        self.model = QSqlTableModel()
        # self.model.setTable("user")  # 指定 user 表
        self.model.setTable("user_with_pinyin")  # 指定 user_with_pinyin 表
        self.model.select()
        # 调用fetchMore()直到没有更多的数据可以加载
        # while self.model.canFetchMore():
        #     self.model.fetchMore()

        self.setup_proxy_model()
        self.setup_string_list_model()

    # 创建代理模型，保持源模型的纯净和可重用性
    def setup_proxy_model(self):

        # 使用默认代理模型，但使用 add_PinYin_Col_for_test.db_.py 预处理数据库，生成 拼音 列
        self.sort_filter_proxy_model = QSortFilterProxyModel()
        
        # 创建自定义代理模型，按拼音排序，数据一多非常卡
        # self.sort_filter_proxy_model = PinyinSortFilterProxyModel()

        self.sort_filter_proxy_model.setSourceModel(self.model)
        # 设置代理模型过滤检查范围
        self.sort_filter_proxy_model.setFilterKeyColumn(-1)     # 设置过滤的关键列，-1表示所有列都将被用于过滤检查
        
        # 设置 代理模型 表头
        # for i, letter in enumerate(['序号 index', '姓名 name', '地址 address', '邮箱 email']):
        
        for i, letter in enumerate(['0 序号 index', '1 姓名 name', '2 地址 address', '3 邮箱 email', '4 姓名拼音']):
            self.sort_filter_proxy_model.setHeaderData(i, Qt.Horizontal, letter)

    # 创建字符串列表模型
    def setup_string_list_model(self):
        self.string_list_model = QStringListModel()
        # 设置补全器
        self.completer = QCompleter(self.string_list_model, self)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)  # 设置不区分大小写
        # 将 QCompleter 设置到 QLineEdit
        self.ui.lineEdit_data_filter.setCompleter(self.completer)


    '''
    -----------------------------------------------------------------------------------------------------------------------------------
    设置视图  View
    -----------------------------------------------------------------------------------------------------------------------------------
    '''

    # 设置视图
    def setup_view(self):
        # 指定模型，使用代理模型，保持源模型的纯净和可重用性
        self.ui.tableView.setModel(self.sort_filter_proxy_model)
        
        # 禁止编辑
        # self.ui.tableView.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        # 选择整行
        self.ui.tableView.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        # 手动调整列宽
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        # 允许排序
        self.ui.tableView.setSortingEnabled(True)
        # 单元格合并
        # self.ui.tableView.setSpan(0, 0, 3, 2)
        # 设置默认按姓名拼音列排序
        self.sort_filter_proxy_model.sort(4)



    '''
    -----------------------------------------------------------------------------------------------------------------------------------
    设置控制  Controller
    -----------------------------------------------------------------------------------------------------------------------------------
    '''

    # 连接信号/槽
    def setup_signals(self):
        # 查
        self.ui.lineEdit_data_filter.textChanged.connect(self.use_filter)
        self.ui.lineEdit_filter_range.textChanged.connect(self.set_filter_range)
        # 增 & 改
        self.ui.pushButton_add.clicked.connect(self.add_data)
        self.ui.lineEdit_add_index.textChanged.connect(lambda: self.check_add_index(self.ui.lineEdit_add_index.text()))
        # 删
        self.ui.pushButton_remove.clicked.connect(self.remove_data)
        self.ui.lineEdit_remove_index.textChanged.connect(lambda: self.check_remove_index(self.ui.lineEdit_remove_index.text()))
        # 输出选中项
        self.ui.pushButton_print_selected.clicked.connect(self.print_selected)

    def use_filter(self):
        text = self.ui.lineEdit_data_filter.text()
        try:
            # 尝试编译正则表达式来检查语法
            re.compile(text)
            # 如果编译成功，设置代理模型的过滤规则，使用 正则表达式 进行搜索 过滤
            self.sort_filter_proxy_model.setFilterRegularExpression(text)
            self.ui.label_data_filter.setText("数据过滤")  # 清除错误信息
            # 添加过滤结果到字符串列表模型补全器
            text_list = []
            # 遍历代理模型的所有行和列
            for row in range(self.sort_filter_proxy_model.rowCount()):
                for column in range(self.sort_filter_proxy_model.columnCount()):
                    # 获取模型索引
                    index = self.sort_filter_proxy_model.index(row, column)
                    # 获取单元格数据
                    data = self.sort_filter_proxy_model.data(index)
                    # 将数据添加到文本列表
                    text_list.append(data)

            self.string_list_model.setStringList(text_list)
        except re.error as e:
            # 如果编译失败，显示错误信息
            self.ui.label_data_filter.setText(f"正则表达式错误: {e}")

    def set_filter_range(self):
        # 获取需要过滤的列
        text = self.ui.lineEdit_filter_range.text()
        list = text.split(",")
        # 设置过滤规则
        for col in list:
            try:
                col = int(col.strip())
                self.sort_filter_proxy_model.setFilterKeyColumn(col)
            except ValueError:
                self.ui.label_filter_range.setText("过滤适用范围（列）设置内容格式错误")
                return
        self.ui.label_filter_range.setText("过滤适用范围（列）")

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
        self.ui.tableView.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.ui.tableView.addAction(self.copy_current_item)
        self.copy_current_item.triggered.connect(self.copy_current_item_function)
        # 删除
        self.delete_current_item = QAction('删除')
        self.ui.tableView.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.ui.tableView.addAction(self.delete_current_item)
        self.delete_current_item.triggered.connect(self.delete_current_item_function)

    # 增
    def add_data(self):
        index = int(self.ui.lineEdit_add_index.text())
        name = self.ui.lineEdit_add_name.text()
        address = self.ui.lineEdit_add_address.text()
        email = self.ui.lineEdit_add_email.text()
        name_pinyin = self.ui.lineEdit_add_name_pinyin.text()

        # 加载全部数据，避免增加数据重复
        while self.model.canFetchMore():
            self.model.fetchMore()

        # 检查索引是否已存在，存在则为修改数据
        exist_index = set()
        for i in range(self.model.rowCount()):
            exist_index.add(self.model.index(i, 0).data())
        if index in exist_index:
            self.ui.pushButton_add.setText("索引已存在，执行修改数据")
            self.modify_data(index, name, address, email, name_pinyin)
            return

        self.model.insertRow(index)
        self.model.setData(self.model.index(index, 0), index)
        self.model.setData(self.model.index(index, 1), name)
        self.model.setData(self.model.index(index, 2), address)
        self.model.setData(self.model.index(index, 3), email)
        self.model.setData(self.model.index(index, 4), name_pinyin)
        if not self.model.submitAll():
            self.ui.pushButton_add.setText("提交失败: " + self.model.lastError().text())
        else:
            # 通知代理模型更新
            self.sort_filter_proxy_model.invalidateFilter()

    # 改
    def modify_data(self, index, name, address, email, name_pinyin):
        # 找到正确的行号
        row = -1
        for i in range(self.model.rowCount()):
            if self.model.index(i, 0).data() == index:
                row = i
                break

        if row != -1:
            self.model.setData(self.model.index(row, 1), name)
            self.model.setData(self.model.index(row, 2), address)
            self.model.setData(self.model.index(row, 3), email)
            self.model.setData(self.model.index(row, 4), name_pinyin)
            if not self.model.submitAll():
                self.ui.pushButton_modify.setText("提交失败: " + self.model.lastError().text())
            else:
                # 通知代理模型更新
                self.sort_filter_proxy_model.invalidateFilter()



    # 删
    def remove_data(self):
        index_to_remove = self.ui.lineEdit_remove_index.text()
        try:
            index_to_remove = int(index_to_remove)  # 将字符串转换为整数
        except ValueError:
            self.ui.pushButton_remove.setText("输入的索引不是有效的数字")
            self.ui.pushButton_remove.setEnabled(False)
            return

        row_to_remove = None
        for i in range(self.model.rowCount()):
            if self.model.index(i, 0).data() == index_to_remove:
                row_to_remove = i
                break  # 找到匹配的行后立即中断循环

        if row_to_remove is not None:
            self.model.removeRow(row_to_remove)
            if not self.model.submitAll():
                self.ui.pushButton_remove.setText("提交失败: " + self.model.lastError().text())
            else:
                # 更新视图
                self.sort_filter_proxy_model.invalidateFilter()
        else:
            self.ui.pushButton_remove.setText("没有找到匹配的索引")


    def check_add_index(self, index):
        # index 防非数字
        try:
            int(index)
            self.ui.pushButton_add.setText("新增数据")
            self.ui.pushButton_add.setEnabled(True)
        except ValueError:
            self.ui.pushButton_add.setText("0 序号 index 格式错误")
            self.ui.pushButton_add.setEnabled(False)


    def check_remove_index(self, index):
        # index 防非数字
        try:
            int(index)
            self.ui.pushButton_remove.setText("删除数据")
            self.ui.pushButton_remove.setEnabled(True)
        except ValueError:
            self.ui.pushButton_remove.setText("0 序号 index 格式错误")
            self.ui.pushButton_remove.setEnabled(False)


    '''
    -----------------------------------------------------------------------------------------------------------------------------------
    当前项
    -----------------------------------------------------------------------------------------------------------------------------------
    '''

    # 复制当前项
    def copy_current_item_function(self):
        # 获取选中的单元格的索引
        selected_indexes = self.ui.tableView.selectedIndexes()
        if not selected_indexes:
            return  # 如果没有选中任何单元格，直接返回

        # 获取选中区域的起始和结束行
        start_row = selected_indexes[0].row()
        end_row = selected_indexes[-1].row()
        # 使用列表推导式按行组织文本
        rows_data = []
        for row in range(start_row, end_row + 1):
            # 获取当前行的所有选中单元格的文本
            row_items = [self.ui.tableView.model().index(row, col).data() for col in range(self.ui.tableView.model().columnCount()) if self.ui.tableView.model().index(row, col) in selected_indexes]
            # 将选中单元格的文本连接成字符串
            row_text = ' '.join(map(str, row_items))
            # 将当前行的文本添加到结果列表中
            rows_data.append(row_text)
        # 将最终的文本连接起来，并添加到剪贴板
        QApplication.clipboard().setText('\n'.join(rows_data))



    # 删除当前项
    def delete_current_item_function(self):
        # 获取选中的索引
        selected_indexes = self.ui.tableView.selectedIndexes()
        
        # 创建一个列表来存储选中项第0列的数据
        remove_target_list = []

        # 遍历选中的索引
        for index in selected_indexes:
            # 检查列号是否为0
            if index.column() == 0:
                # 获取数据
                data = self.ui.tableView.model().data(index)
                # 添加到列表中
                remove_target_list.append(data)
        # 遍历列表
        for row_to_remove in remove_target_list:
            for i in range(self.model.rowCount()):
                if self.model.index(i, 0).data() == row_to_remove:
                    self.model.removeRow(i)
                    if not self.model.submitAll():
                        self.ui.pushButton_remove.setText("提交失败: " + self.model.lastError().text())
                    else:
                        # 更新视图
                        print(f"{i} 删除成功")
                        self.sort_filter_proxy_model.invalidateFilter()



    # 输出选中项
    def print_selected(self):
        # 获取选中的索引
        selected_indexes = self.ui.tableView.selectedIndexes()
        
        # 如果没有选中的索引，则设置文本为空
        if not selected_indexes:
            self.ui.plainTextEdit_print_selected.setPlainText("没有选中的项")
            return

        # 创建一个列表来存储选中的数据
        selected_data = []

        # 遍历选中的索引
        for index in selected_indexes:
            # 获取行号和列号
            row = index.row()
            column = index.column()
            # 获取数据
            data = self.ui.tableView.model().data(index)
            # 添加到列表中
            selected_data.append([row, column, data])

        # 将列表转换为文本
        text = '\n'.join(map(str, selected_data))
        # 设置文本到控件中
        self.ui.plainTextEdit_print_selected.setPlainText(text)



if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
