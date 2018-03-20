# yapaySinirAglari

Aldığım "Yapay Sinir Ağları" dersinde el ile öğretilen formüllerin Python dili ile Kodlanması her bir çalışmanın aşamaları mevcuttur. Bu aşamalar şu şekildedir:

Çalışma mantığı şu şekilde:

    1. Dışarıdan csv uzantılı dosya okuma işlemi gerçekleştir. (Tamamlandı) 
    2. Her bir veri için normalizasyon işlemi gerçekleştir. 
    Formül ni = (xi - minj) / maxj-minj (Tamamlandı)
    3. Okunan verilerin satır satısının %80'ini alarak 0 ile %80'i alınan
    sayı arasında iadesiz örnekleme yaparak yeniden matris eğitim verisini
    oluştur.
    4. Okunan verilerin satır satısının %20'ini alarak 0 ile %20'i alınan
    sayı arasında iadesiz örnekleme yaparak yeniden matris eğitim verisini
    oluştur.
    5. Dışarıdan kaç sütunun x değerleri, kaç sutünun y değerleri olduğunu sor
    ve alınan sayılara göre de girdi matrisi ve beklenen çıktı matrisi oluştur.
    6. Her bir eğitim verisi için:
        1. İlk iterasyonda ileriye doğru hesaplama:
            1. Ağırlık matrisleri [-1,1] arasında rassal olacak.
        2. İkinci iterasyonda geriye doğru hesaplama:
            1. Ağırlık değişim matrisi ilk önce 0 alınacak.
        3. Sonraki iterasyonlarda ileri doğru hesaplama:
            1. Ağırlık matrisleri ilk iterasyondaki geriye doğru hesabı
            sonucunda bulunan ağırlık matrisi ile ilk iterasyonda oluşturulan
            ağırlık matrisi ile toplanacak.
        4. Sonraki itereayonlarda geriye doğru hesaplama:
            1. İlk iterasyonda oluşturulan ağırlık değişim matrisi değeri 
            kullanılarak sonraki iterasyonlar için ağırlık matrisi oluşturulacak.
    7. Her bir test verisi için:
        1. Herbir çıktı değerindeki hata oranlarını bularak bu oranların
        ortalama olarak değerini bul! Bu şekilde yapay sinir ağının performansını
        ölç!
