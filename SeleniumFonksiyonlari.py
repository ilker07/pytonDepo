

from  selenium import webdriver
import time




def filmIsmi():
    return browser.find_element_by_css_selector("h1.left")  # Filmin ismini aldık.
def filmBilgi():
    return browser.find_elements_by_css_selector(".info-group")  # Film bilgilerini aldıkTür,Yapım vs.



i=12

film_linkleri=[]
while(i>0):
 browser=webdriver.Chrome(executable_path=r"C:\Users\Asus\Desktop\chromedriver.exe")

 url="https://www.sinemalar.com/kullanici/ilkeraykut7/listeleri/16846/yeni-filmler?page="+str(i) #44tu.https://www.sinemalar.com/kullanici/ilkeraykut7/izledikleri/filmler/"+str(i)
 #https://www.sinemalar.com/kullanici/ilkeraykut7/listeleri/8121/izlicem?page=     i=106
 browser.get(url)



 time.sleep(1)

 filmler=browser.find_elements_by_css_selector('a.user-list-size.relative') #a tag ı içindeki user-list-size.relative.shadow classı.(a.user-list-size.relative.shadow)
 i -=1


 for film in filmler:

  film_linkleri.append(film.get_attribute('href'))  #Sayfadaki Linkleri aldık.

