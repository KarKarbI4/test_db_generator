from PyQt5.QtWidgets import QWidget
from Ui_DatabaseWidget import Ui_DatabaseWidget


class DatabaseWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_DatabaseWidget()
        self.ui.setupUi(self)
