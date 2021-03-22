

class veri():

    def __init__(self,film_ismi,tur,yapim,sure):

        self.film_ismi=film_ismi
        self.tur = tur
        self.yapim=yapim
        self.sure=sure


    def filmIsminiGoster(self):

        return self.film_ismi


    def yapimiGoster(self):
        return self.yapim


    def turuGoster(self):

        return  self.tur

    def sureyiGoster(self):

        return self.sure
