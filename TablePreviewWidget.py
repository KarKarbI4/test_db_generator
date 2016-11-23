from PyQt5.QtWidgets import QTableWidgetItem, QWidget

from Ui_TablePreviewWidget import Ui_TablePreviewWidget


class TablePreviewWidget(QWidget):

    table = property()

    @table.setter
    def table(self, cols):
        self.ui.tableWidget.setColumnCount(6)
        self.ui.tableWidget.setRowCount(len(cols))
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra'])
        for indx, col in enumerate(cols.values()):
            self.ui.tableWidget.setItem(indx, 0, QTableWidgetItem(col.name))
            self.ui.tableWidget.setItem(indx, 1, QTableWidgetItem(col.type))
            self.ui.tableWidget.setItem(
                indx, 2, QTableWidgetItem(col.nullable))
            self.ui.tableWidget.setItem(indx, 3, QTableWidgetItem(col.keytype))
            self.ui.tableWidget.setItem(indx, 4, QTableWidgetItem(col.default))
            self.ui.tableWidget.setItem(indx, 5, QTableWidgetItem(col.extra))

    def __init__(self, model, controller):
        super().__init__()
        self.model = model
        self.controller = controller

        self.build_ui()

        self.upd_ui_from_model()

    def build_ui(self):
        self.ui = Ui_TablePreviewWidget()
        self.ui.setupUi(self)

        # connections
        self.ui.rowNumSpin.valueChanged.connect(self.on_value_changed)

    def upd_ui_from_model(self):
        self.table = self.model.columns
        self.ui.rowNumSpin.setValue(self.model.generate_size)

    def on_value_changed(self, value):
        self.controller.change_value(value)
