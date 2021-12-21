import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MinhaPrimeiraTela(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.setWindowTitle('Minha primeira tela com PyQt5')
        self.setGeometry(20, 20, 800, 400)

app = QApplication(sys.argv)

form = MinhaPrimeiraTela()
form.show()

sys.exit(app.exec_())
