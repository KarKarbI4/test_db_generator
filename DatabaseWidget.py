from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QTreeWidgetItem, QWidget, QErrorMessage, QMessageBox
from Ui_DatabaseWidget import Ui_DatabaseWidget
from traceback import format_exc

class DatabaseWidget(QWidget):

    tree = property()

    item_dclicked = pyqtSignal(object)

    @tree.setter
    def tree(self, items):
        parent = QTreeWidgetItem(self.ui.tablesTree)
        parent.setText(0, 'All')
        parent.setFlags(parent.flags() | Qt.ItemIsTristate |
                        Qt.ItemIsUserCheckable)
        for tablename in items:
            table_item = QTreeWidgetItem(parent)
            table_item.setFlags(table_item.flags() | Qt.ItemIsUserCheckable)
            table_item.setText(0, tablename)
            table_item.setCheckState(0, Qt.Unchecked)
        parent.setCheckState(0, Qt.Checked)
        self.ui.tablesTree.expandAll()

    def __init__(self, dbmodel, controller):
        super().__init__()
        self.dbmodel = dbmodel
        self.controller = controller

        self.build_ui()

        self.dbmodel.sub_upd_func(self.upd_ui_from_model)
        self.upd_ui_from_model()

    def build_ui(self):
        self.ui = Ui_DatabaseWidget()
        self.ui.setupUi(self)

        # connect
        self.ui.tablesTree.itemDoubleClicked.connect(self.on_item_dclicked)
        self.ui.generateBtn.clicked.connect(self.on_gen_btn_clicked)

    def upd_ui_from_model(self):
        self.tree = self.dbmodel.tables

    def on_item_dclicked(self, item, col):
        if item.text(0) != 'All':
            self.item_dclicked.emit(self.dbmodel.table(item.text(0)))

    def on_gen_btn_clicked(self):
        try:
            self.controller.generate()
        except Exception as e:
            # print(e)
            # error_dialog = QErrorMessage()
            # error_dialog.setIcon(QMessageBox.Critical)
            # error_dialog.showMessage(str(e))
            # error_dialog.exec_()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            msg.setText("Error occured while generating")
            msg.setInformativeText(str(e))
            msg.setWindowTitle("Error!")
            msg.setDetailedText(format_exc())
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()


