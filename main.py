#!/usr/bin/python3
# -*- coding: utf-8 -*-

# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication

from DatabaseGenerator import DatabaseGenerator
from GeneratorWindow import GeneratorWindow


def main():
    import sys
    app = QApplication(sys.argv)
    dbgen = DatabaseGenerator()
    generator_window = GeneratorWindow(dbgen)
    generator_window.show()
    sys.exit(app.exec_())
    print(dbgen.driver)

if __name__ == '__main__':
    main()
