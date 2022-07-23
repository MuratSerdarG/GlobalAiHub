import pandas as pd
import numpy as np
import openpyxl

gecen_liste=[] #----->Gecenler listesi ! Kullanılmadı ancak her ihtimale karşı hazırlandı.
kalan_liste=[] #----->Kalanlar listesi ! Kullanılmadı ancak her ihtimale karşı hazırlandı.
okul_no_g=[] #----->Gecenler listesi numara için
okul_no_k=[] #----->Kalanlar listesi numara için
g01l=[] #----->Gecenler listesi isim için
g02l=[] #----->Gecenler listesi soyisim için
k01l=[] #----->Kalanlar listesi isim için
k02l=[] #----->Kalanlar listesi soyisim için
durum_liste=[] #----->Toplam Öğrenci durumlarıyla birlikte kayıt listesi
ogr_sayi=[] #----->Toplam Öğrenci sayacı


def not_gir():
    ad = input("Öğrenci Adı : ")
    soyad = input("Öğrenci Soyadı : ")
    while True:
        okul_no = input("Öğrenci Okul Numarası : ")
        if int(okul_no)>10000 or int(okul_no)<1000:
            print("Lütfen geçerli bir numara giriniz. (Okul numarası aralığı 1000 - 10000 arası olmalıdır.)")
        elif okul_no in durum_liste:
            print("Aynı numara ile oluşturulmuş farklı bir kayıt mevcuttur. Lütfen yeniden deneyiniz.")
        else:
            break
    print("*"*10)
    while True:
        not1 = input("Not 1 : ")
        if int(not1)>100 or int(not1)<0:
            print("Lütfen geçerli bir not giriniz. (Not aralığı 0 - 100 arası olmalıdır.)")
        else:
            break
    while True:
        not2 = input("Not 2 : ")
        if int(not2)>100 or int(not2)<0:
            print("Lütfen geçerli bir not giriniz. (Not aralığı 0 - 100 arası olmalıdır.)")
        else:
            break
    while True:
        not3 = input("Not 3 : ")
        if int(not3)>100 or int(not3)<0:
            print("Lütfen geçerli bir not giriniz. (Not aralığı 0 - 100 arası olmalıdır.)")
        else:
            break
    ortalama=int((int(not1)*0.25+int(not2)*0.25+int(not3)*0.5))
    while True:
        if int(not3)<=49:
            durum="Kaldı"
            break
        else:
            if ortalama<=49:
                durum="Kaldı"
            else:
                durum="Geçti"
            break
    if durum=="Geçti":
        gecen_liste.append(okul_no),gecen_liste.append(ad),gecen_liste.append(soyad),okul_no_g.append(okul_no)
    else:
        kalan_liste.append(okul_no),kalan_liste.append(ad),kalan_liste.append(soyad),okul_no_k.append(okul_no)
    durum_liste.append(okul_no)
    durum_liste.append(ad)
    durum_liste.append(soyad)
    durum_liste.append(durum)
    ogr_sayi.append("1")

def not_oku():
    if len(ogr_sayi)==0:
        print("Henüz Öğrenci Kaydı Gerçekleştirmediniz.")
    else:
        for i in range(len(ogr_sayi)):
            i=i*4
            print("-"*10)
            print("Öğrenci Numarası: ",durum_liste[i],"\n","Öğrenci Adı Soyadı: ",durum_liste[i+1]," ",durum_liste[i+2],"\n","Öğrenci Geçme Durumu: ",durum_liste[i+3],"\n")
            

