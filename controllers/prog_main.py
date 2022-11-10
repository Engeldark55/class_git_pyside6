from PySide6.QtWidgets import QWidget
from view.simple_saludo import Ui_Form as saludo

class Prog_main(QWidget, saludo):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(lambda: self.saludemos())
    def saludemos(self):
        name = self.line_name.text().strip()
        if len(name):
            self.label_saludo.setText(f'hey hola {name}')
            if name.isnumeric() == True:
                self.label_saludo.setText('no acepto numeros')
        else:
            self.label_saludo.setText('coloque su nombre....')
       
 