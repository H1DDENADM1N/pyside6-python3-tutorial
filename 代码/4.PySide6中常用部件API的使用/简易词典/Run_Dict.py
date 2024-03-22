from Ui_Dict import Ui_Dict
from PySide6.QtWidgets import QApplication, QWidget, QTableView, QHeaderView
from PySide6.QtGui import QAction, QDesktopServices
from PySide6.QtCore import Qt, QUrl, QSortFilterProxyModel
from PySide6.QtSql import ( QSqlDatabase, QSqlQueryModel)
import os


# 切换到当前文件的目录
os.chdir(os.path.dirname(__file__))


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dict()
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
        db.setDatabaseName("./stardict.db")
        if not db.open():
            raise Exception("数据库打开失败")

    # 设置模型
    def setup_model(self):
        self.model = QSqlQueryModel()
        # self.model.setQuery("select id, word, sw, phonetic, definition, translation from stardict")
        self.model.setQuery("select id, word, translation from stardict")
        self.setup_proxy_model()

    # 创建代理模型，保持源模型的纯净和可重用性
    def setup_proxy_model(self):
        self.sort_filter_proxy_model = QSortFilterProxyModel()
        self.sort_filter_proxy_model.setSourceModel(self.model)
        # 设置代理模型过滤检查范围
        self.sort_filter_proxy_model.setFilterKeyColumn(-1)     # 设置过滤的关键列，-1表示所有列都将被用于过滤检查
        # 设置 代理模型 表头
        # for i, letter in enumerate(['0 序号 id', '1 单词 word', '2 单词（无空格） sw', '3 音标 phonetic', '4 定义 definition', '5 翻译 translation']):
        for i, letter in enumerate(['0 序号 id', '1 单词 word', '2 翻译 translation']):
            self.sort_filter_proxy_model.setHeaderData(i, Qt.Horizontal, letter)


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
        # 自动调整列宽-调整到内容大小
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # 允许排序
        self.ui.tableView.setSortingEnabled(True)



    '''
    -----------------------------------------------------------------------------------------------------------------------------------
    设置控制  Controller
    -----------------------------------------------------------------------------------------------------------------------------------
    '''

    # 连接信号/槽
    def setup_signals(self):
        # 查
        self.ui.lineEdit_en2cn.textChanged.connect(self.en2cn)
        self.ui.lineEdit_cn2en.textChanged.connect(self.cn2en)

    def en2cn(self):
        self.ui.lineEdit_cn2en.clear()
        text = self.ui.lineEdit_en2cn.text()
        if text:
            sql_query = f"select id, word, translation from stardict where word like '%{text}%' or sw like '%{text}%'"
            self.model.setQuery(sql_query)
        
    def cn2en(self):
        self.ui.lineEdit_en2cn.clear()
        text = self.ui.lineEdit_cn2en.text()
        if text:
            sql_query = f"select id, word, translation from stardict where translation like '%{text}%' or sw like '%{text}%'"
            self.model.setQuery(sql_query)


    '''
    -----------------------------------------------------------------------------------------------------------------------------------
    当前项
    -----------------------------------------------------------------------------------------------------------------------------------
    '''

    # 设置上下文菜单
    def setup_context_menu(self):
        # 给窗体添加上下文菜单
        self.about = QAction('了解更多')
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.addAction(self.about)
        self.about.triggered.connect(lambda: QDesktopServices.openUrl(QUrl("https://github.com/H1DDENADM1N/pyside6-python3-tutorial")))
        # 给控件添加上下文菜单
        # 复制英文
        self.copy_current_en = QAction('复制英文')
        self.ui.tableView.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.ui.tableView.addAction(self.copy_current_en)
        self.copy_current_en.triggered.connect(self.copy_en_function)
        # 复制中文
        self.copy_current_cn = QAction('复制中文')
        self.ui.tableView.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.ui.tableView.addAction(self.copy_current_cn)
        self.copy_current_cn.triggered.connect(self.copy_cn_function)
        # 复制全部
        self.copy_all = QAction('复制全部')
        self.ui.tableView.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.ui.tableView.addAction(self.copy_all)
        self.copy_all.triggered.connect(self.copy_all_function)

    def copy_en_function(self):
        # 获取选中的单元格的索引
        selected_indexes = self.ui.tableView.selectedIndexes()
        if not selected_indexes:
            return  # 如果没有选中任何单元格，直接返回
        # 获取选中区域的起始和结束行
        start_row = selected_indexes[0].row()
        end_row = selected_indexes[-1].row()
        # 使用列表推导式按行组织文本，只获取第一列的数据
        rows_data = []
        for row in range(start_row, end_row + 1):
            # 获取当前行的第一列的单元格文本
            row_text = self.ui.tableView.model().index(row, 1).data()
            # 将当前行的文本添加到结果列表中
            rows_data.append(row_text)
        # 将最终的文本连接起来，并添加到剪贴板
        QApplication.clipboard().setText('\n'.join(rows_data))

    def copy_cn_function(self):
        # 获取选中的单元格的索引
        selected_indexes = self.ui.tableView.selectedIndexes()
        if not selected_indexes:
            return  # 如果没有选中任何单元格，直接返回
        # 获取选中区域的起始和结束行
        start_row = selected_indexes[0].row()
        end_row = selected_indexes[-1].row()
        # 使用列表推导式按行组织文本，只获取第一列的数据
        rows_data = []
        for row in range(start_row, end_row + 1):
            # 获取当前行的第二列的单元格文本
            row_text = self.ui.tableView.model().index(row, 2).data()
            # 将当前行的文本添加到结果列表中
            rows_data.append(row_text)
        # 将最终的文本连接起来，并添加到剪贴板
        QApplication.clipboard().setText('\n'.join(rows_data))

    def copy_all_function(self):
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




if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
