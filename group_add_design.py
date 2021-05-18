# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_group_add.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(442, 318)
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setGeometry(QtCore.QRect(320, 270, 91, 25))
        self.addButton.setObjectName("addButton")
        self.group_name = QtWidgets.QLineEdit(Form)
        self.group_name.setGeometry(QtCore.QRect(110, 50, 231, 25))
        self.group_name.setObjectName("group_name")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 20, 171, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(170, 100, 121, 17))
        self.label_2.setObjectName("label_2")
        self.group_tasks = QtWidgets.QPlainTextEdit(Form)
        self.group_tasks.setGeometry(QtCore.QRect(30, 129, 381, 121))
        self.group_tasks.setObjectName("group_tasks")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addButton.setText(_translate("Form", "Добавить"))
        self.label.setText(_translate("Form", "Название группы задач"))
        self.label_2.setText(_translate("Form", "Названия задач"))

