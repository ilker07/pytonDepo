

import serial
veri_yolu=serial.Serial('COM6',9600)


while True:

    gelen_deger =veri_yolu.read()

    print("gelen:",gelen_deger[0])
    print("***********************")




