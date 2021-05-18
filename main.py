import sys  
from PyQt5 import QtCore, QtWidgets
import design, plan_design, fact_design, about_design, group_add_design
import method
import shutil
import os

import report 


class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)

        #self.tasknames.textChanged.connect()        
        self.reportButton.clicked.connect(self.generateReport)
        
        self.plan_group.triggered.connect(self.showPlanGroup)
        self.plan.triggered.connect(self.showPlan)
        self.fact.triggered.connect(self.showFact)
        self.about.triggered.connect(self.showAbout)
        self.import_plan_2.triggered.connect(self.importPlan)
        self.import_fact.triggered.connect(self.importFact)
        self.import_hierarchy.triggered.connect(self.importHierarchy)

    def showPlanGroup(self):
        self.planGroup = GroupAddWindow()
        self.planGroup.show()

        #names = self.tasknames.text()
        #self.textBrowser.setText(method.statistic(names))

    def showPlan(self):
        self.plan = PlanWindow()
        self.plan.show()

    def showFact(self):
        self.fact = FactWindow()
        self.fact.show()

    def showAbout(self):
        self.about = AboutWindow()
        self.about.show()

    def importPlan(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Импорт таблицы плановых работ', '/home')[0]
        dest = os.path.abspath(os.curdir)
        dest+= '/data/Plan.csv'
        shutil.copy(fname, dest)

    def importFact(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Импорт таблицы фактических работ', '/home')[0]
        dest = os.path.abspath(os.curdir)
        dest+= '/data/Fact.csv'
        shutil.copy(fname, dest)

    def importHierarchy(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Импорт данных об иерархии', '/home')[0]
        dest = os.path.abspath(os.curdir)
        dest+= '/data/Hierarchy.csv'
        shutil.copy(fname, dest)

    def generateReport(self):
        method.generate(self.taskNames.text())

class PlanWindow(QtWidgets.QMainWindow, plan_design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.okButton.clicked.connect(self.addPlanTask)

    def addPlanTask(self):
        task=method.Task(self.date_s.text(), self.date_f.text(), self.cost.text(), self.task_name.text())
        method.writePlanTask(task)


class FactWindow(QtWidgets.QMainWindow, fact_design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.okButton.clicked.connect(self.addFactTask)

    def addFactTask(self):
        task=method.Task(self.date_s.text(), self.date_f.text(), self.cost.text(), self.task_name.text())
        method.writeFactTask(task)


class GroupAddWindow(QtWidgets.QMainWindow, group_add_design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addButton.clicked.connect(self.addGroup)

    def addGroup(self):
        method.writeHierarchy(self.group_name.text(), self.group_tasks.toPlainText())

class AboutWindow(QtWidgets.QMainWindow, about_design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.okButton.clicked.connect(self.addAbout)

    def addAbout(self):
        about = method.About(self.proj_name.text(), self.start_date.text(), self.finish_date.text(), self.bac.text() )
        method.writeAbout(about)

def main():
    method.readData()
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

    sys.exit(app.exec_())


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