def gecme_durum():
    if len(ogr_sayi)==0:
        print("Henüz Öğrenci Kaydı Gerçekleştirmediniz.")
    else:
        for i in range(len(durum_liste)):
            if durum_liste[i]=="Geçti":
                work1=1
                break
            else:
                work1=0
        for i in range(len(durum_liste)):
            if durum_liste[i]=="Kaldı":
                work2=1
                break
            else:
                work2=0
        while True:
            if work1==0:
                print("-"*10,"Geçen Öğrenci Listesi","-"*10)
                print("Dersten geçen öğrenci bulunamamıştır.")
                print("-"*43)
                break
            elif work1==1:
                print("-"*10,"Geçen Öğrenci Listesi","-"*10)
                gecenler=pd.DataFrame({"Okul No":okul_no_g})
                for i in range(len(ogr_sayi)):
                    i=(i*4)+1
                    g01l.append(durum_liste[i])
                for i in range(len(ogr_sayi)):
                    i=(i*4)+2
                    g02l.append(durum_liste[i])
                isimler=pd.Series(g01l)
                gecenler["Adı"]=isimler
                soyisimler=pd.Series(g02l)
                gecenler["Soyadı"]=soyisimler
                print(gecenler)
                print("-"*43)
                break
        while True:
            if work2==0:
                print("-"*10,"Kalan Öğrenci Listesi","-"*10)
                print("Dersten kalan öğrenci bulunamamıştır.")
                print("-"*43)
                break
            elif work2==1:
                print("-"*10,"Kalan Öğrenci Listesi","-"*10)
                kalanlar=pd.DataFrame({"Okul No":okul_no_k})
                for i in range(len(ogr_sayi)):
                    i=(i*4)+1
                    k01l.append(durum_liste[i])
                for i in range(len(ogr_sayi)):
                    i=(i*4)+2
                    k02l.append(durum_liste[i])
                isimler=pd.Series(k01l)
                kalanlar["Adı"]=isimler
                soyisimler=pd.Series(k02l)
                kalanlar["Soyadı"]=soyisimler
                print(kalanlar)
                print("-"*43)
                break
def hakkimizda():
    print("-"*40)
    print("Biz Ascendants'ız.")
    print("-"*40)
    #1 Muhbet SAV
    print("Adı Soyadı = Muhbet SAV")
    print("Yaşı ve Mesleği = 22 / Öğrenci")
    print("Programcılık geçmişi ve hedefleri = Bilgisayar programcılığı mezunuyum.Daha sonra istatistik bölümünde lisans ve yüksek lisansımı tamamladım.Şu an aynı bölümde doktora öğrencisiyim ve yapay zeka üzerine çalışmamı sürdürüyorum.")
    print("Proje hakkında fikri=Şuan popüler olan Python dili üzerine yapılacak projelerin ilerleyen aşamalarda farklı araştırmacılar için de bir bilgi kaynağı olacağını ve başlangıç düzeyinde de olsa bu konuda ilerlemelerini sağlayabileceklerini düşünüyorum.")
    print("-"*40)
    #2 Umut ACAR
    print("Adı Soyadı = Umut ACAR")
    print("Yaşı ve Mesleği = 26 / Mimar")
    print("Programcılık geçmişi ve hedefleri=Profesyonel geçmişim yok /Hedeflerim yapay zeka alanında uzmanlaşmak")
    print("Proje hakkında fikri= Projelerin genel manada güncel hayatla bağdaşık olması, daha sonrasında bize yol gösterici ve tekrar kullanılabilir satırlardan oluşması dikkatimi çekti. Gayet faydalı konu seçimleri olduğunu düşünüyorum.")
    print("-"*40)
    #3 Burak DİLBER
    print("Adı Soyadı =Burak DİLBER")
    print("Yaşı ve Mesleği = 32 / PHD student")
    print("Programcılık geçmişi ve hedefleri=Bilgisayar programcılığı mezunuyum.Daha sonra istatistik bölümünde lisans ve yüksek lisansımı tamamladım.Şu an aynı bölümde doktora öğrencisiyim ve yapay zeka üzerine çalışmamı sürdürüyorum.")
    print("Proje hakkında fikri=Şuan popüler olan Python dili üzerine yapılacak projelerin ilerleyen aşamalarda farklı araştırmacılar için de bir bilgi kaynağı olacağını ve başlangıç düzeyinde de olsa bu konuda ilerlemelerini sağlayabileceklerini düşünüyorum.")
    print("-"*40)
    #4 MSG
    print("Adı Soyadı = Murat Serdar GURBETOĞLU")
    print("Yaşı ve Mesleği= 32 / İnsan Kaynakları Yöneticisi")
    print("Programcılık geçmişi ve hedefleri = Bilgisayar ile ilk 1999 yılında tanıştım ve o yıldan bu yana sürekli kullancısı oldum. Artık onu yönlendiren olma fikri bile çok heyecanlı. Matematik kökenliyim. Mesleğim gereği algoritmik düşünce yapılarının temeline hakim olmamı avantaj olarak değerlendiriyorum. Firmaların ihtiyaç duyduğu alanlarda uzmanlaşmış bir Backend Developer olmak istiyorum.")
    print("Proje hakkında fikri= Uzun zamandır farklı platformlarda Python, SQL, Java üzerine eğitimler alıyorum. Ancak ilk defa bir proje içerisinde bizden bekleneni tamamlama fırsatı elde ettim. Bu proje sayesinde Pandas,Numpy kütüphanelerinde de çalışma fırsatı elde ederek daha iyi bir görüntü sağladık.")
    
