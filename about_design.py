# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_about.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(402, 300)
        self.okButton = QtWidgets.QPushButton(Form)
        self.okButton.setGeometry(QtCore.QRect(290, 250, 91, 25))
        self.okButton.setObjectName("okButton")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 20, 361, 201))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, 40, -1)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.proj_name = QtWidgets.QLineEdit(self.widget)
        self.proj_name.setObjectName("proj_name")
        self.verticalLayout.addWidget(self.proj_name)
        self.start_date = QtWidgets.QLineEdit(self.widget)
        self.start_date.setObjectName("start_date")
        self.verticalLayout.addWidget(self.start_date)
        self.finish_date = QtWidgets.QLineEdit(self.widget)
        self.finish_date.setObjectName("finish_date")
        self.verticalLayout.addWidget(self.finish_date)
        self.bac = QtWidgets.QLineEdit(self.widget)
        self.bac.setObjectName("bac")
        self.verticalLayout.addWidget(self.bac)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.okButton.setText(_translate("Form", "Ok"))
        self.label.setText(_translate("Form", "Название проекта"))
        self.label_2.setText(_translate("Form", "Дата начала "))
        self.label_3.setText(_translate("Form", "Дата окончания"))
        self.label_4.setText(_translate("Form", "Плановый бюджет"))

