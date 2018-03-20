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

for i in range(satir):
    for j in range(sutun):
        veri[i][j] = float(veri[i][j])

# Her bir hücre değeri ondalıklı sayıya çevrildi.

# Birinci aşama tamamlandı!

for i in range(satir):
    for j in range(sutun):
        veri[i][j] = abs(veri[i][j] - min(veri[i])) / abs(max(veri[i]) - min(veri[i]))

# Her bir hücre değerinde normalizasyon işlemi gerçekleştirildi.

# İkinci aşama tamamlandı!

r.shuffle(veri) # Veriler satır sırasına göre rastgele karıştırıldı.

egitim_veri = veri[0:round(satir * 0.8)] 
# Toplam satır sayısının %80'iyle eğitim verisi oluşturuldu.

test_veri = veri[-round(satir * 0.2):]
# Toplam satır sayısının %20'siyle test verisi oluşturuldu.

# Üçüncü ve dördüncü aşama tamamlandı!