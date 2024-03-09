from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QSystemTrayIcon, QMenu)
from PySide6.QtGui import QIcon, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 添加托盘图标
        tray_icon = QSystemTrayIcon(QIcon('.\\assets\\appicon.ico'), parent=self)
        tray_icon.activated.connect(self.handleTrayIconActivation)
        # 为托盘图标添加菜单
        menu = QMenu()
        quit_action = QAction('退出', self)
        quit_action.triggered.connect(lambda: app.quit())
        menu.addAction(quit_action)
        tray_icon.setContextMenu(menu)

        tray_icon.show()

    # 单击托盘图标打开主窗口
    def handleTrayIconActivation(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.showNormal()

    # 忽略主窗口关闭事件，仅隐藏主窗口
    def closeEvent(self, event):
        self.hide()
        event.ignore()

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
