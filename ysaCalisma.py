# -*- coding: utf-8 -*-
"""
@author: CiciCemal

Tek katmanlı yapay sinir ağı örneği (İleri ve Geri Hesaplama)
"""
import csv
import random as r
import math as m

with open('ysaVeriSeti.csv', 'r') as veri:
    veri_okuma = csv.reader(veri)
    veri = list(veri_okuma)


# .csv uzantılı veri seti okutuldu

satir = len(veri)
sutun = len(veri[1])

# veri setine ait matrisin satır ve sütun değerleri belirlendi

for i in range(satir):
    for j in range(sutun):
        veri[i][j] = float(veri[i][j])

# Her bir hücre değeri ondalık sayıya çevrildi

"""
Tırnakları kaldırarak ve bu yazıyı silerek veri setini 
ekrana matris şeklinde bastırabilirsiniz.

for i in range(satir):
    for j in range(sutun):
        print(round(veri[i][j], 4), end=' ')
    print()
"""

r.shuffle(veri) # Veriler satır sırasına göre rastgele karıştırıldı.

egitim_veri = veri[0:round(satir * 0.8)] 

# Toplam satır sayısının %80'iyle eğitim verisi oluşturuldu.

test_veri = veri[-round(satir * 0.2):]

# Toplam satır sayısının %20'siyle test verisi oluşturuldu.

girdi = int(input("Kaç girdi mevcut: "))
cikti = int(input("Kaç çıktı mevcut: "))
ara_katman = 3

print("{}-{}-{} şeklindeki yapay sinir ağı oluşturuluyor...".format(girdi, ara_katman, cikti))

e_girdi_verileri = [x[:girdi] for x in egitim_veri]
t_girdi_verileri = [x[:girdi] for x in test_veri]

# Eğitim ve Test verileri için girdi matrisi oluşturuldu.

e_cikti_verileri = [x[-cikti:] for x in egitim_veri]
t_cikti_verileri = [x[-cikti:] for x in test_veri]

# Eğitim ve Test verileri için çıktı matrisi oluşturuldu.

iterasyon = 0
sayac = 0
deger = 0
girdi_katmani = []
ara_katmani = []
cikti_katmani = []
g_a_gecis = []
a_c_gecis = []
hata = []

