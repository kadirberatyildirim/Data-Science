# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:58:36 2020
@author: kadio
"""

import sys

from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)
        
        static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(static_canvas)
        self.addToolBar(NavigationToolbar(static_canvas, self))
        
        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(dynamic_canvas)
        self.addToolBar(QtCore.Qt.BottomToolBarArea,
                        NavigationToolbar(dynamic_canvas, self))

        self.S,self.I,self.R = self.data()

        self.count = 0;

        self._static_ax = static_canvas.figure.subplots()
        self._static_ax.plot(list(range(51)), self.S)
        self._static_ax.plot(list(range(51)), self.I)
        self._static_ax.plot(list(range(51)), self.R)
        
        self._dynamic_ax = dynamic_canvas.figure.subplots()

        self.ax = self._dynamic_ax.figure.add_axes([0,0,1,1])
        langs = ["S","I","R"]
        self.bars = self.ax.bar(langs, [1,1,1])
        
        self._timer = dynamic_canvas.new_timer(
            100, [(self._update_canvas, (), {})])

        self._timer.start()

    def _update_canvas(self):
        self._dynamic_ax.clear()    
        for bar, h in zip(self.bars, [self.S[self.count],self.I[self.count],self.R[self.count]]):
            bar.set_height(h)

        self.count = self.count +1;

        if(self.count > 49):
            self.count = 0

        self._dynamic_ax.figure.canvas.draw()

    def data(self):
        a = 0.7
        b = 0.2

        S = [0.99]
        I = [0.01]
        R = [0.0]

        for i in range(0,50):
            S.append(S[i]-a*I[i]*S[i])
            I.append(I[i]+a*I[i]*S[i]-b*I[i])
            R.append(R[i]+b*I[i])
        return S, I ,R
        
days = list(range(0,51))

if __name__ == "__main__":

    qapp = QtWidgets.QApplication(sys.argv)

    app = ApplicationWindow()

    app.show()

    qapp.exec_()
