#!/usr/bin/python3
# -*- coding: utf-8 -*-

# from PyQt5 import QApplication
from PyQt5.QtWidgets import QApplication

from Model import Model
from MainController import MainController
from MainView import MainView
from SessionWindow import SessionWindow

import sys
class App(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.model = Model()
        self.main_ctrl = MainController(self.model)
        self.main_view = MainView(self.model, self.main_ctrl)
        self.main_view.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
