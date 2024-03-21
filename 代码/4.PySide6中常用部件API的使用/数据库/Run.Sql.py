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
        self.ui.lineEdit_data_filter.textChanged.connect(self.use_filter)
        self.ui.lineEdit_filter_range.textChanged.connect(self.set_filter_range)

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




if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
