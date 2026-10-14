# Hafta 3: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest -v

import pytest

from alistirma import kargo_ucreti, bilet_fiyati, ortalama


#Kargo ücreti

def test_kargo_buyuk_sipariste_ucretsiz():
    assert kargo_ucreti(800) == 0


def test_kargo_kucuk_sipariste_ucretli():
    assert kargo_ucreti(100) == 50


def test_kargo_tam_sinirda_ucretsiz():
    assert kargo_ucreti(500) == 0


def test_kargo_sinirin_bir_altinda_ucretli():
    assert kargo_ucreti(499) == 50


def test_kargo_sinirin_bir_ustunde_ucretsiz():
    assert kargo_ucreti(501) == 0


def test_kargo_sifir_tutar_gecerli():
    assert kargo_ucreti(0) == 50


def test_kargo_negatif_tutar_hata_verir():
    with pytest.raises(ValueError):
        kargo_ucreti(-1)


#Müze bileti

def test_bilet_ucretsiz_yas_araligi():
    assert bilet_fiyati(0) == 0
    assert bilet_fiyati(3) == 0


def test_bilet_ucretsiz_ust_sinir():
    assert bilet_fiyati(6) == 0


def test_bilet_ogrenci_alt_sinir():
    assert bilet_fiyati(7) == 50


def test_bilet_ogrenci_yas_araligi():
    assert bilet_fiyati(12) == 50


def test_bilet_ogrenci_ust_sinir():
    assert bilet_fiyati(17) == 50


def test_bilet_tam_alt_sinir():
    assert bilet_fiyati(18) == 100


def test_bilet_tam_yas_araligi():
    assert bilet_fiyati(40) == 100


def test_bilet_tam_ust_sinir():
    assert bilet_fiyati(64) == 100


def test_bilet_yasli_alt_sinir():
    assert bilet_fiyati(65) == 60


def test_bilet_yasli_yas_araligi():
    assert bilet_fiyati(90) == 60


def test_bilet_negatif_yas_hata_verir():
    with pytest.raises(ValueError):
        bilet_fiyati(-1)


#Not ortalaması

def test_ortalama_kusuratli_sonuc():
    assert ortalama([70, 85]) == 77.5


def test_ortalama_tam_sayi_sonuc():
    assert ortalama([60, 80, 100]) == 80


def test_ortalama_tek_elemanli_liste():
    assert ortalama([42]) == 42


def test_ortalama_bos_liste_hata_verir():
    with pytest.raises(ValueError):
        ortalama([])
