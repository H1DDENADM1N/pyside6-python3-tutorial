# 导入设计的GUI界面类，通常这个文件是由Qt Designer设计并使用pyuic工具转换成Python代码生成的。
import Ui_MainWinVerticalLayout
# 从PySide6模块中导入QApplication和QMainWindow类。
from PySide6.QtWidgets import QApplication, QMainWindow

# 这个条件判断确保了当该脚本被当作主程序运行时，下面的代码块将被执行。
if __name__ == '__main__':
    # 使用空列表 [] 创建 QApplication 实例，用于应用程序初始化。
    app = QApplication([])
    # 创建一个QMainWindow类的实例，它是应用程序的主窗口框架。
    mainWindow = QMainWindow()
    # 创建一个设计的GUI界面类的实例。
    ui = Ui_MainWinVerticalLayout.Ui_MainWindow()
    # 调用setupUi方法来设置主窗口的界面，这个方法通常是由Ui_MainWindow类自动生成的。
    ui.setupUi(mainWindow)
    # 调用show()方法来显示主窗口。
    mainWindow.show()
    # 进入主事件循环，等待用户操作，exec_()方法开始处理事件，直到调用exit()或主窗口被销毁时结束。
    app.exec()