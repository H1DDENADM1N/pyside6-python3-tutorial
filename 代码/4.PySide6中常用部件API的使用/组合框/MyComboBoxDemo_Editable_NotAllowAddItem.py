from PySide6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout
from PySide6.QtCore import Qt, QEvent


class MyComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setEditable(True)

        # 设置一个不可选的占位符条目作为 提示语
        self.addItem("提示语")
        self.setItemData(0, Qt.AlignCenter, Qt.TextAlignmentRole)
        self.model().item(0).setEnabled(False)  # 禁用占位符条目，使其不可选

    def event(self, event):
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Return:
            current_text = self.currentText()

            if current_text == "":
                self.setCurrentIndex(0)  # 重置为提示语
            if self.findText(current_text, Qt.MatchExactly) == -1:
                print(f"不允许添加新条目： {current_text} 。")
                # self.setCurrentIndex(0)  # 重置为提示语
                # 如果当前文本不在下拉列表中，找到最相似的条目
                similar_index = self.findText(current_text, Qt.MatchContains)
                if similar_index != -1:
                    self.setCurrentIndex(similar_index)
                return True
        return super().event(event)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.comboBox = MyComboBox(self)
        self.comboBox.addItems(["选项1", "选项2", "选项3"])
        self.comboBox.setCurrentIndex(0)  # 设置初始选中项为提示语
        self.comboBox.currentIndexChanged.connect(self.on_comboBox_currentIndexChanged)
        layout = QVBoxLayout(self)
        layout.addWidget(self.comboBox)
        self.setLayout(layout)
        self.setWindowTitle("不允许添加新条目，但允许编辑的combox示例")
        self.resize(500, 100)
        self.show()

    def on_comboBox_currentIndexChanged(self):
        # 忽略占位符条目的选择
        if self.comboBox.currentIndex() == 0:
            return
        
        print("当前选中的项：", self.comboBox.currentText())



if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
