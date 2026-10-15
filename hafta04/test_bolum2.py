# Lab, Bölüm 2: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum2.py test_hatali_surumler.py -v

import pytest

from bolum2 import sifre_gucu, otopark_ucreti, yuzde_degisim


# sifre_gucu

def test_kisa_sifre_zayif():
    assert sifre_gucu("abc") == "zayıf"


def test_sifre_bir_karakter_zayif():
    assert sifre_gucu("a") == "zayıf"


def test_sifre_7_karakter_zayif():
    assert sifre_gucu("a" * 7) == "zayıf"


def test_sifre_8_karakter_orta():
    assert sifre_gucu("a" * 8) == "orta"


def test_sifre_11_karakter_orta():
    assert sifre_gucu("a" * 11) == "orta"


def test_sifre_12_karakter_guclu():
    assert sifre_gucu("a" * 12) == "güçlü"


def test_uzun_sifre_guclu():
    assert sifre_gucu("a" * 30) == "güçlü"


def test_bos_sifre_hata_firlatir():
    with pytest.raises(ValueError):
        sifre_gucu("")


# otopark_ucreti

def test_otopark_negatif_dakika_hata_firlatir():
    with pytest.raises(ValueError):
        otopark_ucreti(-1)


def test_otopark_0_dakika_ucretsiz():
    assert otopark_ucreti(0) == 0


def test_otopark_15_dakika_ucretsiz():
    assert otopark_ucreti(15) == 0


def test_otopark_16_dakika_20_tl():
    assert otopark_ucreti(16) == 20


def test_otopark_60_dakika_20_tl():
    assert otopark_ucreti(60) == 20


def test_otopark_61_dakika_40_tl():
    assert otopark_ucreti(61) == 40


def test_otopark_180_dakika_40_tl():
    assert otopark_ucreti(180) == 40


def test_otopark_181_dakika_60_tl():
    assert otopark_ucreti(181) == 60


def test_otopark_cok_uzun_sure_60_tl():
    assert otopark_ucreti(1000) == 60


# yuzde_degisim

def test_yuzde_artis():
    assert yuzde_degisim(200, 250) == pytest.approx(25.0)


def test_yuzde_azalis():
    assert yuzde_degisim(200, 150) == pytest.approx(-25.0)


def test_yuzde_degisim_yok():
    assert yuzde_degisim(100, 100) == pytest.approx(0.0)


def test_yuzde_ondalikli_sonuc():
    assert yuzde_degisim(3, 4) == pytest.approx(33.3333, rel=1e-4)


def test_yuzde_eski_deger_sifir_hata_firlatir():
    with pytest.raises(ValueError):
        yuzde_degisim(0, 50)
