from PyQt5.QtWidgets import QMainWindow

from Ui_MainView import Ui_MainView
from SessionWindow import SessionWindow

class MainView(QMainWindow):

    def __init__(self, model, controller):
        self.model = model
        self.controller = controller
        super().__init__()
        self.build_ui()

        self.model.sub_upd_func(self.upd_ui_from_model)

    def build_ui(self):
        self.ui = Ui_MainView()
        self.ui.setupUi(self)
        self.session_manager = SessionWindow(self.model, self.controller)
        self.session_manager.show()
        # connections
        # self.ui.tabWidget.tabCloseRequested.connect(self.tab_close_request)
        # self.session_manager.connected.connect(self.session_manager_connected)
        # self.ui.schemaTreeWidget.itemDoubleClicked.connect(self.item_selected)


    def upd_ui_from_model(self):        
        if self.model.connection.isConnected() and self.session_manager.isVisible():
            self.session_manager.close()

