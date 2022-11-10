from PySide6.QtWidgets import QApplication
from  controllers.prog_main import Prog_main as saludo
import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = saludo()
    prog.show()
    sys.exit(app.exec())