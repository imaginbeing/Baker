from PyQt5.QtWidgets import QWidget, QGraphicsScene, QGraphicsEllipseItem, QGraphicsItem 
from Ui_Mainform import Ui_MainWindow ,QtGui
from PyQt5.QtCore import QTimer, QTime
from PyQt5 import QtWidgets
from random import randint

#baggage courier
#multiple

class MainForm(QWidget,Ui_MainWindow):
    def __init__(self): # constr + timers
        super(MainForm,self).__init__()
        self.setupUi(self)
        b:QtWidgets.QPushButton = self.pushButton_order
        b.clicked.connect(self.addOrder)

        a:QtWidgets.QSpinBox  = self.spinBox_Baker
        a.valueChanged.connect(self.addBaker)
  
        c:QtWidgets.QSpinBox  = self.spinBox_courier
        c.valueChanged.connect(self.addCourier)
        
    Orders = [] # orders
    Baking =[] # baking process counter
    StorageCount = 20 # storage size
    TrunkSize = 10 # courier storage
    prevValB = 0
    prevValC = 0
    def Bakers(self): # baker function
        for i in range(self.Orders.__len__()) :
            if(str(self.Orders[i]) != 'done' and  int(self.Orders[i]) > int(self.Baking[i])): 
                if(self.StorageCount <=0):
                    break
                ##self.Orders[i] = str(self.Orders[i]) +'baked' 
                self.Baking[i] +=1
                self.textEdit_output.append("baking" + str(self.Baking[i]))
                self.textEdit_output.append('#####')

                self.Storage() # calls storage update
                break
        
    def Curiers(self): # courier func
        
        bulkcount = 20 - self.StorageCount  # tmp булок на складе
        for i in range(self.Orders.__len__()) : # chech orders
            if(str(self.Orders[i]) != 'done' and  int(self.Orders[i]) <= bulkcount) :
                bulkcount = bulkcount - int(self.Orders[i])
                self.textEdit_output.append('Delivered:' + str(self.Orders[i]) )
                
                self.StorageCount = self.StorageCount + int(self.Orders[i]) # storage update
                self.Orders[i] = 'done' # order complete
                self.Baking[i] = 0 # baking empty
                '''
                while(self.TrunkSize < bulkcount ):
                    for i in range(self.Orders.__len__()) : # chech orders
                        if(str(self.Orders[i]) != 'done' and  int(self.Orders[i]) <= bulkcount) :
                            bulkcount = bulkcount - int(self.Orders[i])
                            self.textEdit_output.append('Delivered:' + str(self.Orders[i]) )
                
                            self.StorageCount = self.StorageCount + int(self.Orders[i]) # storage update
                            self.Orders[i] = 'done' # order complete
                            self.Baking[i] = 0 # baking empty
                '''
                    
                break

        '''
        for i in range(self.Orders.__len__()) : # output
            self.textEdit_output.append(str(self.Orders[i]))
        self.textEdit_output.append('Starege:' + str(self.StorageCount))
        '''

    def Storage(self): # storage (1 counter)
        
        '''
        for i in range(10):
            if(str(self.Storagelist[i]) == 'None' ):
                for  j in range(self.Orders.__len__()) :
                    #if(str(self.Orders[j]).endswith('baked')): 
                    if(str(self.Orders[j]) !='done'and self.Orders[i] > self.Baking[i]): 
                        self.Storagelist[i] = 'Bulka'
                        #self.Orders[j] = 'done'
        for i in range(10):
            
            self.textEdit_output.append(str(self.Storagelist[i]))
            '''
        self.StorageCount -=1
        '''
        for i in range(self.Orders.__len__()) :
            self.textEdit_output.append(str(self.Orders[i]))
        '''

    def addOrder(self): # adding order to list
        s:QtWidgets.QSpinBox = self.spinBox_amount
        Amount = s.value()

        self.textEdit_output.append( 'Ordered: ' + str(Amount))
        self.Orders.append(str(Amount))
        self.Baking.append(0)

    def addBaker(self):
        if( self.spinBox_Baker.value() > self.prevValB):
            self.commonTimer = QTimer(self)
            self.commonTimer.setInterval(2000)
            self.commonTimer.timeout.connect(self.Bakers)
            self.commonTimer.start()
            self.prevValB = self.spinBox_Baker.value()

    def addCourier(self):
        if(self.spinBox_courier.value() > self.prevValC):
            self.courierTimer = QTimer(self)
            self.courierTimer.setInterval(randint(2000,10000))
            self.courierTimer.timeout.connect(self.Curiers)
            self.courierTimer.start()
            self.prevValC = self.spinBox_courier.value()