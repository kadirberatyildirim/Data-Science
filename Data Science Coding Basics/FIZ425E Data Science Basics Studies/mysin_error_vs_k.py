from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib, sys
import math
from numba import jit

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        title = "My Sinus"
        
        self.setWindowTitle(title)
        self.setGeometry(300, 200, 300, 250)
        
        self.CreateUI()
        
        self.show()
        
    def CreateUI(self):
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.verticalLayout.addWidget(self.static_canvas)
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.xLabel = QtWidgets.QLabel(self.centralwidget)
        self.xLabel.setObjectName("ContractRateLabel")
        self.xLabel.setText("x")
        self.horizontalLayout.addWidget(self.xLabel)
        
        self.xLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.xLineEdit.setObjectName("ContractRateLineEdit")
        self.horizontalLayout.addWidget(self.xLineEdit)
        
        self.kLabel = QtWidgets.QLabel(self.centralwidget)
        self.kLabel.setObjectName("RateofRecoveryLabel")
        self.kLabel.setText("k")
        self.horizontalLayout.addWidget(self.kLabel)
        
        self.kLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.kLineEdit.setObjectName("RateofRecoveryLineEdit")
        self.horizontalLayout.addWidget(self.kLineEdit)
        
        self.GraphItPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.GraphItPushButton.setObjectName("GraphItPushButton")
        self.GraphItPushButton.setText("Graph It")
        self.GraphItPushButton.clicked.connect(self.makeMath)
        self.horizontalLayout.addWidget(self.GraphItPushButton)
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.setCentralWidget(self.centralwidget)
        
    def makeMath(self):
        @jit
        def calculateMeh():
            x = int(self.xLineEdit.text())
            k = int(self.kLineEdit.text())
            N = 10
            mysum = 0
            mysines = []
            for i in range(k):
                for i in range(N**k):
                    mysum += (-1)**i / math.factorial((2*i + 1)) * x**(2*i + 1)
                mysines.append(mysum)
                mysum = 0
            
            error = []
            for i in range(len(mysines)):
                error.append(abs(mysines[i] - math.sin(x))/math.sin(x)*100)
            return error
        
        myerrors = calculateMeh()
        k = int(self.kLineEdit.text())
        
        self._static_ax = self.static_canvas.figure.subplots()
        self._static_ax.plot(list(range(k)), myerrors)
        self.static_canvas.draw()
                
if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
