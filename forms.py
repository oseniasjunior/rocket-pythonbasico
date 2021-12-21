from io import SEEK_CUR
import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QWidget, QVBoxLayout, QPushButton
from bd import Funcionario, BancoDados

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
        self.botao_salvar.clicked.connect(self.acao_salvar)

        self.mensagem = QLabel()
        self.mensagem.setText('')
        self.mensagem.setStyleSheet('color: green')
        self.mensagem.setVisible(False)

        self.vertical = QVBoxLayout()
        self.vertical.addWidget(self.rotulo_nome)
        self.vertical.addWidget(self.texto_nome)
        self.vertical.addWidget(self.rotulo_sexo)
        self.vertical.addWidget(self.texto_sexo)
        self.vertical.addWidget(self.rotulo_salario)
        self.vertical.addWidget(self.texto_salario)
        self.vertical.addWidget(self.botao_salvar)
        self.vertical.addWidget(self.mensagem)

        self.componentes = QWidget()
        self.componentes.setLayout(self.vertical)

        self.setCentralWidget(self.componentes)

        self.banco = BancoDados()

    def acao_salvar(self):
        funcionario = Funcionario()
        funcionario.nome = self.texto_nome.text()
        funcionario.sexo = self.texto_sexo.text()
        funcionario.salario = float(self.texto_salario.text())
        self.banco.salvar(funcionario)
        self.exibir_mensagem()
        self.limpar_tela()
        
    def exibir_mensagem(self):
        self.mensagem.setText('Cadastrado com sucesso')
        self.mensagem.setVisible(True)
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.limpar_mensagem)
        self.timer.start()

    def limpar_mensagem(self):
        self.mensagem.setText('')
        self.mensagem.setVisible(False)

    def limpar_tela(self):
        self.texto_nome.setText('')
        self.texto_salario.setText('')
        self.texto_sexo.setText('')

        
app = QApplication(sys.argv)

form = MinhaPrimeiraTela()
form.show()

sys.exit(app.exec_())
