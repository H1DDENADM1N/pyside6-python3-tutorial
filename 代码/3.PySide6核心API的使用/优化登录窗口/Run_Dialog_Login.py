from PySide6.QtWidgets import ( QApplication, QMainWindow, QDialog,
                                QSystemTrayIcon, QMenu, QMessageBox)
from PySide6.QtGui import QIcon, QAction, QGuiApplication, QMouseEvent
from PySide6.QtCore import Qt, QRect, Signal
from Ui_Dialog_Login import Ui_Dialog
from Ui_MainWindow import Ui_MainWindow

app = QApplication([])

def set_window_icon(window):
    window.setWindowIcon(QIcon('.\\assets\\appicon.ico'))

def move_window_to_screen_center(window):
    screen = QGuiApplication.primaryScreen().availableGeometry()
    size = window.geometry()
    window.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

def show_messagebox(icon, title, message):
    box = QMessageBox()
    box.setIcon(icon)
    box.setWindowTitle(title)
    box.setText(message)
    box.addButton(QMessageBox.Ok)
    box.setWindowFlags(box.windowFlags() | Qt.WindowStaysOnTopHint)
    box.exec()

class CustomMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        set_window_icon(self)
        move_window_to_screen_center(self)
        self.setup_tray_icon()

    def update_login_info(self, username, password):
        self.setWindowTitle(f"主窗口，用户（ {username} ）已登录")
        self.statusBar().showMessage(f"用户（ {username} ）已登录", 5000)

    def setup_tray_icon(self):
        tray_icon = QSystemTrayIcon(QIcon('.\\assets\\appicon.ico'), parent=self)
        tray_icon.activated.connect(self.show_window)
        menu = QMenu()
        quit_action = QAction('退出', self)
        quit_action.triggered.connect(app.quit)
        menu.addAction(quit_action)
        tray_icon.setContextMenu(menu)
        tray_icon.show()

    def show_window(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.showNormal()

    def closeEvent(self, event):
            event.ignore()
            self.hide()

class CustomLoginDialog(QDialog):
    upadteMainWindowLoginInfoSignal = Signal(str, str)  # 自定义信号
    def __init__(self, parent=None):
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
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.tabWidget.tabBar().setVisible(False)  # 隐藏标签栏表头
        self.parent = parent
        set_window_icon(self)
        move_window_to_screen_center(self)
        self.setup_signals()

    def setup_signals(self):
        self.ui.pushButton_goback_login_in_registration.clicked.connect(self.goto_login_tab)
        self.ui.pushButton_goback_login_in_forgot_password.clicked.connect(self.goto_login_tab)
        self.ui.pushButton_goback_login_in_agreement_details.clicked.connect(self.goto_login_tab)
        self.ui.pushButton_goback_login_in_about.clicked.connect(self.goto_login_tab)
        self.ui.pushButton_goto_registration.clicked.connect(self.goto_registration_tab)
        self.ui.pushButton_goto_forgot_password.clicked.connect(self.goto_forgot_password_tab)
        self.ui.commandLinkButton_goto_read_agreement.clicked.connect(self.goto_agreement_details_tab)
        self.ui.checkBox_agree_agreement.stateChanged.connect(self.toggle_login_button)
        self.ui.pushButton_login.clicked.connect(self.process_login)
        self.ui.pushButton_login.setEnabled(False)

        # 注册和忘记密码功能，未完成
        self.ui.pushButton_send_verify_code_in_registration.setDisabled(True)
        self.ui.pushButton_registration_in_registration.setDisabled(True)
        self.ui.pushButton_send_verify_code_in_forgot_password.setDisabled(True)
        self.ui.pushButton_save_new_password_in_forgot_password.setDisabled(True)

        self.upadteMainWindowLoginInfoSignal.connect(self.parent.update_login_info)

    def goto_login_tab(self):
        self.ui.tabWidget.setCurrentIndex(0)

    def goto_registration_tab(self):
        self.ui.tabWidget.setCurrentIndex(1)

    def goto_forgot_password_tab(self):
        self.ui.tabWidget.setCurrentIndex(2)

    def goto_agreement_details_tab(self):
        self.ui.tabWidget.setCurrentIndex(3)

    def toggle_login_button(self, state):
        self.ui.pushButton_login.setEnabled(state == 2)

    def process_login(self):
        username = self.ui.lineEdit_username.text()
        password = self.ui.lineEdit_password.text()
        if username == "1" and password == "1":
            # self.parent.setWindowTitle(f"主窗口，用户（ {username} ）已登录")
            # self.parent.statusBar().showMessage(f"用户（ {username} ）已登录", 5000)
            self.upadteMainWindowLoginInfoSignal.emit(username, password)
            self.accept()
        else:
            show_messagebox(QMessageBox.Critical, "登录失败", "用户名或密码错误！")


    def keyPressEvent(self, event):
        # 忽略 Esc键 关闭窗口
        if event.key() == Qt.Key_Escape:
            event.ignore()
    
    # 重写鼠标按下事件，处理窗口拖动和边缘调整
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.mouse_pressed = True
            self.offset = event.globalPosition() - self.frameGeometry().topLeft()
            self.edge = self.get_resize_edge(event.position())
            if self.edge is not None:
                self.setCursor(self.get_resize_cursor(self.edge))
            else:
                self.draggable = True
                self.offset = event.position().toPoint()

    # 重写鼠标移动事件，处理窗口拖动或调整窗口大小
    def mouseMoveEvent(self, event: QMouseEvent):
        if self.draggable:
            self.move(event.globalPosition().toPoint() - self.offset)
        if self.mouse_pressed and self.edge is not None:
            self.resize_window(event)

    # 重写鼠标释放事件，处理拖动结束
    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.draggable = False
            self.mouse_pressed = False
            self.edge = None
            self.setCursor(Qt.ArrowCursor)

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


def show_login_dialog(main_window):
    dialog = CustomLoginDialog(main_window)
    dialog.exec()

def show_main_window():
    main_window = CustomMainWindow()
    main_window.show()
    show_login_dialog(main_window)
    app.exec()

if __name__ == '__main__':
    show_main_window()
    app.quit()
