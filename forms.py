import sys
from PyQt5.QtCore import QLine
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QWidget, QVBoxLayout, QPushButton


class MinhaPrimeiraTela(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.setWindowTitle('Minha primeira tela com PyQt5')
        self.setGeometry(20, 20, 400, 200)

        self.rotulo_nome = QLabel()
        self.rotulo_nome.setText('Nome')
        self.texto_nome = QLineEdit(self)

        self.rotulo_sexo = QLabel()
        self.rotulo_sexo.setText('Sexo')
        self.texto_sexo = QLineEdit()

        self.rotulo_salario = QLabel()
        self.rotulo_salario.setText('Salário')
        self.texto_salario = QLineEdit()

        self.botao_salvar = QPushButton()
        self.botao_salvar.setText('Salvar')

        self.vertical = QVBoxLayout()
        self.vertical.addWidget(self.rotulo_nome)
        self.vertical.addWidget(self.texto_nome)
        self.vertical.addWidget(self.rotulo_sexo)
        self.vertical.addWidget(self.texto_sexo)
        self.vertical.addWidget(self.rotulo_salario)
        self.vertical.addWidget(self.texto_salario)
        self.vertical.addWidget(self.botao_salvar)

        self.componentes = QWidget()
        self.componentes.setLayout(self.vertical)

        self.setCentralWidget(self.componentes)

app = QApplication(sys.argv)

form = MinhaPrimeiraTela()
form.show()

sys.exit(app.exec_())