while iterasyon < 5000:
    
    while sayac < len(egitim_veri):
        
        # İleriye eğimli girdi katmanının oluşturulması
        
        for i in range(1):
            girdi_katmani += [[0] * girdi]
    
        for i in range(1):
            for j in range(girdi):
                girdi_katmani[i][j] = e_girdi_verileri[sayac][j]
        
        # İleriye eğimli girdi-ara katman ağırlık matrisinin oluşturulması
        
        if sayac == 0 and iterasyon == 0:
            for i in range(girdi):
                g_a_gecis += [[0] * ara_katman]
        
        
            for i in range(girdi):
                for j in range(ara_katman):
                    sayi = r.uniform(-1.0, 1.0)
                    g_a_gecis[i][j] = sayi
        
                   
        
        """for i in range(girdi):
            for j in range(ara_katman):
                print(round(g_a_gecis[i][j], 6), end=' ')
            print()
        
        print("----------")"""
        
        # İleriye eğimli ara katmanın oluşturulması
        
        for i in range(1):
            ara_katmani = [[0] * ara_katman]

        for i in range(1):
            for j in range(ara_katman):
                for k in range(girdi):
                    deger += girdi_katmani[i][k] * g_a_gecis[k][j]
                ara_katmani[i][j] = deger
                deger = 0
        
        for i in range(1):
            for j in range(ara_katman):
                ara_katmani[i][j] = 1 / (1 + (m.e ** (-ara_katmani[i][j])))
        
                
        # İleriye eğimli ara-çıktı katman ağırlık matrisinin oluşturulması
        
        if sayac == 0 and iterasyon == 0:
            for i in range(ara_katman):
                a_c_gecis += [[0] * cikti]

            for i in range(ara_katman):
                for j in range(cikti):
                    sayi = r.uniform(-1.0, 1.0)
                    a_c_gecis[i][j] = sayi
        
        """for i in range(ara_katman):
            for j in range(cikti):
                print(round(a_c_gecis[i][j], 6), end=' ')
            print()
        
        print("*************")"""
        
        # İleriye eğimli çıktı katmanının oluşturulması
        
        for i in range(1):
            cikti_katmani = [[0] * cikti]

        for i in range(1):
            for j in range(cikti):
                for k in range(ara_katman):
                    deger += ara_katmani[i][k] * a_c_gecis[k][j]
                cikti_katmani[i][j] = deger
                deger = 0
        for i in range(1):
            for j in range(cikti):
                cikti_katmani[i][j] = 1 / (1 + (m.e ** (-cikti_katmani[i][j])))
                
        """
        Bu alan çalıştırıldığında iterasyon x satır sayısı kadar çıktı elde etmeyi sağlar!
        for i in range(1):
            for j in range(cikti):
                print(cikti_katmani[i][j], end=' ')
            print()"""
        
        # Geriye eğilimli hatanın hesaplanması
        for i in range(1):
            hata += [[0] * cikti]
        
        for i in range(1):
            for j in range(cikti):
                hata[i][j] = e_cikti_verileri[sayac][j] - cikti_katmani[i][j]
        
        # Çıktı katmanı içi değiştirilecek hata hesabı
        
        for i in range(1):
            for j in range(cikti):
                cikti_katmani[i][j] = (cikti_katmani[i][j]) * (1 - cikti_katmani[i][j]) * (hata[i][j])
        
        # Ara ve çıkış katmanı arasındaki ağırlık değişim hesabı
        ara_vektor = ara_katmani[0]
        
        cikti_vektor = cikti_katmani[0]
        
        a_c_vektor = [[0.5*i*j for j in cikti_vektor] for i in ara_vektor]
        
        if iterasyon == 0 and sayac == 0:
            a_c_degisim = []
            for i in range(ara_katman):
                a_c_degisim += [[0] * cikti]                
        for i in range(ara_katman):
            for j in range(cikti):
                a_c_degisim[i][j] = a_c_vektor[i][j] + 0.01 * a_c_degisim[i][j]
        
        # Ara katman için değiştirilecek hata hesabı
        
        ara_deger = list()
                       
        for i in range(len(a_c_gecis)):
            sonuc = [x * y for x,y in zip(a_c_gecis[i], cikti_katmani[0])]
            ara_deger.append(sum(sonuc))
        
        ara_katman_degisim = [ara_deger]
        
        for i in range(1):
            for j in range(ara_katman):
                ara_katmani[i][j] = ara_katmani[i][j] * (1 - ara_katmani[i][j]) * ara_katman_degisim[i][j]
        
        
        # Girdi ve ara katmanı arasındaki ağırlık değişim hesabı
        
        girdi_vektor = girdi_katmani[0]
        ara_vektor = ara_katmani[0]        
        g_a_vektor = [[0.5*i*j for j in ara_vektor] for i in girdi_vektor]
        
        if iterasyon == 0 and sayac == 0:
            g_a_degisim = []
            for i in range(girdi):
                g_a_degisim += [[0] * ara_katman]
        
        for i in range(len(girdi_vektor)):
            for j in range(len(ara_vektor)):
                g_a_degisim[i][j] = g_a_vektor[i][j] + 0.01 * g_a_degisim[i][j]
        
        # Ağırlık matrislerinin yeniden belirlenmesi
        
        for i in range(ara_katman):
            for j in range(cikti):
                a_c_gecis[i][j] = a_c_degisim[i][j] + a_c_gecis[i][j]
        
        """for i in range(ara_katman):
            for j in range(cikti):
                print(round(a_c_gecis[i][j], 6), end=' ')
            print()
        
        print("++++++++++++")"""
        
                
        for i in range(girdi):
            for j in range(ara_katman):
                g_a_gecis[i][j] = g_a_degisim[i][j] + g_a_gecis[i][j] 
        
        """for i in range(girdi):
            for j in range(ara_katman):
                print(round(g_a_gecis[i][j], 6), end=' ')
            print()
        
        print("============")"""
        
        
        sayac += 1
         
        
    sayac = 0
    print("{}. iterasyon tamamlandı.".format(iterasyon+1))     
    iterasyon += 1

print("Eğitim Tamamlandı. Test işlemine başlandı.")
sayac = 0

while sayac < len(test_veri):
    
    # İleriye eğimli girdi katmanının oluşturulması
    for i in range(1):
        girdi_katmani += [[0] * girdi]
    
    for i in range(1):
        for j in range(girdi):
            girdi_katmani[i][j] = t_girdi_verileri[sayac][j]
        
        
    # İleriye eğimli ara katmanın oluşturulması
    for i in range(1):
        ara_katmani = [[0] * ara_katman]

    for i in range(1):
        for j in range(ara_katman):
            for k in range(girdi):
                deger += girdi_katmani[i][k] * g_a_gecis[k][j]
            ara_katmani[i][j] = deger
            deger = 0
        
    for i in range(1):
        for j in range(ara_katman):
            ara_katmani[i][j] = 1 / (1 + (m.e ** (-ara_katmani[i][j])))
    
        
    # İleriye eğimli çıktı katmanının oluşturulması
    for i in range(1):
        cikti_katmani = [[0] * cikti]

    for i in range(1):
        for j in range(cikti):
            for k in range(ara_katman):
                deger += ara_katmani[i][k] * a_c_gecis[k][j]
            cikti_katmani[i][j] = deger
            deger = 0
    for i in range(1):
        for j in range(cikti):
            cikti_katmani[i][j] = 1 / (1 + (m.e ** (-cikti_katmani[i][j])))
                
                
    # Hatanın hesaplanması
    for i in range(1):
        hata += [[0] * cikti]
        
    for i in range(1):
        for j in range(cikti):
            hata[i][j] = t_cikti_verileri[i][j] - cikti_katmani[i][j]
    
    hata_deger = hata[0]

    for i in range(len(hata_deger)):
        print("{}. verinin sonuç farkı:".format(i+1), hata_deger[i])
    sayac +=1
    



    