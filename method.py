import datetime
import dateutil.parser as parser
import os.path
import copy
import csv
import report

import plotly as py                     # pip install plotly==2.0.5
import plotly.figure_factory as ff
import plotly.graph_objects as go

planTasksR = [] 
factTasksR = []
groups = []

class Task:
    
    isDone = 0
    
    startDate = datetime.date(1970 ,1,1)
    finishDate = datetime.date(1970 ,1,1)
    name = "None"
    
    def __init__(self, start, finish , money, name, isDone = 1):
        
        self.startDate = start
        self.finishDate = finish
        self.money = int (money)
        self.name = name
        self.isDone = isDone
        
    def info(self):
        print(self.startDate, ' ', self.finishDate, ' ', self.money, ' ',self.name, self.isDone)
       
  
class TaskGroup:
    
    groupName = "None"
    tasksNames = []
    
    def __init__(self, groupname, tasksname):
        self.groupName = groupname
        self.tasksNames = tasksname

    def info(self):
        print(self.groupName, ' ', self.tasksNames)

class About:

    projectName = "None"
    startDate = datetime.date(1970 ,1,1)
    finishDate = datetime.date(1970 ,1,1)    
    bac = 0

    def __init__(self, Name, start, finish, budg):
        self.projectName = Name
        self.startDate = start
        self.finishDate = finish    
        self.bac = int (budg)

about = About(0,0,0,0)


def funcBAC (Tasks):
    return sum((int(Tasks[i].money) for i in range(0, int(len(Tasks)))))


def funcPV (planTasksTrue, date, names ):                  # planned value
    planTasks = copy.deepcopy(planTasksTrue)
   
    pv=0
    Tasks = []
    
    for task in planTasks:                             # specified tasks from plan go into 'Tasks'
        if task.name in names:
            Tasks.append(task)
            #task.info()
    
    if 'all' in names:                                 # or all of them go there
        for task in planTasks:
            Tasks.append(task)
            
    for task in Tasks:
        if task.finishDate <= date:
            pv = pv + task.money*task.isDone
    
    if Tasks[-1].finishDate > date:                
        dayCost = Tasks[-1].money / ( (Tasks[-1].finishDate - Tasks[-1].startDate).days +1)
        pv += dayCost * ((date - Tasks[-1].startDate).days + 1)
    
    return pv
     
    
def funcEV (planTasksTrue, factTasksTrue, names):                 # earned value
    factTasks = copy.deepcopy(factTasksTrue)    
    planTasks = copy.deepcopy(planTasksTrue)
    ev = 0
    
    Tasks = []

    
    if 'all' in names: 
        for task in factTasks:                                    # takes started tasks 
            if task.isDone > 0:
                Tasks.append(task)
    else:
        for task in factTasks:                                    # takes started tasks 
            if (task.name in names) and (task.isDone > 0):
                Tasks.append(task)
        
    
    def searchTaskCost (Tasks, name):                                # searches for some cash
        for task in Tasks:
            if task.name == name:
                return task.money
            
    for task in Tasks:
        task.money = searchTaskCost(planTasks, task.name)            # replaces actual cost with planned
           
    date = datetime.date(2100, 4, 10)
    ev = funcPV(Tasks, date, 'all')
        
    return ev
    
    
def funcAC (factTasksTrue, date, names ):                             # actual cost
    factTasks = copy.deepcopy(factTasksTrue)
    Tasks = []
    
    for task in factTasks:
        task.isDone = 1
        Tasks.append(task)
        
    return funcPV(Tasks, date, names )

def funcPspi (names, planTasks, factTasks):
    lp = 0
    lf = 0
    Tasks1=[]
    Tasks2=[]
    for task in planTasks:                             
        if task.name in names:
            Tasks1.append(task)
    for task in factTasks:                             
        if task.name in names:
            Tasks2.append(task)

    for task in Tasks1:
        lp+=(task.finishDate-task.startDate).days
        
    for task in Tasks2:
        lf+=(task.finishDate-task.startDate).days
    if lf<=lp:
        p=1
    else: p=lp/lf
    return p

def funcP (names, date):
    ev = funcEV (planTasksR, factTasksR, names)
    pv = funcPV (planTasksR, date, names)
    pspi = funcPspi(names,planTasksR, factTasksR)
    return (ev/pv)*pspi

def funcE (names, date):
    ac = funcAC(factTasksR, date, names)
    ev = funcEV (planTasksR, factTasksR, names)
    kpr=1
    return 1 + (1 - ac/ev)*kpr

def funcEA (names, date):
    return funcE(names, date)*funcP(names, date)




def readData():

    if not os.path.isfile('data/Plan.csv'): 
        with open('data/Plan.csv', 'tw', encoding='utf-8') as f:
            pass

    if not os.path.isfile('data/About.csv'): 
        with open('data/About.csv', 'tw', encoding='utf-8') as f:
            pass

    if not os.path.isfile('data/Fact.csv'): 
        with open('data/Fact.csv', 'tw', encoding='utf-8') as f:
            pass

    if not os.path.isfile('data/Hierarchy.csv'): 
        with open('data/Hierarchy.csv', 'tw', encoding='utf-8') as f:
            pass

    with open('data/Plan.csv', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            planTasksR.append( Task(  parser.parse(row[0]).date(), parser.parse(row[1]).date(), row[2], row[3] ) )
        
    with open('data/Fact.csv', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            factTasksR.append( Task( parser.parse(row[0]).date(), parser.parse(row[1]).date(), row[2], row[3], float(row[4]) ) )

    with open('data/Hierarchy.csv', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            f = list( map(str,row) )
            father = f[0]
            del f[0]
            groups.append( TaskGroup(father, f) )

    with open('data/About.csv', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            about = About( row[0], parser.parse(row[1]).date(), parser.parse(row[2]).date(), row[3])
            

def writePlanTask(task):
    f = open('data/Plan.csv', 'a')
    f.write(str(task.startDate) + ',' + str(task.finishDate) + ',' + str(task.money) + ',' + str(task.name)+ '\n')
    f.close
 
def writeFactTask(task):
    f = open('data/Fact.csv', 'a')
    f.write(str(task.startDate) + ',' + str(task.finishDate) + ',' + str(task.money) + ',' + str(task.name)+ ',' + str(task.isDone)+ '\n')
    f.close

def writeHierarchy(group, tasks):
    import re
    f = open('data/Hierarchy.csv', 'a')
    f.write(str(group) + ',' + str(str(re.sub('\,\s+',',', tasks))) + '\n')
    f.close

def writeAbout(about):
    f = open('data/About.csv', 'w')
    f.write(str(about.projectName) + ',' + str(about.startDate) + ',' + str(about.finishDate) + ',' + str(about.bac) + '\n')
    f.close
   







def generate(nams):

    report.makeReport(nams, planTasksR, factTasksR, groups)


