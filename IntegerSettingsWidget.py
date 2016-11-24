from PyQt5.QtWidgets import QWidget

from Ui_IntegerSettingsWidget import Ui_IntegerSettingsWidget


class IntegerSettingsWidget(QWidget):

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
        self.ui.minValueEdit.setValue(value)

    @property
    def maxvalue(self):
        return self.ui.maxValueEdit.value()

    @maxvalue.setter
    def maxvalue(self, value):
        self.ui.maxValueEdit.setValue(value)

    def __init__(self, model, controller):
        self.model = model
        self.controller = controller

        super().__init__()
        self.build_ui()

        self.model.sub_upd_func(self.upd_ui_from_model)
        self.upd_ui_from_model()

    def build_ui(self):
        self.ui = Ui_IntegerSettingsWidget()
        self.ui.setupUi(self)

        # Connections
        self.ui.seqGroup.toggled.connect(self.on_seq_toggled)
        self.ui.randomGroup.toggled.connect(self.on_rand_toggled)
        self.ui.minValueEdit.valueChanged.connect(self.on_minvalue_changed)
        self.ui.maxValueEdit.valueChanged.connect(self.on_maxvalue_changed)
        self.ui.stepValue.valueChanged.connect(self.on_stepvalue_changed)

    def upd_ui_from_model(self):
        self.colname = self.model.name
        self.table = self.model.table.name
        self.coltype = self.model.type
        self.nullable = self.model.nullable
        self.keytype = self.model.keytype
        self.default = self.model.default
        self.extra = self.model.extra

        self.seq = self.model.generator.seq
        self.rand = self.model.generator.rand
        self.seq_step = self.model.generator.seq_step
        self.distribution = self.model.generator.distribution
        self.maxvalue = self.model.generator.maxvalue
        self.minvalue = self.model.generator.minvalue

    def on_seq_toggled(self, checked):
        self.controller.seq_toggled(checked)

    def on_rand_toggled(self, checked):
        self.controller.rand_toggled(checked)

    def on_minvalue_changed(self, value):
        self.controller.change_minvalue(value)
        self.ui.maxValueEdit.minimum = value

    def on_maxvalue_changed(self, value):
        self.controller.change_maxvalue(value)
        self.ui.minValueEdit.maximum = value

    def on_stepvalue_changed(self, value):
        self.controller.change_stepvalue(value)
