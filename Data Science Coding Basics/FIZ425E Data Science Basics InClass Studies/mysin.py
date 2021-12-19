from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import math

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
        
        self.NLabel = QtWidgets.QLabel(self.centralwidget)
        self.NLabel.setObjectName("RateofRecoveryLabel")
        self.NLabel.setText("N")
        self.horizontalLayout.addWidget(self.NLabel)
        
        self.NLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.NLineEdit.setObjectName("RateofRecoveryLineEdit")
        self.horizontalLayout.addWidget(self.NLineEdit)
        
        self.GraphItPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.GraphItPushButton.setObjectName("GraphItPushButton")
        self.GraphItPushButton.setText("Graph It")
        self.GraphItPushButton.clicked.connect(self.makeMath)
        self.horizontalLayout.addWidget(self.GraphItPushButton)
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.outlabel = QtWidgets.QLabel()
        self.verticalLayout.addWidget(self.outlabel)
        
        self.errorlabel = QtWidgets.QLabel()
        self.verticalLayout.addWidget(self.errorlabel)
        
        self.setCentralWidget(self.centralwidget)
        
    def makeMath(self):
        x = int(self.xLineEdit.text())
        N = int(self.NLineEdit.text())
        mysum = 0
        for i in range(N + 1):
            mysum += (-1)**i / math.factorial((2*i + 1)) * x**(2*i + 1)
            
        self.outlabel.setText('My Sine: ' + str(mysum) + ', Real Sine :' + str(math.sin(x)))
        self.errorlabel.setText('Error : ' + str(abs(mysum - math.sin(x))))
                
if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
