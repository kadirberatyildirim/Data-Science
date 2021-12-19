from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib, sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        title = "SIR Model"
        
        self.setWindowTitle(title)
        self.setGeometry(500, 200, 300, 250)
        
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
        
        self.ContractRateLabel = QtWidgets.QLabel(self.centralwidget)
        self.ContractRateLabel.setObjectName("ContractRateLabel")
        self.ContractRateLabel.setText("Contract Rate")
        self.horizontalLayout.addWidget(self.ContractRateLabel)
        
        self.ContractRateLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ContractRateLineEdit.setObjectName("ContractRateLineEdit")
        self.horizontalLayout.addWidget(self.ContractRateLineEdit)
        
        self.RateofRecoveryLabel = QtWidgets.QLabel(self.centralwidget)
        self.RateofRecoveryLabel.setObjectName("RateofRecoveryLabel")
        self.RateofRecoveryLabel.setText("Rate of Recovery")
        self.horizontalLayout.addWidget(self.RateofRecoveryLabel)
        
        self.RateofRecoveryLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.RateofRecoveryLineEdit.setObjectName("RateofRecoveryLineEdit")
        self.horizontalLayout.addWidget(self.RateofRecoveryLineEdit)
        
        self.GraphItPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.GraphItPushButton.setObjectName("GraphItPushButton")
        self.GraphItPushButton.setText("Graph It")
        self.GraphItPushButton.clicked.connect(self.makeMath)
        self.horizontalLayout.addWidget(self.GraphItPushButton)
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        
        self.whichDayLabel = QtWidgets.QLabel(self.centralwidget)
        self.whichDayLabel.setObjectName("ContractRateLabel")
        self.whichDayLabel.setText("Which Day to plot ?")
        self.horizontalLayout2.addWidget(self.whichDayLabel)
        
        self.whichDayLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.whichDayLineEdit.setObjectName("ContractRateLineEdit")
        self.whichDayLineEdit.setReadOnly(True)
        self.whichDayLineEdit.setPlaceholderText('Only for bar plot')
        self.horizontalLayout2.addWidget(self.whichDayLineEdit)
        
        self.radiobutton1 = QtWidgets.QRadioButton("Line Plot")
        self.radiobutton1.setChecked(True)
        self.radiobutton1.toggled.connect(self.changeLineEdit)
        self.horizontalLayout2.addWidget(self.radiobutton1)
        
        self.radiobutton2 = QtWidgets.QRadioButton("Bar Plot")
        self.radiobutton2.toggled.connect(self.changeLineEdit)
        self.horizontalLayout2.addWidget(self.radiobutton2)
        
        self.verticalLayout.addLayout(self.horizontalLayout2)
        
        self.setCentralWidget(self.centralwidget)
        
    def makeMath(self):
        def calcSusceptible(a, b, S, I):
            	return S - a*I*S
        	
        def calcInfected(a, b, S, I):
            	return I + a*I*S - b*I
        	
        def calcRecovered(b, R, I):
            	return R + b*I
        
        a, b = float(self.ContractRateLineEdit.text()), float(self.RateofRecoveryLineEdit.text()) 
        S, I, R = [0.99], [0.01], [0.00]
        t = list(range(0, 50))
        
        for i in t:
        	S.append(calcSusceptible(a, b, S[i], I[i]))
        	I.append(calcInfected(a, b, S[i], I[i]))
        	R.append(calcRecovered(b, R[i], I[i]))
        
        t.append(50)
        
        if self.radiobutton1.isChecked():
            self._static_ax = self.static_canvas.figure.subplots()
            self._static_ax.plot(t, S, label = 'Susceptible')
            self._static_ax.plot(t, R, color = 'k', label = 'Recovered')
            self._static_ax.plot(t, I, color = 'r', label = 'Infected')
            self.static_canvas.draw()
            
        elif self.radiobutton2.isChecked():
            listForBarPlot = [S[int(self.whichDayLineEdit.text())], I[int(self.whichDayLineEdit.text())], R[int(self.whichDayLineEdit.text())]]
            self._static_ax = self.static_canvas.figure.subplots()
            self._static_ax.bar(['S', 'I', 'R'], listForBarPlot)
            self.static_canvas.draw()
            
    def changeLineEdit(self):
        sender = self.sender()
        if sender.text() == 'Line Plot':
            self.whichDayLineEdit.clear()
            self.whichDayLineEdit.setReadOnly(True)
            self.whichDayLineEdit.setPlaceholderText('Only for bar plot')
        elif sender.text() == 'Bar Plot':
            self.whichDayLineEdit.setReadOnly(False)
                
if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
