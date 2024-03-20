from Ui_TableView import Ui_TableView

from PySide6.QtWidgets import ( QApplication, QWidget,
                                QTableView, QHeaderView, QCompleter)
from PySide6.QtGui import ( QAction, QDesktopServices,
                            QStandardItemModel, QStandardItem)
from PySide6.QtCore import (    Qt, QUrl,
                                QSortFilterProxyModel, QStringListModel)
import re

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TableView()
        self.ui.setupUi(self)
        # 设置模型
        self.setup_model()
        # 设置视图
        self.setup_view()
        # 设置控制
        self.setup_signals()
        self.setup_context_menu()

    '''
    -----------------------------------------------------------------------------------------------------------------------------------
    设置模型  Model
    -----------------------------------------------------------------------------------------------------------------------------------
    '''

    # 设置模型
    def setup_model(self):
        # 创建模型
        self.model = QStandardItemModel()
        # 设置数据 A1-Z26
        self.data = [[col_letter + str(row_number) for col_letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'] for row_number in range(1, 27)]
        for rowIndex, row in enumerate(self.data):
            for colIndex, col in enumerate(row):
                self.model.setItem(rowIndex, colIndex, QStandardItem(col))
        # 设置 原模型 表头
        # self.model.setHorizontalHeaderLabels([letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])
        self.setup_proxy_model()
        self.setup_string_list_model()

    # 创建代理模型，保持源模型的纯净和可重用性
    def setup_proxy_model(self):
        self.sort_filter_proxy_model = QSortFilterProxyModel()
        self.sort_filter_proxy_model.setSourceModel(self.model)
        # 设置代理模型过滤检查范围
        self.sort_filter_proxy_model.setFilterKeyColumn(-1)     # 设置过滤的关键列，-1表示所有列都将被用于过滤检查
        # 设置 代理模型 表头
        for i, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
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
        self.ui.tableView.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        # 选择整行
        self.ui.tableView.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        # 手动调整列宽
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        # 允许排序
        self.ui.tableView.setSortingEnabled(True)
        # 单元格合并
        self.ui.tableView.setSpan(0, 0, 3, 2)


    '''
    -----------------------------------------------------------------------------------------------------------------------------------
    设置控制  Controller
    -----------------------------------------------------------------------------------------------------------------------------------
    '''

    # 连接信号/槽
    def setup_signals(self):
        self.ui.lineEdit_data_filter.textChanged.connect(self.use_filter)

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
