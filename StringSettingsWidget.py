from PyQt5.QtWidgets import QWidget

from Ui_StringSettingsWidget import Ui_StringSettingsWidget


class StringSettingsWidget(QWidget):

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
    def rdict(self):
        return self.ui.dictGroup.isChecked()

    @rdict.setter
    def rdict(self, checked):
        self.ui.dictGroup.setChecked(checked)

    @property
    def rand(self):
        return self.ui.randGroup.isChecked()

    @rand.setter
    def rand(self, checked):
        self.ui.randGroup.setChecked(checked)

    @property
    def dictionary(self):
        return self.ui.dictCombo.currentText()

    @dictionary.setter
    def dictionary(self, distr):
        indx = self.ui.dictCombo.findText(distr)
        self.ui.dictCombo.setCurrentIndex(indx)

    @property
    def minlen(self):
        return self.ui.minLenSpin.value()

    @minlen.setter
    def minlen(self, value):
        self.ui.maxLenSpin.minimum = value
        self.ui.minLenSpin.setValue(value)

    @property
    def maxlen(self):
        return self.ui.maxLenSpin.value()

    @maxlen.setter
    def maxlen(self, value):
        self.ui.minLenSpin.maximum = value
        self.ui.maxLenSpin.setValue(value)

    def __init__(self, model, controller):
        self.model = model
        self.controller = controller

        super().__init__()
        self.build_ui()

        self.model.sub_upd_func(self.upd_ui_from_model)
        self.upd_ui_from_model()

    def build_ui(self):
        self.ui = Ui_StringSettingsWidget()
        self.ui.setupUi(self)

        # Connections
        self.ui.dictGroup.toggled.connect(self.on_dict_toggled)
        self.ui.randGroup.toggled.connect(self.on_rand_toggled)
        self.ui.minLenSpin.valueChanged.connect(self.on_minlen_changed)
        self.ui.maxLenSpin.valueChanged.connect(self.on_maxlen_changed)

    def upd_ui_from_model(self):
        self.colname = self.model.name
        self.table = self.model.table.name
        self.coltype = self.model.type
        self.nullable = self.model.nullable
        self.keytype = self.model.keytype
        self.default = self.model.default
        self.extra = self.model.extra

        self.rdict = self.model.generator.dict
        self.rand = self.model.generator.rand
        self.dictionary = self.model.generator.dictionary
        self.maxlen = self.model.generator.maxlen
        self.minlen = self.model.generator.minlen

    def on_dict_toggled(self, checked):
        self.controller.dict_toggled(checked)

    def on_rand_toggled(self, checked):
        self.controller.rand_toggled(checked)

    def on_minlen_changed(self, value):
        self.ui.maxLenSpin.minimum = value
        self.controller.change_minlen(value)

    def on_maxlen_changed(self, value):
        self.ui.minLenSpin.maximum = value
        self.controller.change_maxlen(value)
