from Ui_List import Ui_Form_List

from PySide6.QtWidgets import ( QApplication, QWidget,
                                QListWidgetItem)
from PySide6.QtGui import QAction, QDesktopServices
from PySide6.QtCore import Qt, QUrl
import re

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_List()
        self.ui.setupUi(self)
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
        self.ui.listWidget_List.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.ui.listWidget_List.addAction(self.copy_current_item)
        self.copy_current_item.triggered.connect(lambda: QApplication.clipboard().setText(self.ui.listWidget_List.currentItem().text()))
        # 删除
        self.delete_current_row = QAction('删除')
        self.ui.listWidget_List.addAction(self.delete_current_row)
        self.delete_current_row.triggered.connect(lambda: self.ui.listWidget_List.takeItem(self.ui.listWidget_List.currentRow()))
        # 允许勾选
        self.checkable_current_row = QAction('允许勾选')
        self.ui.listWidget_List.addAction(self.checkable_current_row)
        self.checkable_current_row.triggered.connect(self.checkable_current_row_function)
        # 不允许勾选
        self.uncheckable_current_row = QAction('不允许勾选')
        self.ui.listWidget_List.addAction(self.uncheckable_current_row)
        self.uncheckable_current_row.triggered.connect(self.uncheckable_current_row_function)
        # 上移
        self.moveUp_current_row = QAction('上移')
        self.ui.listWidget_List.addAction(self.moveUp_current_row)
        self.moveUp_current_row.triggered.connect(self.moveUp_current_row_function)
        # 下移
        self.moveDown_current_row = QAction('下移')
        self.ui.listWidget_List.addAction(self.moveDown_current_row)
        self.moveDown_current_row.triggered.connect(self.moveDown_current_row_function)
        # 移至顶部
        self.moveToTop_current_row = QAction('移至顶部')
        self.ui.listWidget_List.addAction(self.moveToTop_current_row)
        self.moveToTop_current_row.triggered.connect(self.moveToTop_current_row_function)
        # 移至顶部
        self.moveToBottom_current_row = QAction('移至底部')
        self.ui.listWidget_List.addAction(self.moveToBottom_current_row)
        self.moveToBottom_current_row.triggered.connect(self.moveToBottom_current_row_function)

    # 连接信号/槽
    def setup_signals(self):
        # 排序
        self.ui.pushButton_sort.clicked.connect(self.sort_list)
        # 输出
        self.ui.pushButton_print_all.clicked.connect(self.print_all)
        # 控制选中项
        # 复制
        self.ui.pushButton_copy_current_item.clicked.connect(lambda: QApplication.clipboard().setText(self.ui.listWidget_List.currentItem().text()))
        # 删除
        self.ui.pushButton_delete_current_row.clicked.connect(lambda: self.ui.listWidget_List.takeItem(self.ui.listWidget_List.currentRow()))
        # 允许勾选
        self.ui.pushButton_checkable_current_row.clicked.connect(self.checkable_current_row_function)
        # 不允许勾选
        self.ui.pushButton_uncheckable_current_row.clicked.connect(self.uncheckable_current_row_function)
        # 上移
        self.ui.pushButton_moveUp.clicked.connect(self.moveUp_current_row_function)
        # 下移
        self.ui.pushButton_moveDown.clicked.connect(self.moveDown_current_row_function)
        # 移至顶部
        self.ui.pushButton_moveToTop.clicked.connect(self.moveToTop_current_row_function)
        # 移至底部
        self.ui.pushButton_moveToBottom.clicked.connect(self.moveToBottom_current_row_function)
        # 增
        self.ui.pushButton_add.clicked.connect(self.add_item)
        self.ui.pushButton_add_s.clicked.connect(self.add_item_s)
        self.ui.pushButton_insert.clicked.connect(self.insert_item)
        self.ui.pushButton_insert_s.clicked.connect(self.insert_item_s)
        # 删
        self.ui.pushButton_remove_by_position.clicked.connect(self.remove_by_position)
        self.ui.pushButton_remove_by_content.clicked.connect(self.remove_by_content)
        self.ui.pushButton_clear.clicked.connect(self.clear_list)
        # 改
        self.ui.pushButton_modify.clicked.connect(self.modify_item)
        self.ui.pushButton_replace.clicked.connect(self.replace_item)
        self.ui.pushButton_change_position.clicked.connect(self.change_position)
        # 查
        self.ui.pushButton_find_by_position.clicked.connect(self.find_by_position)
        self.ui.pushButton_find_by_content.clicked.connect(self.find_by_content)
        self.ui.pushButton_find_match.clicked.connect(self.find_match)
        # 当前项
        self.ui.listWidget_List.currentItemChanged.connect(self.current_item_changed)
        # 勾选状态
        self.ui.listWidget_List.itemChanged.connect(self.item_changed)


    # 排序
    def sort_list(self):
        if self.ui.radioButton_ascending_order.isChecked():  # 升序
            self.ui.listWidget_List.sortItems(Qt.SortOrder.AscendingOrder)
        elif self.ui.radioButton_descending_order.isChecked():  # 降序
            self.ui.listWidget_List.sortItems(Qt.SortOrder.DescendingOrder)
        elif self.ui.radioButton_max_order.isChecked():  # 大数优先
            self.customSortOrderMax()
        elif self.ui.radioButton_min_order.isChecked():  # 小数优先
            self.customSortOrderMin()

    # 大数优先
    def customSortOrderMax(self):
        # 初始化三个列表，分别用于整数、小数和字符串
        int_list = []
        float_list = []
        string_list = []
        # 遍历 QListWidget 中的所有项
        for i in range(self.ui.listWidget_List.count()):
            # 获取每一项
            item = self.ui.listWidget_List.item(i)
            if item is not None:
                # 尝试将项的文本转换为整数
                try:
                    number = int(item.text())
                    # 如果成功，添加到整数列表
                    int_list.append(number)
                except ValueError:
                    # 如果转换失败，尝试将项的文本转换为小数
                    try:
                        number = float(item.text())
                        # 如果成功，添加到小数列表
                        float_list.append(number)
                    except ValueError:
                        # 如果转换失败，添加到字符串列表
                        string_list.append(item.text())
        # 对整数列表进行从大到小排序
        sorted_int_list = sorted(int_list, reverse=True)
        # 对小数列表进行从大到小排序
        sorted_float_list = sorted(float_list, reverse=True)
        # 合并排序后的整数列表和小数列表
        merged_number_list = sorted_int_list + sorted_float_list
        # 对合并后的列表进行从大到小排序
        sorted_merged_number_list = sorted(merged_number_list, reverse=True)
        # 对字符串列表进行排序
        sorted_string_list = sorted(string_list, reverse=True, key=lambda s: s.lower())
        # 将字符串列表添加到合并后的数字列表末尾
        merged_list = sorted_merged_number_list + sorted_string_list
        # 清空 QListWidget
        self.ui.listWidget_List.clear()
        # 将合并后的列表转换为字符串，并添加到 QListWidget 中
        [self.ui.listWidget_List.addItem(str(item)) for item in merged_list]

    # 小数优先
    def customSortOrderMin(self):
        # 初始化三个列表，分别用于整数、小数和字符串
        int_list = []
        float_list = []
        string_list = []
        # 遍历 QListWidget 中的所有项
        for i in range(self.ui.listWidget_List.count()):
            # 获取每一项
            item = self.ui.listWidget_List.item(i)
            if item is not None:
                # 尝试将项的文本转换为整数
                try:
                    number = int(item.text())
                    # 如果成功，添加到整数列表
                    int_list.append(number)
                except ValueError:
                    # 如果转换失败，尝试将项的文本转换为小数
                    try:
                        number = float(item.text())
                        # 如果成功，添加到小数列表
                        float_list.append(number)
                    except ValueError:
                        # 如果转换失败，添加到字符串列表
                        string_list.append(item.text())
        # 对整数列表进行从小到大排序
        sorted_int_list = sorted(int_list, reverse=False)
        # 对小数列表进行从小到大排序
        sorted_float_list = sorted(float_list, reverse=False)
        # 合并排序后的整数列表和小数列表
        merged_number_list = sorted_int_list + sorted_float_list
        # 对合并后的列表进行从小到大排序
        sorted_merged_number_list = sorted(merged_number_list, reverse=False)
        # 对字符串列表进行排序
        sorted_string_list = sorted(string_list, reverse=False, key=lambda s: s.lower())
        # 将字符串列表添加到合并后的数字列表末尾
        merged_list = sorted_merged_number_list + sorted_string_list
        # 清空 QListWidget
        self.ui.listWidget_List.clear()
        # 将合并后的列表转换为字符串，并添加到 QListWidget 中
        [self.ui.listWidget_List.addItem(str(item)) for item in merged_list]

    # 输出全部
    def print_all(self):
        self.ui.plainTextEdit_print_all.clear()
        for i in range(self.ui.listWidget_List.count()):
            self.ui.plainTextEdit_print_all.appendPlainText(f"{i} : {self.ui.listWidget_List.item(i).text()}")

    '''
    -----------------------------------------------------------------------------------------------------------------------------------
    增
    -----------------------------------------------------------------------------------------------------------------------------------
    '''

    # 增加一个元素
    def add_item(self):
        text = self.ui.lineEdit_add.text()
        item = QListWidgetItem(text)
        self.ui.listWidget_List.addItem(item)  # 增加一个元素

    # 增加多个元素
    def add_item_s(self):
        text = self.ui.plainTextEdit_add_s.toPlainText()
        items = text.split('\n')  # 分割文本为多个元素
        self.ui.listWidget_List.addItems(items)  # 增加多个元素

    # 插入一个元素
    def insert_item(self):
        text = self.ui.lineEdit_insert.text()
        item = QListWidgetItem(text)
        position = self.ui.spinBox_insert_position.value()
        if position >= 0 and position < self.ui.listWidget_List.count():
            self.ui.listWidget_List.insertItem(position, item)  # 插入一个元素
        elif position >= self.ui.listWidget_List.count():
            self.ui.listWidget_List.addItem(item)  # 添加一个元素
        else:
            self.ui.lineEdit_insert.setText("插入范围错误")

    # 插入多个元素
    def insert_item_s(self):
        text = self.ui.plainTextEdit_insert_s.toPlainText()
        items = text.split('\n')  # 分割文本为多个元素
        position = self.ui.spinBox_insert_s_position.value()
        if position >= 0 and position < self.ui.listWidget_List.count():
            self.ui.listWidget_List.insertItems(position, items)  # 插入多个元素
        elif position >= self.ui.listWidget_List.count():
            self.ui.listWidget_List.addItems(items)  # 添加多个元素
        else:
            self.ui.lineEdit_insert.setText("插入范围错误")

    '''
    -----------------------------------------------------------------------------------------------------------------------------------
    删
    -----------------------------------------------------------------------------------------------------------------------------------
    '''

    # 依位置删除
    def remove_by_position(self):
        position = self.ui.spinBox_remove_by_position.value()
        if position >= 0 and position < self.ui.listWidget_List.count():
            self.ui.listWidget_List.takeItem(position)  # 删除一个元素
            self.ui.label_remove_by_position_result.setText(f"删除第{position}项成功")
        else:
            self.ui.label_remove_by_position_result.setText("删除范围错误")

    # 依内容删除
    def remove_by_content(self):
        text = self.ui.lineEdit_remove_by_content.text()
        # 收集所有要删除的项的索引
        if self.ui.radioButton_equal.isChecked():  # 精确匹配
            targets = [i for i in range(self.ui.listWidget_List.count()) if self.ui.listWidget_List.item(i).text() == text]
            removed_list =[]
            # 从后向前删除，避免迭代时索引变化
            for i in reversed(targets):
                self.ui.listWidget_List.takeItem(i)  # 删除所有内容为 text 的元素
                removed_list.append(i)
            self.ui.label_remove_by_content_result.setText(f"删除内容为{text}的项成功，删除项索引为{removed_list}")
        elif self.ui.radioButton_include.isChecked():  # 模糊匹配 包含*
            targets = [i for i in range(self.ui.listWidget_List.count()) if text in self.ui.listWidget_List.item(i).text()]
            removed_list =[]
            # 从后向前删除，避免迭代时索引变化
            for i in reversed(targets):
                self.ui.listWidget_List.takeItem(i)  # 删除所有内容包含 text 的元素
                removed_list.append(i)
            self.ui.label_remove_by_content_result.setText(f"删除内容包含{text}的项成功，删除项索引为{removed_list}")
        elif self.ui.radioButton_start_with.isChecked():  # 模糊匹配 以*开头
            targets = [i for i in range(self.ui.listWidget_List.count()) if self.ui.listWidget_List.item(i).text().startswith(text)]
            removed_list =[]
            # 从后向前删除，避免迭代时索引变化
            for i in reversed(targets):
                self.ui.listWidget_List.takeItem(i)  # 删除所有内容以 text 开头
                removed_list.append(i)
            self.ui.label_remove_by_content_result.setText(f"删除内容以{text}开头的项成功，删除项索引为{removed_list}")
        elif self.ui.radioButton_end_with.isChecked():  # 模糊匹配 以*结尾
            targets = [i for i in range(self.ui.listWidget_List.count()) if self.ui.listWidget_List.item(i).text().endswith(text)]
            removed_list =[]
            # 从后向前删除，避免迭代时索引变化
            for i in reversed(targets):
                self.ui.listWidget_List.takeItem(i)  # 删除所有内容以 text 结尾
                removed_list.append(i)
            self.ui.label_remove_by_content_result.setText(f"删除内容以{text}结尾的项成功，删除项索引为{removed_list}")
        elif self.ui.radioButton_ignore_capltals.isChecked():  # 模糊匹配 忽略大小写
            targets = [i for i in range(self.ui.listWidget_List.count()) if self.ui.listWidget_List.item(i).text().lower() == text.lower()]
            removed_list =[]
            # 从后向前删除，避免迭代时索引变化
            for i in reversed(targets):
                self.ui.listWidget_List.takeItem(i)  # 删除所有内容为 text 的元素 忽略大小写
                removed_list.append(i)
            self.ui.label_remove_by_content_result.setText(f"删除内容为{text}的元素的项（忽略大小写）成功，删除项索引为{removed_list}")
        elif self.ui.radioButton_regular_expression.isChecked():  # 正则匹配
            if re.compile(text):
                targets = [i for i in range(self.ui.listWidget_List.count()) if re.match(text, self.ui.listWidget_List.item(i).text())]
                removed_list =[]
                # 从后向前删除，避免迭代时索引变化
                for i in reversed(targets):
                    self.ui.listWidget_List.takeItem(i)  # 删除所有内容匹配正则表达式的元素
                    removed_list.append(i)
                if removed_list:
                    self.ui.label_remove_by_content_result.setText(f"删除内容匹配正则表达式{text}的元素成功，删除项索引为{removed_list}")
                else:
                    self.ui.label_remove_by_content_result.setText(f"没有删除项，因为列表中没有内容匹配正则表达式{text}")
            else:
                self.ui.label_remove_by_content_result.setText(f"正则表达式{text}语法错误")

    # 清空列表全部内容
    def clear_list(self):
        self.ui.listWidget_List.clear()

    '''
    -----------------------------------------------------------------------------------------------------------------------------------
    改
    -----------------------------------------------------------------------------------------------------------------------------------
    '''

    # 依位置修改
    def modify_item(self):
        text = self.ui.lineEdit_modify.text()
        position = self.ui.spinBox_modify_position.value()
        self.ui.listWidget_List.item(position).setText(text)
        self.ui.label_modify_by_position_result.setText(f"修改第{position}个元素为{text}成功")

    # 依内容替换
    def replace_item(self):
        text_old = self.ui.lineEdit_replace_old_content.text()
        text_new = self.ui.lineEdit_replace_new_content.text()
        if self.ui.radioButton_equal.isChecked():  # 精确匹配
            targets = [i for i in range(self.ui.listWidget_List.count()) if self.ui.listWidget_List.item(i).text() == text_old]
            replaced_list = []
            for i in targets:
                self.ui.listWidget_List.item(i).setText(text_new)
                replaced_list.append(i)
            if replaced_list:
                self.ui.label_replace_by_content_result.setText(f"成功将列表中所有内容为{text_old}的元素替换为{text_new}，替换项索引为{replaced_list}")
            else:
                self.ui.label_replace_by_content_result.setText(f"列表中没有内容为{text_old}的元素")
        elif self.ui.radioButton_include.isChecked():  # 模糊匹配
            targets = [i for i in range(self.ui.listWidget_List.count()) if text_old in self.ui.listWidget_List.item(i).text()]
            replaced_list = []
            for i in targets:
                self.ui.listWidget_List.item(i).setText(self.ui.listWidget_List.item(i).text().replace(text_old, text_new))
                replaced_list.append(i)
            if replaced_list:
                self.ui.label_replace_by_content_result.setText(f"成功将列表中所有包含{text_old}的元素替换为{text_new}，替换项索引为{replaced_list}")
            else:
                self.ui.label_replace_by_content_result.setText(f"列表中没有包含{text_old}的元素")
        elif self.ui.radioButton_start_with.isChecked():  # 模糊匹配 以*开头
            targets = [i for i in range(self.ui.listWidget_List.count()) if self.ui.listWidget_List.item(i).text().startswith(text_old)]
            replaced_list = []
            for i in targets:
                self.ui.listWidget_List.item(i).setText(self.ui.listWidget_List.item(i).text().replace(text_old, text_new, 1))
                replaced_list.append(i)
            if replaced_list:
                self.ui.label_replace_by_content_result.setText(f"成功将列表中所有以{text_old}开头的元素替换为以{text_new}开头，替换项索引为{replaced_list}")
            else:
                self.ui.label_replace_by_content_result.setText(f"列表中没有以{text_old}开头的元素")
        elif self.ui.radioButton_end_with.isChecked():  # 模糊匹配 以*结尾
            targets = [i for i in range(self.ui.listWidget_List.count()) if self.ui.listWidget_List.item(i).text().endswith(text_old)]
            replaced_list = []
            pattern = re.escape(text_old) + '$'
            for i in targets:
                self.ui.listWidget_List.item(i).setText(re.sub(pattern, text_new, self.ui.listWidget_List.item(i).text()))
                replaced_list.append(i)
            if replaced_list:
                self.ui.label_replace_by_content_result.setText(f"成功将列表中所有以{text_old}结尾的元素替换为以{text_new}结尾，替换项索引为{replaced_list}")
            else:
                self.ui.label_replace_by_content_result.setText(f"列表中没有以{text_old}结尾的元素")
        elif self.ui.radioButton_ignore_capltals.isChecked():  # 模糊匹配 忽略大小写
            targets = [i for i in range(self.ui.listWidget_List.count()) if self.ui.listWidget_List.item(i).text().lower() == text_old.lower()]
            replaced_list = []
            pattern = re.compile(re.escape(text_old), re.IGNORECASE)
            for i in targets:
                self.ui.listWidget_List.item(i).setText(pattern.sub(text_new, self.ui.listWidget_List.item(i).text()))
                replaced_list.append(i)
            if replaced_list:
                self.ui.label_replace_by_content_result.setText(f"成功将列表中所有内容为{text_old}（忽略大小写）替换为{text_new}，替换项索引为{replaced_list}")
            else:
                self.ui.label_replace_by_content_result.setText(f"列表中没有内容为{text_old}（忽略大小写）的元素")
        elif self.ui.radioButton_regular_expression.isChecked():  # 正则表达式匹配
            if re.compile(text_old):
                targets = [i for i in range(self.ui.listWidget_List.count()) if re.search(text_old, self.ui.listWidget_List.item(i).text())]
                replaced_list = []
                for i in targets:
                    self.ui.listWidget_List.item(i).setText(re.sub(text_old, text_new, self.ui.listWidget_List.item(i).text()))
                    replaced_list.append(i)
                if replaced_list:
                    self.ui.label_replace_by_content_result.setText(f"成功将列表中所有匹配正则表达式{text_old}的元素替换为{text_new}，替换项索引为{replaced_list}")
                else:
                    self.ui.label_replace_by_content_result.setText(f"列表中没有匹配正则表达式{text_old}的元素")
            else:
                self.ui.label_remove_by_content_result.setText(f"正则表达式{text_old}语法错误")

    # 依位置交换
    def change_position(self):
        position_1 = self.ui.spinBox_change_position_1.value()
        position_2 = self.ui.spinBox_change_position_2.value()
        if position_1 == position_2:
            self.ui.label_change_position_result.setText("两个位置不能相同")
        else:
            # 确保两个位置都在列表的范围内
            if position_1 >= 0 and position_1 < self.ui.listWidget_List.count() and \
            position_2 >= 0 and position_2 < self.ui.listWidget_List.count():
                # 获取两个位置的项目
                item_1 = self.ui.listWidget_List.item(position_1)
                item_2 = self.ui.listWidget_List.item(position_2)
                temp_text = item_1.text()
                item_1.setText(item_2.text())
                item_2.setText(temp_text)
                self.ui.label_change_position_result.setText(f"（{position_1} : {item_2.text()}）与（{position_2} : {item_1.text()}）位置交换成功")
            else:
                self.ui.label_change_position_result.setText("位置超出列表范围")

    '''
    -----------------------------------------------------------------------------------------------------------------------------------
    查
    -----------------------------------------------------------------------------------------------------------------------------------
    '''

    # 依位置查找
    def find_by_position(self):
        position = self.ui.spinBox_find_result_position.value()
        if position >= 0 and position < self.ui.listWidget_List.count():
            text = self.ui.listWidget_List.item(position).text()
            self.ui.label_find_by_position_result.setText(f"依位置查找 查找结果（{position} : {text}）")
        else:
            self.ui.label_find_by_position_result.setText("查找范围错误")

    # 依内容查找
    def find_by_content(self):
        text = self.ui.lineEdit_find_by_content.text()
        items = self.ui.listWidget_List.findItems(text, Qt.MatchFlag.MatchExactly)
        position_list = [self.ui.listWidget_List.row(item) for item in items]
        if position_list:
            self.ui.label_find_by_content_result.setText(f"依内容查找 查找结果（{str(position_list)}）")
        else:
            self.ui.label_find_by_content_result.setText("未找到内容")

    # 依内容匹配
    def find_match(self):
        text = self.ui.lineEdit_find_match.text()
        if self.ui.radioButton_equal.isChecked():  # 精确匹配
            items = self.ui.listWidget_List.findItems(text, Qt.MatchFlag.MatchExactly)
        elif self.ui.radioButton_include.isChecked():  # 模糊匹配 包含*
            items = self.ui.listWidget_List.findItems(text, Qt.MatchFlag.MatchContains | Qt.MatchFlag.MatchCaseSensitive) # 大小写敏感
        elif self.ui.radioButton_start_with.isChecked():  # 模糊匹配 以*开头
            items = self.ui.listWidget_List.findItems(text, Qt.MatchFlag.MatchStartsWith)
        elif self.ui.radioButton_end_with.isChecked():  # 模糊匹配 以*结尾
            items = self.ui.listWidget_List.findItems(text, Qt.MatchFlag.MatchEndsWith)
        elif self.ui.radioButton_ignore_capltals.isChecked():  # 模糊匹配 忽略大小写
            items = self.ui.listWidget_List.findItems(text, Qt.MatchFlag.MatchContains)
        elif self.ui.radioButton_regular_expression.isChecked():  # 正则匹配
            items = self.ui.listWidget_List.findItems(text, Qt.MatchFlag.MatchRegularExpression)
            if not re.compile(text):
                self.ui.plainTextEdit_find_include.setPlainText(f"正则表达式{text}语法错误")
                return
        position_list = [self.ui.listWidget_List.row(item) for item in items]
        if position_list:
            self.ui.plainTextEdit_find_include.setPlainText(str(position_list))
            for position in position_list:
                content = self.ui.listWidget_List.item(position).text()
                self.ui.plainTextEdit_find_include.appendPlainText(f"{position} : {content}")
        else:
            self.ui.plainTextEdit_find_include.setPlainText("未找到匹配项")

    '''
    -----------------------------------------------------------------------------------------------------------------------------------
    当前项
    -----------------------------------------------------------------------------------------------------------------------------------
    '''

    # 当前项 信息
    def current_item_changed(self, current_item, previous_item):
        if current_item and previous_item:
            current_item_index = self.ui.listWidget_List.currentIndex().row()
            previous_item_index = self.ui.listWidget_List.row(previous_item)
            self.ui.label_current_item.setText(f"当前选择项（{current_item_index} : {current_item.text()}），上一选择项（{previous_item_index} : {previous_item.text()}）。")

    # 勾选状态
    def item_changed(self, current_item):
        state = current_item.checkState()
        if state == Qt.CheckState.Unchecked:
            state = "未勾选"
        elif state == Qt.CheckState.PartiallyChecked:
            state = "部分勾选"
        else:
            state = "已勾选"
        self.ui.label_check_state.setText(f"勾选状态：{state}")

    # 使当前项 允许勾选
    def checkable_current_row_function(self):
        current_row = self.ui.listWidget_List.currentRow()
        current_item = self.ui.listWidget_List.item(current_row)
        current_flags = current_item.flags()
        # 设置勾选状态为未勾选
        current_item.setCheckState(Qt.CheckState.Unchecked)
        # 允许用户勾选
        new_flags = current_flags | Qt.ItemFlag.ItemIsUserCheckable
        current_item.setFlags(new_flags)
    
    # 使当前项 不允许勾选
    def uncheckable_current_row_function(self):
        current_row = self.ui.listWidget_List.currentRow()
        current_item = self.ui.listWidget_List.item(current_row)
        current_flags = current_item.flags()
        # 移除勾选状态
        current_item.setCheckState(Qt.CheckState.Unchecked)
        # 不允许用户勾选
        new_flags = current_flags & ~Qt.ItemFlag.ItemIsUserCheckable
        current_item.setFlags(new_flags)
        # 重新插入相同内容到相同位置，以完全移除勾选框
        text = current_item.text()
        position = self.ui.listWidget_List.currentRow()
        self.ui.listWidget_List.takeItem(position)
        self.ui.listWidget_List.insertItem(position, text)
        self.ui.listWidget_List.setCurrentRow(current_row)
        
    # 上移 当前项
    def moveUp_current_row_function(self):
        current_row = self.ui.listWidget_List.currentRow()
        if current_row > 0:
            current_item = self.ui.listWidget_List.takeItem(current_row)
            self.ui.listWidget_List.insertItem(current_row - 1, current_item)
            self.ui.listWidget_List.setCurrentRow(current_row - 1)

    # 下移当前项
    def moveDown_current_row_function(self):
        current_row = self.ui.listWidget_List.currentRow()
        if current_row < self.ui.listWidget_List.count() - 1:
            current_item = self.ui.listWidget_List.takeItem(current_row)
            self.ui.listWidget_List.insertItem(current_row + 1, current_item)
            self.ui.listWidget_List.setCurrentRow(current_row + 1)

    # 将当前项 移至顶部
    def moveToTop_current_row_function(self):
        current_row = self.ui.listWidget_List.currentRow()
        if current_row > 0:
            current_item = self.ui.listWidget_List.takeItem(current_row)
            self.ui.listWidget_List.insertItem(0, current_item)
            self.ui.listWidget_List.setCurrentRow(0)

    # 将当前项 移至底部
    def moveToBottom_current_row_function(self):
        current_row = self.ui.listWidget_List.currentRow()
        if current_row < self.ui.listWidget_List.count() - 1:
            current_item = self.ui.listWidget_List.takeItem(current_row)
            self.ui.listWidget_List.addItem(current_item)
            self.ui.listWidget_List.setCurrentRow(self.ui.listWidget_List.count() - 1)



if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
