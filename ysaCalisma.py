# -*- coding: utf-8 -*-
"""
@author: CiciCemal

Tek katmanlı yapay sinir ağı örneği (İleri ve Geri Eğilimli Hesaplama)
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

"""
Tırnakları kaldırarak ve bu yazıyı silerek veri setini 
ekrana matris şeklinde bastırabilirsiniz.

for i in range(satir):
    for j in range(sutun):
        print(veri[i][j], end=' ')
    print()
"""

r.shuffle(veri) # Veriler satır sırasına göre rastgele karıştırıldı.

egitim_veri = veri[0:round(satir * 0.8)] 

# Toplam satır sayısının %80'iyle eğitim verisi oluşturuldu.

test_veri = veri[-round(satir * 0.2):]

# Toplam satır sayısının %20'siyle test verisi oluşturuldu.

# Üçüncü ve dördüncü aşama tamamlandı!

girdi = int(input("Kaç girdi mevcut: "))
cikti = int(input("Kaç çıktı mevcut: "))
ara_katman = int(input("Ara katman sayısı kaç olsun istersiniz: "))

print("{}-{}-{} şeklindeki yapay sinir ağı oluşturuluyor...".format(girdi, ara_katman, cikti))

e_girdi_verileri = [x[:girdi] for x in egitim_veri]
t_girdi_verileri = [x[:girdi] for x in test_veri]

# Eğitim ve Test verileri için girdi matrisi oluşturuldu.

e_cikti_verileri = [x[-cikti:] for x in egitim_veri]
t_cikti_verileri = [x[-cikti:] for x in test_veri]

# Eğitim ve Test verileri için çıktı matrisi oluşturuldu.

# Beşinci aşama tamamlandı!

iterasyon = 0
sayac = 0
deger = 0
girdi_katmani = []
ara_katmani = []
cikti_katmani = []
g_a_gecis = []
a_c_gecis = []
hata = []


while iterasyon < 5:
    
    while sayac < len(egitim_veri):
        # İleriye eğimli girdi katmanının oluşturulması
        for i in range(1):
            girdi_katmani += [[0] * girdi]
    
        for i in range(1):
            for j in range(girdi):
                girdi_katmani[i][j] = e_girdi_verileri[sayac][j]
        
        # İleriye eğimli girdi-ara katman ağırlık matrisinin oluşturulması
        for i in range(girdi):
            g_a_gecis += [[0] * ara_katman]
        
        for i in range(girdi):
            for j in range(ara_katman):
                sayi = r.uniform(-1.0, 1.0)
                g_a_gecis[i][j] = sayi
        
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
        
        print("1. ara katman", ara_katmani)
        
        # İleriye eğimli ara-çıktı katman ağırlık matrisinin oluşturulması
        for i in range(ara_katman):
            a_c_gecis += [[0] * cikti]

        for i in range(ara_katman):
            for j in range(cikti):
                sayi = r.uniform(-1.0, 1.0)
                a_c_gecis[i][j] = sayi
        
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
        
        print(a_c_vektor)
                
        if iterasyon == 0:
            a_c_degisim = []
            for i in range(len(ara_vektor)):
                a_c_degisim += [[0] * len(cikti_vektor)]        
        
        for i in range(ara_katman):
            for j in range(cikti):
                a_c_degisim[i][j] = a_c_vektor[i][j] + 0.01 * a_c_degisim[i][j]
           
        ara_katmani_degisim = []
        
        for i in range(ara_katman):
            ara_katmani_degisim += [[0] * 1] 
        
        
        """for i in range(1):
            for j in range(ara_katman):
                ara_katmani[i][j] = (ara_katmani[i][j]) * (1 - ara_katmani[i][j]) * deger
            deger = 0"""
        
        
        
        # Girdi ve ara katmanı arasındaki ağırlık değişim hesabı
        
        girdi_vektor = girdi_katmani[0]
        ara_vektor = ara_katmani[0]        
        g_a_vektor = [[0.5*i*j for j in girdi_vektor] for i in ara_vektor]
        
        if iterasyon == 0:
            g_a_degisim = []
            for i in range(len(girdi_vektor)):
                g_a_degisim += [[0] * ara_vektor]
        
        for i in range(len(girdi_vektor)):
            for j in range(len(ara_vektor)):
                g_a_degisim[i][j] = g_a_vektor[i][j] + 0.01 * g_a_degisim[i][j]
        
        
        for i in range(ara_katman):
            for i in range(cikti):
                a_c_gecis[i][j] = a_c_gecis[i][j] + a_c_degisim[i][j]
        
        for i in range(girdi):
            for i in range(ara_katman):
                g_a_gecis[i][j] = g_a_gecis[i][j] + g_a_degisim[i][j]
        
        sayac += 1
        
         
        
        
        
    iterasyon += 1

    