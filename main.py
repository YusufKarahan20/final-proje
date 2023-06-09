#kullanacağımız classları import ediyoruz
from insan import insan
from işsiz import işsiz
from çalışan import çalışan
from maviyaka import maviyaka
from beyazyaka import beyazyaka
import pandas as pd
#dataframe'i görebilmek için görüntülenen maksimum sütün saysını arttırıyorum
pd.set_option("display.max_columns", 15)
#örneklerimi girip ekrana yazdırıyorum
insan_1 = insan(tc_no=13579,ad="yusuf",soyad="karahan",yas=18,cinsiyet="erkek",uyruk="türk")
insan_2 = insan(tc_no=24680,ad="emre",soyad="çavdar",yas=19,cinsiyet="erkek",uyruk="fransız")
print(insan_1.__str__(),"\n",insan_2.__str__(),"\n")
insan_3 = işsiz(tc_no=25800,ad="furkan",soyad="harmandalı",yas=47,cinsiyet="erkek",uyruk="alman",mavi_yaka=5,beyaz_yaka=8,yonetici=10)
insan_4 = işsiz(tc_no=24200,ad="bugra",soyad="zorlu",yas=41,cinsiyet="erkek",uyruk="italyan",mavi_yaka=0,beyaz_yaka=4,yonetici=3)
insan_5 = işsiz(tc_no=23200,ad="ayça",soyad="çelik",yas=34,cinsiyet="kadın",uyruk="ispanyol",mavi_yaka=9,beyaz_yaka=3,yonetici=0)
print(insan_3.__str__(),"\n",insan_4.__str__(),"\n",insan_5.__str__(),"\n")
insan_6 = çalışan(tc_no=12345,ad="yeşim",soyad="yeşil",yas=44,cinsiyet="kadın",uyruk="ingiliz",sektor="teknoloji",tecrube=77,maas=50000,yeni_maas=0)
insan_7 = çalışan(tc_no=67890,ad="defne",soyad="toprak",yas=28,cinsiyet="kadın",uyruk="rus",sektor="insaat",tecrube=99,maas=20000,yeni_maas=0)
insan_8 = çalışan(tc_no=11111,ad="ipek",soyad="seçkin",yas=35,cinsiyet="kadın",uyruk="türk",sektor="muhasebe",tecrube=36,maas=18000,yeni_maas=0)
print(insan_6.__str__(),"\n",insan_7.__str__(),"\n",insan_8.__str__(),"\n")
insan_9 = maviyaka(tc_no=22222,ad="arda",soyad="kayık",yas=64,cinsiyet="erkek",uyruk="türk",sektor="teknoloji",tecrube=120,maas=25000,yeni_maas=0,yipranma_payi=0.6)
insan_10 = maviyaka(tc_no=33333,ad="dursun",soyad="kazma",yas=58,cinsiyet="erkek",uyruk="türk",sektor="teknoloji",tecrube=89,maas=36000,yeni_maas=0,yipranma_payi=0.3)
insan_11 = maviyaka(tc_no=44444,ad="barış",soyad="çekiç",yas=44,cinsiyet="erkek",uyruk="türk",sektor="diger",tecrube=125,maas=33000,yeni_maas=0,yipranma_payi=0.8)
print(insan_9.__str__(),"\n",insan_10.__str__(),"\n",insan_11.__str__(),"\n")
insan_12 = beyazyaka(tc_no=55555,ad="merve",soyad="köksal",yas=33,cinsiyet="kadın",uyruk="türk",sektor="teknoloji",tecrube=28,maas=55000,yeni_maas=0,tesvik_primi=500)
insan_13 = beyazyaka(tc_no=66666,ad="ecem",soyad="su",yas=59,cinsiyet="kadın",uyruk="türk",sektor="insaat",tecrube=15,maas=28000,yeni_maas=0,tesvik_primi=600)
insan_14 = beyazyaka(tc_no=77777,ad="batu",soyad="ankastre",yas=64,cinsiyet="erkek",uyruk="türk",sektor="muhasebe",tecrube=34,maas=45000,yeni_maas=0,tesvik_primi=250)
print(insan_12.__str__(),"\n",insan_13.__str__(),"\n",insan_14.__str__(),"\n")
#dataframe'de kullanacağım nesneleri listeye atıyorum
nesneler = [insan_6,insan_7,insan_8,insan_9,insan_10,insan_11,insan_12,insan_13,insan_14,]
#dataframe oluşturmak için kullanacağım sözlüğü oluşturuyorum
sözlük = {"tc_no": [], "ad": [], "soyad": [], "yas": [], "cinsiyet": [], "uyruk": [], "sektor": [], "tecrube(ay)": [], "maas": [],"yeni maas": [] ,"yıpranma_payi": [], "tesvik_primi": [],"çalışan_tipi": []}
#nesneler listesindeki her bir nesne için dönecek for döngüsünü açıyorum
for nesne in nesneler:
    #nesnenin yeni maaş değerinin hesaplanması için zam_hakki metodu çağırıyorum
    nesne.zam_hakki()
    #her bir nesnenin gerekli değerlerini sözlüğe kaydediyorum
    sözlük["tc_no"].append(nesne.get_tc_no())
    sözlük["ad"].append(nesne.get_ad())
    sözlük["soyad"].append(nesne.get_soyad())
    sözlük["yas"].append(nesne.get_yas())
    sözlük["cinsiyet"].append(nesne.get_cinsiyet())
    sözlük["uyruk"].append(nesne.get_uyruk())
    sözlük["sektor"].append(nesne.get_sektor())
    sözlük["tecrube(ay)"].append(nesne.get_tecrube())
    sözlük["maas"].append(nesne.get_maas())
    sözlük["yeni maas"].append(nesne.get_yeni_maas())
    sözlük["çalışan_tipi"].append(type(nesne).__name__)
    #istenilen değerin nesnede bulunmaması halinde try-except kullanarak sözlükte o değerlerin None değerini almasını sağlıyorum
    try:
        sözlük["yıpranma_payi"].append(nesne.get_yipranma_payi())
    except AttributeError:
        sözlük["yıpranma_payi"].append(None)
    try:
        sözlük["tesvik_primi"].append(nesne.get_tesvik_primi())
    except AttributeError:
        sözlük["tesvik_primi"].append(None)
