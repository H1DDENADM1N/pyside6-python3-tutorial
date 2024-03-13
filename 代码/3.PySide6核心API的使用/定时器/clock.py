import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import QTimer, QDateTime, Qt

class CountDownClock(QWidget):
    def __init__(self, end_date):
        super().__init__()
        self.end_date = end_date
        self.initUI()

    def initUI(self):
        # 设置窗口标题
        self.setWindowTitle('倒计时时钟')
        # 创建一个标签用于显示日期和时间
        self.label_current_time = QLabel('当前时间： YYYY年-MM月-DD日 hh:mm:ss')
        self.label_current_time.setAlignment(Qt.AlignCenter)
        self.label_current_time.setFont(self.font())
        # 创建一个标签用于显示倒计时
        self.label_remain_time = QLabel('剩余时间：DD 天 HH 时 MM 分 SS 秒')
        self.label_remain_time.setAlignment(Qt.AlignCenter)
        self.label_remain_time.setFont(self.font())
        # 设置窗口布局
        layout = QVBoxLayout()
        layout.addWidget(self.label_current_time)
        layout.addWidget(self.label_remain_time)
        self.setLayout(layout)
        # 创建一个 QTimer 对象
        self.timer = QTimer()
        self.timer.setInterval(1000)
        # 连接计时器的信号/槽
        self.timer.timeout.connect(self.updateTime)
        self.timer.timeout.connect(self.updateCountDown)
        # 启动计时器
        self.timer.start()

    def updateTime(self):
        # 获取当前时间
        current_time = QDateTime.currentDateTime()
        # 格式化时间为字符串，包括日期和时间
        time_str = current_time.toString('当前时间：yyyy年-MM月-dd日 hh:mm:ss')
        # 更新标签显示的日期和时间
        self.label_current_time.setText(time_str)

    def updateCountDown(self):
        # 获取当前时间
        current_time = QDateTime.currentDateTime()
        # 计算剩余时间
        remaining_time = self.end_date.toMSecsSinceEpoch() - current_time.toMSecsSinceEpoch()
        # 如果剩余时间小于等于0，停止计时器
        if remaining_time <= 0:
            self.timer.stop()
            self.label_remain_time.setText("已过期")
            return
        # 将毫秒转换为秒
        remaining_time /= 1000
        # 计算年月日时分秒
        days = remaining_time // (24 * 60 * 60)
        remaining_time %= (24 * 60 * 60)
        hours = remaining_time // (60 * 60)
        remaining_time %= (60 * 60)
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        # 更新标签显示的倒计时
        self.label_remain_time.setText(f"剩余时间：{int(days)} 天 {int(hours):02} 时 {int(minutes):02} 分 {int(seconds):02} 秒")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 假设到期时间为未来的某个日期
    end_date = QDateTime.fromString("2024-03-16T07:00:00", Qt.ISODate)
    clock = CountDownClock(end_date)
    clock.show()
    sys.exit(app.exec())
