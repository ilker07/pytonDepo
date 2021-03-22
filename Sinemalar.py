

import Veriler
import Bilgiler
import time
import SeleniumFonksiyonlari
import Degiskenler



for i in range(0,len(SeleniumFonksiyonlari.film_linkleri)):

 yeni_url=SeleniumFonksiyonlari.film_linkleri[i] #Her link için dolaşıyoruz.
 SeleniumFonksiyonlari.browser.get(yeni_url)
 time.sleep(1)


 for eleman in SeleniumFonksiyonlari.filmBilgi():

    SeleniumFonksiyonlari.browser.find_element_by_css_selector(".label")

    if eleman.text.startswith("Vizyon Tarihi") or eleman.text.startswith("Orijinal İsmi") : #a=eleman.text.strip("Vizyon Tarihi")  Bu kod sadece tarihi almak için yazılır.
        continue
    if eleman.text.startswith("Tür"):
        Degiskenler.tur_degeri=Bilgiler.ortakIslemler(eleman.text,"Tür")
    if eleman.text.startswith("Yapımı"):
        Degiskenler.yapim_degeri=Bilgiler.ortakIslemler(eleman.text,"Yapımı")
    if eleman.text.startswith("Süre"):
        Degiskenler.sure_degeri=Bilgiler.ortakIslemler(eleman.text,"Süre")



 #süre yapım tür boş değilse kontrolü yap.Sonra nesneyi oluştur.
 sinema_nesnesi=Veriler.veri(SeleniumFonksiyonlari.filmIsmi().text,Degiskenler.tur_degeri,Degiskenler.yapim_degeri,Degiskenler.sure_degeri)  #1.para film.ismi.text
 with open("C:/Users/Asus/Desktop/yeniFilmler.txt", "a", encoding="UTF-8") as file:
     file.write(sinema_nesnesi.filmIsminiGoster()+"\n")
     file.write(sinema_nesnesi.turuGoster() + "\n")
     file.write(sinema_nesnesi.yapimiGoster() + "\n")
     file.write(sinema_nesnesi.sureyiGoster() + "\n")


SeleniumFonksiyonlari.browser.close()

