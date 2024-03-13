from Ui_Calc import Ui_Calc
from PySide6.QtWidgets import (QApplication, QWidget,
                               QSystemTrayIcon, QMenu)
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent, QIcon, QAction

class Calc(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口标志
        self.setWindowFlags(
            self.windowFlags()
            | Qt.FramelessWindowHint  # 隐藏标题栏
            | Qt.Tool  # 隐藏Windows任务栏上的图标
            | Qt.WindowStaysOnTopHint  # 置顶
        )
        self.margin = 10  # 确定鼠标位置是否在边缘或角落
        self.mouse_pressed = False  # 鼠标按下标志
        self.draggable = False  # 窗口可拖动标志
        self.text = ""
        self.ui = Ui_Calc()
        self.ui.setupUi(self)
        self.ui.maximize_botton.clicked.connect(self.toggle_maximize_window)
        self.setup_signals()

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

    def setup_signals(self):
        self.ui.pushButton_1.clicked.connect(lambda: self.calc_func('1'))
        self.ui.pushButton_2.clicked.connect(lambda: self.calc_func('2'))
        self.ui.pushButton_3.clicked.connect(lambda: self.calc_func('3'))
        self.ui.pushButton_4.clicked.connect(lambda: self.calc_func('4'))
        self.ui.pushButton_5.clicked.connect(lambda: self.calc_func('5'))
        self.ui.pushButton_6.clicked.connect(lambda: self.calc_func('6'))
        self.ui.pushButton_7.clicked.connect(lambda: self.calc_func('7'))
        self.ui.pushButton_8.clicked.connect(lambda: self.calc_func('8'))
        self.ui.pushButton_9.clicked.connect(lambda: self.calc_func('9'))
        self.ui.pushButton_0.clicked.connect(lambda: self.calc_func('0'))
        self.ui.pushButton_Backspace.clicked.connect(lambda: self.calc_func('backspace'))
        self.ui.pushButton_Clear.clicked.connect(lambda: self.calc_func('clear'))
        self.ui.pushButton_Enter.clicked.connect(lambda: self.calc_func('enter'))
        self.ui.pushButton_Dot.clicked.connect(lambda: self.calc_func('.'))
        self.ui.pushButton_Add.clicked.connect(lambda: self.calc_func('+'))
        self.ui.pushButton_Sub.clicked.connect(lambda: self.calc_func('-'))
        self.ui.pushButton_Muti.clicked.connect(lambda: self.calc_func('*'))
        self.ui.pushButton_Div.clicked.connect(lambda: self.calc_func('/'))
        self.ui.pushButton_LeftBracket.clicked.connect(lambda: self.calc_func('('))
        self.ui.pushButton_RightBracket.clicked.connect(lambda: self.calc_func(')'))

    def calc_func(self, number):
        print("Button clicked, setting text to:", number)
        if number == 'backspace':
            self.text = self.text[:-1]
        elif number == 'enter':
            try:
                calc_result = str(eval(self.text))
            except Exception as e:
                calc_result = "Error"
            self.text = f"{self.text} = {calc_result}"
            self.ui.label_number_keyboard.setText(calc_result)
        elif number == 'clear':
            self.text = ''
        else:
            self.text += str(number)
        self.ui.plainTextEdit.setPlainText(self.text)
    
    # 最大化窗口的槽函数
    def toggle_maximize_window(self):
        if self.windowState() & Qt.WindowMaximized:
            self.showNormal()
        else:
            self.showMaximized()


    # 单击托盘图标打开主窗口
    def handleTrayIconActivation(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.showNormal()


    # 重写鼠标按下事件，处理窗口拖动和边缘调整
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
                    self.mouse_pressed = True  # 设置鼠标按下标志
                    self.offset = event.globalPosition() - self.frameGeometry().topLeft()
                    self.edge = self.get_resize_edge(event.position())  # 获取调整边缘
                    if self.edge is not None:
                        self.setCursor(self.get_resize_cursor(self.edge))  # 设置鼠标光标形状
                    else:
                        self.draggable = True  # 设置窗口可拖动标志
                        self.offset = event.position().toPoint()  # 更新偏移量

    # 重写鼠标移动事件，处理窗口拖动或调整窗口大小
    def mouseMoveEvent(self, event: QMouseEvent):
        if self.draggable:
            self.move(event.globalPosition().toPoint() - self.offset)    # 移动窗口
        if self.mouse_pressed and self.edge is not None:
            self.resize_window(event)    # 调整窗口大小

    # 重写鼠标释放事件，处理拖动结束
    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.draggable = False  # 清除窗口可拖动标志
            self.mouse_pressed = False  # 清除鼠标按下标志
            self.edge = None  # 清除调整边缘
            self.setCursor(Qt.ArrowCursor)  # 恢复鼠标光标形状

    # 获取鼠标位置对应的调整边缘
    def get_resize_edge(self, pos):
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()

        if pos.x() < self.margin and pos.y() < self.margin:
            return 'top_left'
        elif pos.x() > width - self.margin and pos.y() < self.margin:
            return 'top_right'
        elif pos.x() < self.margin and pos.y() > height - self.margin:
            return 'bottom_left'
        elif pos.x() > width - self.margin and pos.y() > height - self.margin:
            return 'bottom_right'
        elif pos.x() < self.margin:
            return 'left'
        elif pos.x() > width - self.margin:
            return 'right'
        elif pos.y() < self.margin:
            return 'top'
        elif pos.y() > height - self.margin:
            return 'bottom'
        else:
            return None

    # 设置适当的鼠标光标
    def get_resize_cursor(self, edge):
        if edge in ('top', 'bottom'):
            return Qt.SizeVerCursor
        elif edge in ('left', 'right'):
            return Qt.SizeHorCursor
        elif edge in ('top_left', 'bottom_right'):
            return Qt.SizeFDiagCursor
        elif edge in ('top_right', 'bottom_left'):
            return Qt.SizeBDiagCursor
        else:
            return Qt.ArrowCursor

    def resize_window(self, event):
        if self.edge is not None:
            global_pos = event.globalPosition()  # 全局鼠标位置
            local_pos = event.position()  # 局部（窗口内）鼠标位置
            x, y, w, h = self.x(), self.y(), self.width(), self.height()  # 当前窗口的位置和尺寸

            # 根据不同的边缘调整窗口的尺寸
            if self.edge in ('top', 'top_left', 'top_right'):
                delta_y = local_pos.y() - self.offset.y()
                y += delta_y
                h -= delta_y
            if self.edge in ('bottom', 'bottom_left', 'bottom_right'):
                h = global_pos.y() - y
            if self.edge in ('left', 'top_left', 'bottom_left'):
                delta_x = local_pos.x() - self.offset.x()
                x += delta_x
                w -= delta_x
            if self.edge in ('right', 'top_right', 'bottom_right'):
                w = global_pos.x() - x
            # 设置窗口的新位置和尺寸
            self.setGeometry(x, y, w, h)



if __name__ == '__main__':
    app = QApplication([])
    mainWindow = Calc()
    mainWindow.show()
    app.exec()
