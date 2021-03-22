


import serial


veri_index=0
X_SIFIR=0
X_BIR=0
x_yildiz_geldi=0
x_unlem_geldi=0


veri_yolu=serial.Serial('COM6',9600)

#33 unlem ,42 yildiz
while True:

    gelen_deger =veri_yolu.read()
    veri_index+=1
    if(veri_index==1 and gelen_deger[0]==42):
        x_yildiz_geldi=1
    if (veri_index==1 and gelen_deger[0]!=42):
        veri_index=0
        x_yildiz_geldi = 0
        x_unlem_geldi = 0
    if (veri_index ==2 and gelen_deger[0]==33):
        x_unlem_geldi =1
    if (veri_index ==2 and gelen_deger[0] !=33):
        veri_index=0
        x_yildiz_geldi=0
        x_unlem_geldi=0
    if veri_index==3 and x_yildiz_geldi==1 and x_unlem_geldi==1:
        X_SIFIR=gelen_deger[0]
    if veri_index==4 and x_yildiz_geldi==1 and x_unlem_geldi==1:
        X_BIR=gelen_deger[0]
        x_yildiz_geldi=0
        x_unlem_geldi=0

    if veri_index>=4:
        veri_index=0

    print("X0:",X_SIFIR)
    print("X1:",X_BIR)
    print("gelen:",gelen_deger[0])
    print("İndex:",veri_index)
    print("Yildiz:",x_yildiz_geldi)
    print("Unlem:",x_unlem_geldi)

    print("***********************")