#pandas modülünü kullanarak sözlükten dataframe oluşturuyorum ve ekrana yazdırıyorum
df = pd.DataFrame(sözlük).fillna(0)
print(df)


#shape metodu kullanarak maaşı 15000'den fazla olanları yazdırıyorum
maas__15000__uzeri = df[df["maas"] > 15000].shape[0]
print("\nMaaşı 15000 TL üzerinde olanların toplam sayısı:", maas__15000__uzeri)
#dataframedeki değerleri çalışan tipine göre gruplandırıp her grubun ortalama maaş ve tecrübesini ekrana yazdırıyorum
gruplanmis_df = df.groupby("çalışan_tipi").agg({"yeni maas": "mean", "tecrube(ay)": "mean"})
print("\nÇalışan Tiplerine Göre Ortalama Maaş ve Tecrübe:")
print(gruplanmis_df)
#yeni maaş değerine df sıralıyorum
sıralı_df = df.sort_values("yeni maas")
print("\nyeni maaş değerine göre sıralanmış dataframe:")
print(sıralı_df)
#ay halindeki tecrube değerini yıl haline getirip 3 seneden fazla olan beyaz yakalıları yazdırıyorum
print("\nTecrübesi 3 seneden fazla olan Beyaz yakalılar:")
filtre = (df["çalışan_tipi"] == "BeyazYaka") & ((df["tecrube(ay)"]/12) >= 3)
print(df.loc[filtre])
print("\nYeni maaşı 10000 TL üzerinde olanlar için; 2-5 satır arası olanları, tc_no ve yeni_maaş sütunları:")
filtre = (df['yeni maas'] > 10000) & (df.index > 2) & (df.index < 5)
print(df.loc[filtre, ['tc_no', 'yeni maas']])
#istenilen sütunlar alınıp yeni df oluşturuyorum
print("\nyeni dataframe:")
yeni_df = df[["ad","soyad","sektor","yeni maas"]]
print(yeni_df)
