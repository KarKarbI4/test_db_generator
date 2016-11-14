from PyQt5.QtWidgets import QWidget

from Ui_TablePreviewWidget import Ui_TablePreviewWidget
# from DatabaseGenerator import DatabaseGenerator, DbConnectionError


class TablePreviewWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TablePreviewWidget()
        self.ui.setupUi(self)
        self.setup()

    def setup(self):
        pass
