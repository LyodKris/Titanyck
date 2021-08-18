import sys
import numpy as np
import random as rd
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
import pandas as pd
from PIL import Image    #  pip install Pillow

data = pd.read_csv('C:\\D\\t.csv', delimiter=',')

y = data['Pclass']
x = data['PassengerId']
x2 = [10, 20,30, 40, 50, 60, 100]
y2 = [0, 0, 0, 0 ,0 , 0, 0]
for i in range(len(data)):
    if data.Age[i] < 10:
        y2[0] += 1
        continue
    if data.Age[i] < 20:
        y2[1] += 1
        continue
    if data.Age[i] < 30:
        y2[2] += 1
        continue
    if data.Age[i] < 40:
        y2[3] += 1
        continue
    if data.Age[i] < 50:
        y2[4] += 1
        continue
    if data.Age[i] < 60:
        y2[5] += 1
        continue
    else:
        y2[6] += 1
        continue
plt = pg.plot()
plt2 = pg.plot()

#график со стилем и маркером 
plt.setBackground('ffffbb')
plt.setXRange(0, 5)
plt.setYRange(0, 5)
plt.setTitle("Simple Line Graph")
plt.showGrid(x=False, y=True)
line = plt.plot(x, y, pen=None, symbol='o', symbolPen='b', symbolSize=8)
#Столбиковая диаграмма
bg = pg.BarGraphItem(x=x2, height=y2, width=0.8, brush='b')
plt2.setLabel('bottom', '<p style="font-size:20px;color:green">X-axis Values</p>')
plt2.setLabel('left', '<p style="font-size:20px;color:green">Y-axis Values</p>')
plt2.setTitle('<h3>Bar Graph using PyQtGraph</h3>')
plt2.addItem(bg)
x3 = np.arange(10)
y3 = np.random.normal(size=(3, 10))
plotWidget = pg.plot(title="Three plot curves")
for i in range(3):
    plotWidget.plot(x3, y3[i], pen=(i,3))

imageData = np.asarray(Image.open('C:\D\img.jpg').convert('RGB'))
pg.image (imageData)
if __name__ == '__main__':
    if sys.flags.interactive != 1:
        QtGui.QApplication.instance().exec()