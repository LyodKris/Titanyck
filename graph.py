import sys
import numpy as np
import random as rd
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
import pandas as pd
data = pd.read_csv('C:\\D\\t.csv', delimiter=',')

y = data['Pclass']
x = data['PassengerId']
x2 = np.arange(0, 10)
y2 = np.array([3, 5, 7, 9, 15, 8, 10, 6, 5, 20, 5, 17, 9, 5, 18, 10, 16, 5, 2])
plt = pg.plot()
plt2 = pg.plot()

#график со стилем и маркером 
plt.setBackground('0a0a0a')
plt.setXRange(0, 5)
plt.setYRange(0, 5)
plt.setTitle("Simple Line Graph")
plt.showGrid(x=True, y=True)
line = plt.plot(x, y, pen=pg.mkPen('r', width=4), symbol='o', symbolPen='b', symbolSize=8)
#Столбиковая диаграмма
bg = pg.BarGraphItem(x=x2, height=y2, width=0.8, brush='b')
plt2.setLabel('bottom', '<p style="font-size:20px;color:green">X-axis Values</p>')
plt2.setLabel('left', '<p style="font-size:20px;color:green">Y-axis Values</p>')
plt2.setTitle('<h3>Bar Graph using PyQtGraph</h3>')
plt2.addItem(bg)


if __name__ == '__main__':
    if sys.flags.interactive != 1:
        QtGui.QApplication.instance().exec()