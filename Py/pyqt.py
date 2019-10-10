from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel
import PyQt5
# from PyQt5.QtWidgets import QDesktopWidget
# from mainwindow import Ui_MainWindow

class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)

        # TITLE
        self.title = 'Login'
        self.setWindowTitle(self.title)

        # SIZE
        self.left = 20
        self.top = 20
        self.width = 640
        self.height = 380
        self.setGeometry(self.left, self.top, self.width, self.height)
        # Center function calling
        self.center()

        # UserName
        self.textName = QtWidgets.QLineEdit(self)
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Username:')
        self.textPass = QtWidgets.QLineEdit(self)

        # self.textPass = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    # FUNCTION TO CENTER THE WINDOW
    def center(self):
        frameGm = self.frameGeometry()
        screen = PyQt5.QtWidgets.QApplication.desktop().screenNumber(PyQt5.QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = PyQt5.QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def handleLogin(self):
        if (self.textName.text() == 'foo' and
            self.textPass.text() == 'bar'):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Bad user or password')

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = Window()
        window.show()
        sys.exit(app.exec_())