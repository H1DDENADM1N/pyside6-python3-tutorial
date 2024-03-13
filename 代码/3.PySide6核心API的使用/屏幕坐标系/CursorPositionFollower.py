import win32api
import win32con
import win32gui
import win32print
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPalette, QFont, QColor, QScreen

class Cursor_Position(QLabel):
    def __init__(self):
        super().__init__()
        self.Print_Screen_Scale_Use_QScreen()  # QScreen 无法直接获取屏幕未缩放前的屏幕尺寸
                                                # 但是可以获取缩放后的逻辑尺寸和屏幕缩放比例，计算出未缩放前的屏幕尺寸

        self.setWindowFlags(Qt.ToolTip | Qt.FramelessWindowHint)
        self.resize(150, 20)
        font = QFont("Segoe MDL2 Assets", 14)
        self.setFont(font)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#212121"))  # 设置背景颜色
        palette.setColor(QPalette.WindowText, QColor("#00B294"))  # 设置文本颜色
        self.setPalette(palette)

        # 创建一个定时器来定期更新鼠标位置
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_tooltip_position)
        self.timer.start(100)  # 每100毫秒更新一次

    def update_tooltip_position(self):
        # 使用pywin32获取全局鼠标位置
        x, y = win32api.GetCursorPos()

        # global scale_x, scale_y  # 获取屏幕缩放比例方法一
                                    # 在Pyside6 实例化 app 前，
                                    # 可以使用 Pywin32 计算屏幕缩放比例
                                    # 并设为全局变量

        # print(f"屏幕缩放比例: {scale_x}, {scale_y}")
        # x, y = x / scale_x, y / scale_y
        # print(x, y)
        # # 更新标签的位置和文本
        # self.move(x+(20/scale_x),y+(20/scale_y))

        print(f"QScreen 获取到的 屏幕缩放比例: {self.scale_factor}")  # 获取屏幕缩放比例方法二
                                                                    # 在Pyside6 实例化 app 后，
                                                                    # 可以使用 QScreen 获取屏幕缩放比例
        x, y = x / self.scale_factor, y / self.scale_factor
        print(x, y)
        self.move(x+(20/self.scale_factor),y+(20/self.scale_factor))

        self.setText(f"X: {int(x)}, Y: {int(y)}")
        self.setVisible(True)

    def Print_Screen_Scale_Use_QScreen(self):
        # 获取当前屏幕
        screen = QApplication.primaryScreen()
        # 获取屏幕的分辨率
        # resolution = screen.size()
        # logical_width = resolution.width()
        # logical_height = resolution.height()
        # print(f"QScreen 获取到的 逻辑尺寸: {logical_width}x{logical_height}")  # 2048x1152
        # 获取屏幕的缩放比例
        self.scale_factor = screen.devicePixelRatio()
        print(f"QScreen 获取到的 屏幕缩放比例: {self.scale_factor}")  # 1.25
        # # 计算原始屏幕尺寸
        # screen_width = logical_width * self.scale_factor
        # screen_height = logical_height * self.scale_factor
        # print(f"QScreen 获取到的 屏幕尺寸: {screen_width}x{screen_height}")  # 2560x1440


def Print_Screen_Scale():
    # 获取屏幕尺寸
    hDC = win32gui.GetDC(0)
    screen_width = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    screen_height = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
    print(f"屏幕尺寸: {screen_width}x{screen_height}")  # 2560x1440
    # 获取屏幕逻辑尺寸
    logical_width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    logical_height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    print(f"逻辑尺寸: {logical_width}x{logical_height}")  # 2048x1152
    # 计算屏幕的缩放比例
    global scale_x, scale_y
    scale_x = screen_width / logical_width
    scale_y = screen_height / logical_height
    print(f"屏幕缩放比例: {scale_x}, {scale_y}")  # 1.25, 1.25

def Print_Screen_Scale_After_app_Set():
    # 获取屏幕尺寸
    hDC = win32gui.GetDC(0)
    screen_width = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    screen_height = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
    print(f"实例化 app 后 获取到的 屏幕尺寸: {screen_width}x{screen_height}")  # 2560x1440
    # 获取屏幕逻辑尺寸
    logical_width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    logical_height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    print(f"实例化 app 后 获取到的 逻辑尺寸: {logical_width}x{logical_height}")  # 2560x1440
                                                                                # 与实例化 app 前 获取到的 2048x1152 不同，
                                                                                # 在实例化 app 后 获取到的 逻辑尺寸 不正确
    # 计算屏幕的缩放比例
    scale_x = screen_width / logical_width
    scale_y = screen_height / logical_height
    print(f"实例化 app 后 获取到的 屏幕缩放比例: {scale_x}, {scale_y}")  # 1.25, 1.25



if __name__ == "__main__":

    Print_Screen_Scale()  # 在Pyside6 实例化 app 前，
                            # 可以使用 Pywin32 计算屏幕缩放比例

    app = QApplication([])

    Print_Screen_Scale_After_app_Set()  # 在Pyside6 实例化 app 后 使用 Pywin32 计算屏幕缩放比例，
                                        # 与实例化 app 前 获取到的 2048x1152 不同，
                                        # 在实例化 app 后 获取到的 逻辑尺寸 不正确

    # Print_Screen_Scale_Use_QScreen()  # QScreen 无法直接获取屏幕未缩放前的屏幕尺寸
                                        # 但是可以获取缩放后的逻辑尺寸和屏幕缩放比例，计算出未缩放前的屏幕尺寸

    label = Cursor_Position()
    label.show()
    app.exec()
