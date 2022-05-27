from PyQt5.QtWidgets import QMessageBox,QApplication,QWidget,QScrollArea,QFormLayout,QLabel,QPushButton,QGroupBox,QVBoxLayout
from PyQt5 import QtGui
import sys
class Scrolling(QWidget):
    def __init__(self,_items):
        super().__init__()
        self.title = "scroll area"
        self.left = 500 
        self.top = 200
        self.width_ = 500
        self.height_ = 400
    
        
        
        
      
        self.setGeometry(self.left,self.top,self.width_,self.height_)
        
        
      
        formLayout = QFormLayout()
        groupBox = QGroupBox("Products to pick from")
        
       
        self.Labellist = []
        self.button_list = {}
        
        var= len(_items)
        for i in range(var):
            self.Labellist.append(QLabel("hi"))
            self.button_list[i] = QPushButton("click")
            formLayout.addRow(self.Labellist[i],self.button_list[i])
            
        
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
   