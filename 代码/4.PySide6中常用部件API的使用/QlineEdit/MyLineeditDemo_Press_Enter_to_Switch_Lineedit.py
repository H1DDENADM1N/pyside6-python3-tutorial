from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton, QMessageBox, QLabel
from PySide6.QtCore import Qt

class MyLineEdit(QLineEdit):
    def __init__(self, next_focus_widget=None, parent=None):
        super().__init__(parent)
        self.next_focus_widget = next_focus_widget
        self.returnPressed.connect(self.switch_focus)

    def switch_focus(self):
        if self.next_focus_widget:
            self.next_focus_widget.setFocus()

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.machine_id_label = QLabel("机器码：")
        self.machine_id = MyLineEdit()
        self.activate_key_label = QLabel("激活码：")
        self.activate_key = MyLineEdit()
        self.execute_registration = QPushButton("激活(Shift+Enter)")
        self.execute_registration.clicked.connect(self.execute_registration_pressed)
        self.execute_registration.setShortcut(Qt.ShiftModifier | Qt.Key_Return)

        # 设置下一个焦点对象
        self.machine_id.next_focus_widget = self.activate_key
        self.activate_key.next_focus_widget = self.machine_id

        layout = QVBoxLayout(self)
        layout.addWidget(self.machine_id_label)
        layout.addWidget(self.machine_id)
        layout.addWidget(self.activate_key_label)
        layout.addWidget(self.activate_key)
        layout.addWidget(self.execute_registration)
        
        self.machine_id.setFocus()
        
        self.setWindowTitle("回车切换LineEdit示例")
        self.resize(500, 100)
        self.show()

    def execute_registration_pressed(self):
        machine_id = self.machine_id.text()
        activate_key = self.activate_key.text()
        if not (machine_id or activate_key):
            critical_box = QMessageBox()
            reply = critical_box.critical(self, "错误", "请输入机器码和激活码。", QMessageBox.Ok)

        if machine_id == "1" and activate_key == "1":
            info_box = QMessageBox()
            reply = info_box.information(self, "信息", "激活成功", QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
