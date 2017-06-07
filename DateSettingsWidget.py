from datetime import datetime

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QDate

from Ui_DateSettingsWidget import Ui_DateSettingsWidget

datetime_to_qdate = lambda x: QDate(x.year, x.month, x.day)
qdate_to_datetime = lambda x: datetime(year=x.year(), month=x.month(), day=x.day())

class DateSettingsWidget(QWidget):

    colname = property()

    @colname.setter
    def colname(self, name):
        self.ui.columnNameValueLabel.setText(name)

    table = property()

    @table.setter
    def table(self, table):
        self.ui.tableValueLabel.setText(table)

    coltype = property()

    @coltype.setter
    def coltype(self, coltype):
        self.ui.typeValueLabel.setText(coltype)

    nullable = property()

    @nullable.setter
    def nullable(self, nullable):
        self.ui.nullValueLabel.setText(nullable)

    keytype = property()

    @keytype.setter
    def keytype(self, keytype):
        self.ui.keyValueLabel.setText(keytype)

    default = property()

    @default.setter
    def default(self, default):
        self.ui.defaultValueLabel.setText(default)

    extra = property()

    @extra.setter
    def extra(self, extra):
        self.ui.extraValueLabel.setText(extra)

    @property
    def seq(self):
        return self.ui.seqGroup.isChecked()

    @seq.setter
    def seq(self, checked):
        self.ui.seqGroup.setChecked(checked)

    @property
    def rand(self):
        return self.ui.randomGroup.isChecked()

    @rand.setter
    def rand(self, checked):
        self.ui.randomGroup.setChecked(checked)

    @property
    def seq_step(self):
        return self.ui.stepValue.value()

    @seq_step.setter
    def seq_step(self, value):
        self.ui.stepValue.setValue(value)

    @property
    def distribution(self):
        return self.ui.distributionCombo.currentText()

    @distribution.setter
    def distribution(self, distr):
        indx = self.ui.distributionCombo.findText(distr)
        self.ui.distributionCombo.setCurrentIndex(indx)

    @property
    def minvalue(self):
        return self.ui.minValueEdit.value()

    @minvalue.setter
    def minvalue(self, value):
        self.ui.maxValueEdit.minimum = value
        self.ui.minValueEdit.setDate(value)

    @property
    def maxvalue(self):
        return self.ui.maxValueEdit.value()

    @maxvalue.setter
    def maxvalue(self, value):
        self.ui.minValueEdit.maximum = value
        self.ui.maxValueEdit.setDate(value)

    def __init__(self, model, controller):
        self.model = model
        self.controller = controller

        super().__init__()
        self.build_ui()

        self.model.sub_upd_func(self.upd_ui_from_model)
        self.upd_ui_from_model()

    def build_ui(self):
        self.ui = Ui_DateSettingsWidget()
        self.ui.setupUi(self)
        self.ui.minValueEdit.setCalendarPopup(True)
        self.ui.maxValueEdit.setCalendarPopup(True)

        # Connections
        self.ui.seqGroup.toggled.connect(self.on_seq_toggled)
        self.ui.randomGroup.toggled.connect(self.on_rand_toggled)
        self.ui.minValueEdit.dateChanged.connect(self.on_minvalue_changed)
        self.ui.maxValueEdit.dateChanged.connect(self.on_maxvalue_changed)
        self.ui.stepValue.valueChanged.connect(self.on_stepvalue_changed)

    def upd_ui_from_model(self):
        self.colname = self.model.name
        self.table = self.model.table.name
        self.coltype = self.model.type
        self.nullable = self.model.nullable
        self.keytype = self.model.keytype
        self.default = self.model.default
        self.extra = self.model.extra

        self.ui.distributionCombo.clear()
        self.ui.distributionCombo.addItems(self.model.generator.distributions)
        self.seq = self.model.generator.seq
        self.rand = self.model.generator.rand
        self.seq_step = self.model.generator.seq_step
        self.distribution = self.model.generator.distribution
        self.maxvalue = datetime_to_qdate(self.model.generator.maxvalue)
        self.minvalue = datetime_to_qdate(self.model.generator.minvalue)

    def on_seq_toggled(self, checked):
        self.controller.seq_toggled(checked)

    def on_rand_toggled(self, checked):
        self.controller.rand_toggled(checked)

    def on_minvalue_changed(self, value):
        new_value = qdate_to_datetime(value)
        self.controller.change_minvalue(new_value)
        self.ui.maxValueEdit.minimum = value

    def on_maxvalue_changed(self, value):
        new_value = qdate_to_datetime(value)
        self.controller.change_maxvalue(new_value)
        self.ui.minValueEdit.maximum = value

    def on_stepvalue_changed(self, value):
        self.controller.change_stepvalue(value)
