# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/DateSettingsWidget.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DateSettingsWidget(object):
    def setupUi(self, DateSettingsWidget):
        DateSettingsWidget.setObjectName("DateSettingsWidget")
        DateSettingsWidget.resize(511, 434)
        self.mainLayout = QtWidgets.QVBoxLayout(DateSettingsWidget)
        self.mainLayout.setObjectName("mainLayout")
        self.infoLayout = QtWidgets.QFormLayout()
        self.infoLayout.setObjectName("infoLayout")
        self.columnNameLabel = QtWidgets.QLabel(DateSettingsWidget)
        self.columnNameLabel.setObjectName("columnNameLabel")
        self.infoLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.columnNameLabel)
        self.columnNameValueLabel = QtWidgets.QLabel(DateSettingsWidget)
        self.columnNameValueLabel.setObjectName("columnNameValueLabel")
        self.infoLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.columnNameValueLabel)
        self.typeLabel = QtWidgets.QLabel(DateSettingsWidget)
        self.typeLabel.setObjectName("typeLabel")
        self.infoLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.typeLabel)
        self.typeValueLabel = QtWidgets.QLabel(DateSettingsWidget)
        self.typeValueLabel.setObjectName("typeValueLabel")
        self.infoLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.typeValueLabel)
        self.nullValueLabel = QtWidgets.QLabel(DateSettingsWidget)
        self.nullValueLabel.setObjectName("nullValueLabel")
        self.infoLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.nullValueLabel)
        self.nullLabel = QtWidgets.QLabel(DateSettingsWidget)
        self.nullLabel.setObjectName("nullLabel")
        self.infoLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.nullLabel)
        self.defaultLabel = QtWidgets.QLabel(DateSettingsWidget)
        self.defaultLabel.setObjectName("defaultLabel")
        self.infoLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.defaultLabel)
        self.extraLabel = QtWidgets.QLabel(DateSettingsWidget)
        self.extraLabel.setObjectName("extraLabel")
        self.infoLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.extraLabel)
        self.defaultValueLabel = QtWidgets.QLabel(DateSettingsWidget)
        self.defaultValueLabel.setObjectName("defaultValueLabel")
        self.infoLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.defaultValueLabel)
        self.extraValueLabel = QtWidgets.QLabel(DateSettingsWidget)
        self.extraValueLabel.setObjectName("extraValueLabel")
        self.infoLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.extraValueLabel)
        self.keyLabel = QtWidgets.QLabel(DateSettingsWidget)
        self.keyLabel.setObjectName("keyLabel")
        self.infoLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.keyLabel)
        self.keyValueLabel = QtWidgets.QLabel(DateSettingsWidget)
        self.keyValueLabel.setObjectName("keyValueLabel")
        self.infoLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.keyValueLabel)
        self.tableLabel = QtWidgets.QLabel(DateSettingsWidget)
        self.tableLabel.setObjectName("tableLabel")
        self.infoLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.tableLabel)
        self.tableValueLabel = QtWidgets.QLabel(DateSettingsWidget)
        self.tableValueLabel.setObjectName("tableValueLabel")
        self.infoLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tableValueLabel)
        self.mainLayout.addLayout(self.infoLayout)
        self.settingsGroup = QtWidgets.QGroupBox(DateSettingsWidget)
        self.settingsGroup.setFlat(False)
        self.settingsGroup.setCheckable(False)
        self.settingsGroup.setObjectName("settingsGroup")
        self.settingsGroupLayout = QtWidgets.QFormLayout(self.settingsGroup)
        self.settingsGroupLayout.setObjectName("settingsGroupLayout")
        self.minValueLabel = QtWidgets.QLabel(self.settingsGroup)
        self.minValueLabel.setObjectName("minValueLabel")
        self.settingsGroupLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.minValueLabel)
        self.maxValueLabel = QtWidgets.QLabel(self.settingsGroup)
        self.maxValueLabel.setObjectName("maxValueLabel")
        self.settingsGroupLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.maxValueLabel)
        self.seqGroup = QtWidgets.QGroupBox(self.settingsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seqGroup.sizePolicy().hasHeightForWidth())
        self.seqGroup.setSizePolicy(sizePolicy)
        self.seqGroup.setCheckable(True)
        self.seqGroup.setObjectName("seqGroup")
        self.seqGroupLayout = QtWidgets.QFormLayout(self.seqGroup)
        self.seqGroupLayout.setObjectName("seqGroupLayout")
        self.stepLabel = QtWidgets.QLabel(self.seqGroup)
        self.stepLabel.setObjectName("stepLabel")
        self.seqGroupLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.stepLabel)
        self.spinBox = QtWidgets.QSpinBox(self.seqGroup)
        self.spinBox.setObjectName("spinBox")
        self.seqGroupLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.settingsGroupLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.seqGroup)
        self.randomGroup = QtWidgets.QGroupBox(self.settingsGroup)
        self.randomGroup.setCheckable(True)
        self.randomGroup.setObjectName("randomGroup")
        self.randomGroupLayout = QtWidgets.QFormLayout(self.randomGroup)
        self.randomGroupLayout.setObjectName("randomGroupLayout")
        self.distributionLabel = QtWidgets.QLabel(self.randomGroup)
        self.distributionLabel.setObjectName("distributionLabel")
        self.randomGroupLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.distributionLabel)
        self.distributionCombo = QtWidgets.QComboBox(self.randomGroup)
        self.distributionCombo.setObjectName("distributionCombo")
        self.randomGroupLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.distributionCombo)
        self.settingsGroupLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.randomGroup)
        self.minValueEdit = QtWidgets.QDateEdit(self.settingsGroup)
        self.minValueEdit.setObjectName("minValueEdit")
        self.settingsGroupLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.minValueEdit)
        self.maxValueEdit = QtWidgets.QDateEdit(self.settingsGroup)
        self.maxValueEdit.setObjectName("maxValueEdit")
        self.settingsGroupLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.maxValueEdit)
        self.mainLayout.addWidget(self.settingsGroup)

        self.retranslateUi(DateSettingsWidget)
        QtCore.QMetaObject.connectSlotsByName(DateSettingsWidget)

    def retranslateUi(self, DateSettingsWidget):
        _translate = QtCore.QCoreApplication.translate
        DateSettingsWidget.setWindowTitle(_translate("DateSettingsWidget", "DateSettingsWidget"))
        self.columnNameLabel.setText(_translate("DateSettingsWidget", "Column:"))
        self.columnNameValueLabel.setText(_translate("DateSettingsWidget", "ColumnName"))
        self.typeLabel.setText(_translate("DateSettingsWidget", "Type:"))
        self.typeValueLabel.setText(_translate("DateSettingsWidget", "types"))
        self.nullValueLabel.setText(_translate("DateSettingsWidget", "no"))
        self.nullLabel.setText(_translate("DateSettingsWidget", "Nullable:"))
        self.defaultLabel.setText(_translate("DateSettingsWidget", "Default:"))
        self.extraLabel.setText(_translate("DateSettingsWidget", "Extra:"))
        self.defaultValueLabel.setText(_translate("DateSettingsWidget", "\'\'"))
        self.extraValueLabel.setText(_translate("DateSettingsWidget", "\'\'"))
        self.keyLabel.setText(_translate("DateSettingsWidget", "Key:"))
        self.keyValueLabel.setText(_translate("DateSettingsWidget", "\'\'"))
        self.tableLabel.setText(_translate("DateSettingsWidget", "Table:"))
        self.tableValueLabel.setText(_translate("DateSettingsWidget", "TableName"))
        self.settingsGroup.setTitle(_translate("DateSettingsWidget", "Generate settings"))
        self.minValueLabel.setText(_translate("DateSettingsWidget", "Min date: "))
        self.maxValueLabel.setText(_translate("DateSettingsWidget", "Max date:"))
        self.seqGroup.setTitle(_translate("DateSettingsWidget", "Sequentialy"))
        self.stepLabel.setText(_translate("DateSettingsWidget", "Day step:"))
        self.randomGroup.setTitle(_translate("DateSettingsWidget", "Randomly"))
        self.distributionLabel.setText(_translate("DateSettingsWidget", "Distribution:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DateSettingsWidget = QtWidgets.QWidget()
    ui = Ui_DateSettingsWidget()
    ui.setupUi(DateSettingsWidget)
    DateSettingsWidget.show()
    sys.exit(app.exec_())
