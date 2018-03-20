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