print("""
*************************************
*     Programlamaya Giriş Dersi     *
*************************************
*      1 - Bilgi Gir                *   
*                                   *      
*      2 - Öğrenci Durum Listeleme  *   
*                                   *
*      3 - Durum Listesi Gör        *
*                                   *
*      4 - Excel'e Aktar            *
*                                   *
*      5 - Hesaplamalar Hakkında     *
*                                   *
*      6 - Hakkımızda                *
*                                   *
*      7 - Global Ai Hakkında        *
*                                   *
*      8 - Çıkış                     *
*                                   *
*************************************
*       Not Sistemi (Global AI)     *
*        A S C E N D A N T S        *
*************************************
""")
while True:
    print("\-/"*25)
    islem = input("Gerçekleştirmek istediğiniz işlem numarasını girin : ")

    if (islem == "1"):
        not_gir()
    elif (islem == "2"):
        not_oku()
    elif (islem == "3"):
        gecme_durum()
    elif (islem == "4"):
        df = pd.DataFrame(columns = ['Numara', 'Ad', 'Soyad', 'Durum'])
        for i in range(len(ogr_sayi)):
            i=i*4
            df = df.append({'Numara' : durum_liste[i], 'Ad' : durum_liste[i+1], 'Soyad' : durum_liste[i+2], 'Durum' : durum_liste[i+3]}, ignore_index = True)
        df.to_excel('Bilgiler.xlsx', sheet_name = "Bilgiler")
        print('Not Bilgileri Excele başarılı bir şekilde aktarılmıştır.')
    elif (islem == "5"):
        print("-"*30)
        print("Öğrenci Not sistemimize hoş geldiniz. Programımıza ilişkin;\n*Puan hesaplamaları Vize + Vize + Final şeklinde hazırlanmıştır.\n*Vizeler ortalamaya %25 etki ederken Final %50 etki etmektedir.\n*Finalden 50 puandan aşağı alınması durumunda direk kalınır.\n*Öğrenci numaraları 1000 ile 10000 arasında olmalıdır.")
        print("-"*30)
 
    elif (islem == "6"):
        hakkimizda()
    elif (islem == "7"):
        print("Global Ai Hakkında:")
        print("""Global Al Hub yapay zeka odaklı sosyal paylaşım platformudur. İsviçre merkezli olan Global Al Hub ülkemizde öne çıkan topluluklar arasında yer alıyor.Eğitimlerin yanı sıra yapay zeka alanına odaklanan bir sosyal paylaşım sitesi olarak konumlanıyor. Global Al Hub tıpkı bir sosyal ağ platformu gibi paylaşım ve mesajlaşma özelliklerine de sahip. Global Al Hub’a üye olan kullanıcılar, platformdaki Python, Machine Learning gibi teknik Hub’lara, Al in Banking, Al in Insurance gibi iş dünyasına yönelik Hublara, Turkish Al Hub, Nigerian Al Hub gibi yerel Hublara katılabiliyor. Ayrıca Global Al Hub’da üyeler Al alanında yaptıkları çalışmaları paylaşabiliyor ve diğer kullanıcılarla etkileşime girebiliyor. Platformun şu anda 18 bin 556 kullanıcısı bulunuyor, 100 bin kullanıcıya ulaştıktan sonra ise reklam ve sponsorluk içerik modellerinin yayına alınması planlanıyor.İsviçre, Almanya, Türkiye haricinde Nijerya, Pakistan, Hindistan gibi ülkelerde de binlerce kişinin katıldığı Python, Machine Learning ve PA alanında eğitimler veriyor.""")
                
    elif (islem == "8"):
        print("Sistemden başarıyla çıkış gerçekleştirdiniz.")
        break
    else:
        print("Geçersiz işlem numarası girdiniz. Lütfen tekrar deneyiniz.")
