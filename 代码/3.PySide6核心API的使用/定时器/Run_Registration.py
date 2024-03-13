from Ui_Registration import Ui_Registration as Ui
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QTimer

class Registration(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui()
        self.ui.setupUi(self)

        self.count = 5  # 假设倒计时为5秒
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_countdown)
        self.ui.pushButton_send_verify_code_in_registration.clicked.connect(self.send_verify_code)

    def send_verify_code(self):
        self.count = 5  # 重置倒计时
        self.ui.pushButton_send_verify_code_in_registration.setEnabled(False)
        # 如果定时器已经在运行，先停止它
        if self.timer.isActive():
            self.timer.stop()
        # 启动定时器
        self.timer.start(1000)

    def update_countdown(self):
        self.count -= 1
        self.ui.pushButton_send_verify_code_in_registration.setText(f"重新发送 ( {self.count}s )")
        if self.count <= 0:
            self.timer.stop()
            self.ui.pushButton_send_verify_code_in_registration.setEnabled(True)
            self.ui.pushButton_send_verify_code_in_registration.setText("发送验证码")

if __name__ == '__main__':
    app = QApplication([])
    window = Registration()
    window.show()
    app.exec()
