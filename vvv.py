

import sys
import serial
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import serial.tools.list_ports

a=1




class Pencere(QWidget):
        def __init__(self):
            super().__init__()
            self.durum=False
            self.i=0
            self.x = 0
            self.X_SIFIR = 0
            self.X_BIR = 0
            self.veri_index = 0
            self.baglandi=False

            self.git()
        def git(self):

            v_box1 = QVBoxLayout()
            h_box1= QHBoxLayout()
            h_box2=QHBoxLayout()



            self.setWindowTitle("STM32-Python Haberleşmesi")

            self.portComboBox = QComboBox()
            self.ports = serial.tools.list_ports.comports()  # Com portlar listelendi.
            for i in self.ports:
                self.portComboBox.addItem(str(i))

            self.baglanButon = QPushButton("Bağlan")
            h_box1.addWidget(self.portComboBox)
            h_box1.addStretch()
            h_box1.addWidget(self.baglanButon)

            self.baglanButon.clicked.connect(self.baglanma)



            self.xBirYazi=QLabel("X1:")
            self.xBirDeger=QLabel("0  ")

            self.xIkiYazi=QLabel("X2:")
            self.xIkiDeger=QLabel("0  ")

            h_box2.addWidget(self.xBirYazi)
            h_box2.addWidget(self.xBirDeger)
            h_box2.addWidget(self.xIkiYazi)
            h_box2.addWidget(self.xIkiDeger)
            h_box2.addStretch()

            v_box1.addLayout(h_box1)
            v_box1.addLayout(h_box2)

            self.timer = QTimer()
            self.timer.timeout.connect(self.dongu)


            self.setLayout(v_box1)

            #self.setFixedSize(270, 100)
            if (a == 1):
                self.show()
        def dongu(self):
            print("Burada")
            if (self.veri_yolu.in_waiting != 0):
                gelen_deger = self.veri_yolu.read()

                self.veri_index += 1
                if self.veri_index == 1:
                    if gelen_deger[0] != 42:
                        self.veri_index = 0

                elif self.veri_index == 2:
                    if gelen_deger[0] != 33:
                        self.veri_index = 0
                elif self.veri_index == 3:
                    self.X_SIFIR = gelen_deger[0]
                elif self.veri_index == 4:
                    self.X_BIR = gelen_deger[0]
                    self.veri_index = 0

                    self.xBirDeger.setText(str(self.X_SIFIR))
                    self.xIkiDeger.setText(str(self.X_BIR))
                    print("X0:", self.X_SIFIR)
                    print("X1:",self. X_BIR)
                    print("**********************")

        def baglanma(self):


            self.portText = self.portComboBox.currentText()  # port combobox'ın içinde hangi değer varsa çekildi.
            if(self.portText !=""):
             self.port = self.portText.split()  # combo box'ın içerisinde bize lazım olan sadece "COM13" kısmı. Bu yüzden split ile kelimeler ayrıldı.
             self.veri_yolu = serial.Serial(self.port[0], 9600)
             self.baglanButon.setEnabled(False)
             self.baglandi=True
            else:

                self.baglanButon.setEnabled(False)
                QTimer.singleShot(1000, lambda: self.baglanButon.setDisabled(False))
                self.baglandi=False
            if(self.baglandi):
                print("Burada")
                self.timer.start(100)

                '''
                while True:
                    #print("Girdi")
                    gelen_deger = self.veri_yolu.read()

                    veri_index += 1
                    if veri_index == 1:
                        if gelen_deger[0] != 42:
                            veri_index = 0

                    elif veri_index == 2:
                        if gelen_deger[0] != 33:
                            veri_index = 0
                    elif veri_index == 3:
                        X_SIFIR = gelen_deger[0]
                    elif veri_index == 4:
                        X_BIR = gelen_deger[0]
                        veri_index = 0
                    
                    self.xBirDeger.setText("55")
                    self.xIkiDeger.setText(str(X_BIR))
                    print("X0:", X_SIFIR)
                    print("X1:", X_BIR)
                    print("**********************")
                    '''

        def closeEvent(self, event):

            reply = QMessageBox.question(
                self, "Uyarı",
                "Çıkmak istiyor musunuz?",
                 QMessageBox.Close | QMessageBox.Cancel,
                )

            if reply == QMessageBox.Close:
                event.accept()
                if(self.x==1):
                 self.timer.stop()
                 self.veri_yolu.close()



            else:
                event.ignore()






app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())










'''
import serial


veri_index=0
X_SIFIR=0
X_BIR=0



veri_yolu=serial.Serial('COM6',9600)

#33 unlem ,42 yildiz
while True:

    gelen_deger =veri_yolu.read()
    veri_index+=1
    if veri_index==1:
        if  gelen_deger[0]!=42:
            veri_index = 0

    elif veri_index ==2:
        if  gelen_deger[0]!=33:
            veri_index = 0
    elif veri_index==3 :
        X_SIFIR=gelen_deger[0]
    elif veri_index==4:
        X_BIR=gelen_deger[0]
        veri_index = 0


    print("X0:",X_SIFIR)
    print("X1:",X_BIR)
    print("gelen:",gelen_deger[0])
    print("İndex:",veri_index)


    print("***********************")



'''
