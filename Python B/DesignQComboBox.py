# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ComboBox.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(385, 199)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.t1 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.t1.setFont(font)
        self.t1.setObjectName("t1")
        self.horizontalLayout.addWidget(self.t1)
        self.b1 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.additem)
        self.horizontalLayout.addWidget(self.b1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.combo1 = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.combo1.setFont(font)
        self.combo1.setObjectName("combo1")
        self.combo1.addItem("")
        self.combo1.addItem("")
        self.combo1.addItem("")
        self.combo1.addItem("")
        self.combo1.addItem("")
        self.combo1.addItem("")
        self.horizontalLayout_2.addWidget(self.combo1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.b2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.b2.clicked.connect(self.rmitem)
        self.horizontalLayout_2.addWidget(self.b2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.t2 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.t2.setFont(font)
        self.t2.setObjectName("t2")
        self.verticalLayout.addWidget(self.t2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.b1.setText(_translate("Form", "Add Item"))
        self.combo1.setItemText(0, _translate("Form", "C"))
        self.combo1.setItemText(1, _translate("Form", "C++"))
        self.combo1.setItemText(2, _translate("Form", "Java"))
        self.combo1.setItemText(3, _translate("Form", "Python"))
        self.combo1.setItemText(4, _translate("Form", "Rust"))
        self.combo1.setItemText(5, _translate("Form", "Go"))
        self.b2.setText(_translate("Form", "Remove Item"))

    def rmitem(self):
      indx=self.combo1.currentIndex()
      item=self.combo1.currentText()
      self.t2.setText(item+" is removed from combobox")
      self.combo1.removeItem(indx)

    def additem(self):
      self.combo1.addItem(self.t1.text())
      self.t2.setText(self.t1.text()+" is added to combobox")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
