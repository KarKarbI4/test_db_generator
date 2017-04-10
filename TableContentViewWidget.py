from PyQt5.QtWidgets import QTableWidgetItem, QWidget

from Ui_TableContentViewWidget import Ui_TableContentViewWidget

class TableContentViewWidget(QWidget):

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, content):
        self._rows = content

    @property
    def cols(self):
        return self._cols

    @cols.setter
    def cols(self, cols):
        self._cols = cols

    @property
    def table_name(self):
        self._table_name

    @table_name.setter
    def table_name(self, table_name):
        self._table_name = table_name

    def build_table(self):
        self.ui.tableWidget.setColumnCount(len(self.cols))
        self.ui.tableWidget.setRowCount(len(self.rows))
        self.ui.tableWidget.setHorizontalHeaderLabels(self.cols)
        for i, row in enumerate(self.rows):
            for j in range(len(self.cols)):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(row[j])))


    def __init__(self, model, controller):
        super().__init__()
        self.model = model
        self.controller = controller
        self._rows = None
        self._cols = None
        self._table_name = ""

        self.build_ui()

        self.upd_ui_from_model()

    def build_ui(self):
        self.ui = Ui_TableContentViewWidget()
        self.ui.setupUi(self)

        # connections

    def upd_ui_from_model(self):
        self.rows = self.model.content
        self.cols = self.model.columns
        self.table_name = self.model.name
        self.build_table()