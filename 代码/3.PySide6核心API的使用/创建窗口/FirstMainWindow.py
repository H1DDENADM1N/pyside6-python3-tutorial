from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QMenuBar, QToolBar, QTextEdit)
from PySide6.QtGui import QAction

# 创建应用程序实例
app = QApplication([])
# 创建主窗口实例
main_window = QMainWindow()
# 调整窗口大小
main_window.resize(400, 100)
# 设置窗口标题
main_window.setWindowTitle('QMainWindow Example')

# 设置菜单栏
# 创建一个菜单栏
menu_bar = QMenuBar()
# 创建一个菜单
this_menu = menu_bar.addMenu("这是菜单")
# 创建一个动作（菜单项）
exit_action = QAction("退出", main_window)
# 将动作连接到关闭窗口的槽函数
exit_action.triggered.connect(main_window.close)
# 将动作添加到菜单中
this_menu.addAction(exit_action)
# 将菜单栏添加到主窗口中
main_window.setMenuBar(menu_bar)

# 设置工具栏
# 创建一个工具栏
tool_bar = QToolBar("主工具栏")
# 创建一个动作（工具按钮）
tool_bar_action = QAction("这是工具栏里的按钮", main_window)
# 将动作添加到工具栏中
tool_bar.addAction(tool_bar_action)
# 将工具栏添加到主窗口中
main_window.addToolBar(tool_bar)

# 设置状态栏，5秒后消失
main_window.statusBar().showMessage("这是状态栏，它会在5秒后消失", 5000)

# 设置中心小部件
# 创建一个中心小部件
# 中心小部件通常使用垂直布局
central_widget = QTextEdit()
central_widget.setPlainText("这是中心小部件的内容。")
# 将中心小部件添加到窗口中
main_window.setCentralWidget(central_widget)

# 显示主窗口
main_window.show()
# 启动应用程序的事件循环
app.exec()
