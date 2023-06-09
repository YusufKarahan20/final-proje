from insan import insan
class işsiz(insan):
    #istenilen bilgileri içerecek init metodunu yazıyorum
    def __init__(self,tc_no,ad,soyad,yas,cinsiyet,uyruk,mavi_yaka,beyaz_yaka,yonetici, tecrube= None,statu=None):
        #insan classından inherit ettiğimiz değerlerin kullanılabilmesi için super metodunu kullanıyorum
        super().__init__(tc_no,ad,soyad,yas,cinsiyet,uyruk)
        self.__mavi_yaka = mavi_yaka
        self.__beyaz_yaka = beyaz_yaka
        self.__yonetici = yonetici
        #tecrube sözlüğünün içi boşsa içine girdiğimiz beyaz yaka,mavi yaka ve yönetici tecrubesi değerlerini atıyorum
        if tecrube is None:
            tecrube = {"mavi yaka": mavi_yaka, "beyaz yaka": beyaz_yaka, "yonetici": yonetici}
        self.__tecrube = tecrube
        #statü değerini statu_bul metodu kullanarak bulduruyorum
        if statu is None:
            self.__statu = self.statu_bul()

    # private değerleri güncellemek için get ve set metotlarını yazıyorum
    def get_mavi_yaka_tecrube(self):
        return self.__tecrube["mavi yaka"]
    def set_mavi_yaka_tecrube(self,yeni_mavi_yaka_tecrube):
        self.__mavi_yaka = yeni_mavi_yaka_tecrube

    def get_beyaz_yaka_tecrube(self):
        return self.__tecrube["beyaz yaka"]
    def set_beyaz_yaka_tecrube(self,yeni_beyaz_yaka_tecrube):
        self.__beyaz_yaka = yeni_beyaz_yaka_tecrube

    def get_yonetici_tecrube(self):
        return self.__tecrube["yonetici"]
    def set_yonetici_tecrube(self,yeni_yonetici_tecrube):
        self.__mavi_yaka = yeni_yonetici_tecrube

    def get_statu(self):
        return self.__statu

    # tecrube sözlüğündeki değerlere bakarak statü değeri döndürecek metodu yazıyorum
    def statu_bul(self):
        #sözlükteki değerlerin etki oranını kullanılarak tecrube değişkenlerini oluşturuyorum
        mavi_yaka_tecrube  = self.__tecrube["mavi yaka"]*(20/100)
        beyaz_yaka_tecrube = self.__tecrube["beyaz yaka"]*(35/100)
        yonetici_tecrube = self.__tecrube["yonetici"]*(45/100)
        #tecrube değerlerini karşılaştırıp en büyük değere göre statü döndürüyorum
        if mavi_yaka_tecrube >= beyaz_yaka_tecrube and mavi_yaka_tecrube > yonetici_tecrube:
            return "Mavi yaka"

        elif beyaz_yaka_tecrube >= mavi_yaka_tecrube and beyaz_yaka_tecrube > yonetici_tecrube:
            return "Beyaz yaka"

        elif yonetici_tecrube >= mavi_yaka_tecrube and yonetici_tecrube >= beyaz_yaka_tecrube:
            return "Yönetici"

    # istenilen değerleri string halinde döndürecek str metodunu yazıyorum
    def __str__(self):
        return f"Ad:{self.get_ad()},Soyad:{self.get_soyad()},Statü:{self.get_statu()}"


