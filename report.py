import method
import plotly as py                     # pip install plotly==2.0.5
import plotly.figure_factory as ff
import plotly.graph_objects as go
from  plotly.subplots import make_subplots
import datetime

def makeReport(nams, planTasksR, factTasksR, groups):

    names = list(map(str,nams.split(", ")))

    for gr in groups:                           
        if gr.groupName in names:
            names.extend(gr.tasksNames)

    date1 = factTasksR[-1].finishDate
        
    pv = method.funcPV(planTasksR, date1, names)
    ev = method.funcEV(planTasksR, factTasksR, names)
    ac = method.funcAC(factTasksR, date1, names)
    ea = method.funcEA(names, date1)
    cpi = ev/ac
    bac = method.funcBAC(planTasksR)

    ganttFactTasks = []
    for task in factTasksR:                             
        if task.name in names:
            ganttFactTasks.append(task)

    ganttPlanTasks = []
    for task in planTasksR:                             
        if task.name in names:
            ganttPlanTasks.append(task)

    beg=factTasksR[0].startDate 
    end=factTasksR[-1].finishDate + datetime.timedelta(days=2)

    if ganttFactTasks: 
        beg=ganttFactTasks[0].startDate 
        end=ganttFactTasks[-1].finishDate + datetime.timedelta(days=2)

    Tasks=ganttPlanTasks

    specified = True
    if not Tasks:
        Tasks = planTasksR
        #specified = False

    df = []
    for i in range(0, int(len(Tasks))):
        df.append(dict(Task=str(Tasks[i].name), Start=Tasks[i].startDate, Finish=Tasks[i].finishDate, Resouce=str(Tasks[i].name)))
    fig1 = ff.create_gantt(df, bar_width=0.2, title="Плановый график работ", showgrid_x=True, showgrid_y=True)
    fig1['layout'].update(autosize=False, width=1000, height = 390, yaxis=dict(range=[-1,len(planTasksR)]))
    if specified: fig1['layout'].update(xaxis=dict(range=[beg,end]))

    Tasks= ganttFactTasks 
    if not Tasks: 
        Tasks = factTasksR

    df = []
    for i in range(0, int(len(Tasks))):
        df.append(dict(Task=str(Tasks[i].name), Start=Tasks[i].startDate, Finish=Tasks[i].finishDate, Resouce=str(Tasks[i].name)))
    fig2 = ff.create_gantt(df, bar_width=0.2, title="Фактический график работ", showgrid_x=True, showgrid_y=True)
    fig2['layout'].update(autosize=False,width = 1000, height=390, yaxis=dict(range=[-1,len(planTasksR)]))
    if  specified: fig2['layout'].update(xaxis=dict(range=[beg,end]))

    lay = go.Layout(yaxis=dict(range=[0,1]), title='EA')
    fig3 = go.Figure(data=[go.Bar(y=[ea])], layout = lay )
    fig3.update_layout(
        autosize=False,
        width=200,
        height=800,)
    EAgraph = py.offline.plot(fig3, show_link=False, include_plotlyjs=False, output_type='div')

    lay = go.Layout(yaxis=dict(range=[0,pv]), title='EV')
    fig4 = go.Figure(data=[go.Bar(y=[ev])], layout = lay )
    fig4.update_layout(
        autosize=False,
        width=200,
        height=800,)
    EVgraph = py.offline.plot(fig4, show_link=False, include_plotlyjs=False, output_type='div')

    lay = go.Layout(yaxis=dict(range=[0,1]), title='CPI')
    fig5 = go.Figure(data=[go.Bar(y=[cpi])], layout = lay )
    fig5.update_layout(
        autosize=False,
        width=200,
        height=800,)
    CPIgraph = py.offline.plot(fig5, show_link=False, include_plotlyjs=False, output_type='div')
        

    graph1 = py.offline.plot(fig1, show_link=False, include_plotlyjs=False, output_type='div')
    graph2 = py.offline.plot(fig2, show_link=False, include_plotlyjs=False, output_type='div')


    html_string = '''
        <html>
            <head>
              <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
              <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
              <style>body{ margin:0 100; background:white; }
                  .graphs {
                      display: flex;
                      flex-direction: row;
                  }
                  .gantt {
                      display: flex;
                      flex-direction: column;
                  }
                  .inds {
                      
                  }
              </style>
            </head>
            <body>
              <h1>Отчет</h1>
              <div class = "graphs">
                  <div class="gantt">
                      <div class="1 graph">
                        ''' + graph1 + '''
                      </div>
                      <div class="1.1 graph">
                        ''' + graph2 + '''
                      </div>
                  </div>
                      <div class="2 graph">
                      ''' + EAgraph + '''
                      </div>
                      <div class="3 graph">
                      ''' + EVgraph + '''
                      </div>
                      <div class="4 graph">
                      ''' + CPIgraph + '''
                      </div>    
              </div>
            </body>
        </html>'''

    with open("report.html", 'w') as f:
        f.write(html_string)
        f.close()













