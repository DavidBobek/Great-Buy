from PyQt5.QtWidgets import QMessageBox,QApplication,QWidget,QScrollArea,QFormLayout,QLabel,QPushButton,QGroupBox,QVBoxLayout
from PyQt5 import QtGui
import sys
class Scrolling(QWidget):
    def __init__(self,_items):
        super().__init__()
        self.title = "scroll area"
        self.left = 500 
        self.top = 200
        self.width_ = 300
        self.height_ = 250
        self.iconName = 'home.png'
        
        
        
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left,self.top,self.width_,self.height_)
        
        
      
        formLayout = QFormLayout()
        groupBox = QGroupBox("This is the groupbox")
        
       
        Labellist = []
        self.button_list = []
        
        var= len(_items)
        for i in range(var):
            Labellist.append(QLabel("hi"))
            self.button_list.append(QPushButton("click"))
            formLayout.addRow(Labellist[i],self.button_list[i])
            
        
        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)
        
        layout = QVBoxLayout()
        layout.addWidget(scroll)
        
        self.setLayout(layout)
        
        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Scrolling(20)
   