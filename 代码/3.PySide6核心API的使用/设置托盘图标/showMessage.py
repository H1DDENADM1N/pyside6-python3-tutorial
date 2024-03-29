from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QSystemTrayIcon, QMessageBox, QPushButton, QVBoxLayout, QWidget)
from PySide6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_tray_icon()
        self.init_buttons()
    
    def init_tray_icon(self):
        # 添加托盘图标
        self.tray_icon = QSystemTrayIcon(QIcon('.\\assets\\appicon.ico'), parent=self)
        self.tray_icon.messageClicked.connect(self.message_clicked)
        self.tray_icon.show()

    def init_buttons(self):
        # 创建按钮并设置其点击信号连接到槽函数
        self.info_button = QPushButton("显示信息消息")
        self.info_button.clicked.connect(self.show_info_message)
        
        self.warning_button = QPushButton("显示警告消息")
        self.warning_button.clicked.connect(self.show_warning_message)
        
        self.critical_button = QPushButton("显示严重错误消息")
        self.critical_button.clicked.connect(self.show_critical_message)
        
        self.custom_button = QPushButton("显示自定义图标消息")
        self.custom_button.clicked.connect(self.show_custom_message)
        
        # 垂直布局管理器
        layout = QVBoxLayout()
        
        # 添加按钮到布局
        layout.addWidget(self.info_button)
        layout.addWidget(self.warning_button)
        layout.addWidget(self.critical_button)
        layout.addWidget(self.custom_button)
        
        # 创建一个中心小部件并设置布局
        central_widget = QWidget()
        central_widget.setLayout(layout)
        
        # 设置中心小部件
        self.setCentralWidget(central_widget)

    def show_info_message(self):
        self.tray_icon.showMessage("信息", "这是一个信息内容", QSystemTrayIcon.MessageIcon.Information, 5000)

    def show_warning_message(self):
        self.tray_icon.showMessage("警告", "这是一个警告内容", QSystemTrayIcon.MessageIcon.Warning, 5000)

    def show_critical_message(self):
        self.tray_icon.showMessage("严重错误", "这是一个严重错误内容", QSystemTrayIcon.MessageIcon.Critical, 5000)

    def show_custom_message(self):
        self.tray_icon.showMessage("自定义图标", "这是一个自定义图标内容", QIcon('.\\assets\\appicon.ico'), 5000)

    def message_clicked(self):
        QMessageBox.information(
            self,
            "标题",
            "内容",
        )

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
