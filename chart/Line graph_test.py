 # 取得元 https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Bar_Chart.py 
import PySimpleGUI as sg
import random
import json
import datetime


BAR_WIDTH = 10
# BAR_WIDTH = 5
BAR_SPACING = 16
# BAR_SPACING = 6
EDGE_OFFSET = 3
GRAPH_SIZE = (550,500)
DATA_SIZE = (500,200)
graph = sg.Graph(GRAPH_SIZE, (0,-30), DATA_SIZE, background_color='white',)

layout = [[sg.Text('chart demo')],
          [graph],
          [sg.Button('OK')]]

window = sg.Window('Window Title', layout)

before_value = 0
while True:
    event, values = window.Read()
    graph.Erase()
    if event is None:
        break

    for i in range(30):
        graph_value = random.randint(0, 150)
        if i > 0:
            graph.DrawLine(((i-1) * BAR_SPACING + EDGE_OFFSET+ BAR_WIDTH/2 ,  before_value)  ,  (i * BAR_SPACING + EDGE_OFFSET+ BAR_WIDTH/2 , graph_value ),color='blue', width=1 )

        graph.DrawText(text=graph_value, location=(i*BAR_SPACING+EDGE_OFFSET+2, graph_value+10))

        graph.DrawPoint((i * BAR_SPACING + EDGE_OFFSET+ BAR_WIDTH/2 ,graph_value), size=3 ,color='blue',)
        before_value = graph_value

window.Close()