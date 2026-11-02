# Alıştırma 4: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest -v

import pytest

from alistirma import indirim_orani, sepet_toplami, en_pahali_urun


def test_sepet_toplami():
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": 2},
        {"urun": "simit", "fiyat": 15, "adet": 3},
        {"urun": "tost", "fiyat": 60, "adet": 1},
    ]
    assert sepet_toplami(sepet) == 145


# --- indirim_orani ---


@pytest.mark.parametrize(
    "tutar, beklenen",
    [
        (0, 0),
        (99, 0),
        (100, 5),
        (499, 5),
        (500, 10),
        (999, 10),
        (1000, 15),
        (5000, 15),
    ],
)
def test_indirim_orani(tutar, beklenen):
    assert indirim_orani(tutar) == beklenen


def test_indirim_orani_negatif_tutar_hata_verir():
    with pytest.raises(ValueError):
        indirim_orani(-1)


# --- sepet_toplami ---


def test_sepet_toplami_bos_sepet_sifir():
    assert sepet_toplami([]) == 0


def test_sepet_toplami_tek_urun_adet_carpilir():
    assert sepet_toplami([{"urun": "çay", "fiyat": 20, "adet": 5}]) == 100


@pytest.mark.parametrize("adet", [0, -1, -10])
def test_sepet_toplami_gecersiz_adet_hata_verir(adet):
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": 2},
        {"urun": "simit", "fiyat": 15, "adet": adet},
    ]
    with pytest.raises(ValueError):
        sepet_toplami(sepet)


# --- en_pahali_urun ---


def test_en_pahali_urun_bos_sepet_none():
    assert en_pahali_urun([]) is None


def test_en_pahali_urun_tek_urun():
    assert en_pahali_urun([{"urun": "çay", "fiyat": 20, "adet": 1}]) == "çay"


def test_en_pahali_urun_en_yuksek_fiyatli_doner():
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": 1},
        {"urun": "tost", "fiyat": 60, "adet": 1},
        {"urun": "simit", "fiyat": 15, "adet": 1},
    ]
    assert en_pahali_urun(sepet) == "tost"


def test_en_pahali_urun_esitlikte_ilk_gelen_doner():
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": 1},
        {"urun": "tost", "fiyat": 60, "adet": 1},
        {"urun": "kahve", "fiyat": 60, "adet": 1},
    ]
    assert en_pahali_urun(sepet) == "tost"


def test_en_pahali_urun_birim_fiyata_bakar_adede_degil():
    sepet = [
        {"urun": "simit", "fiyat": 15, "adet": 100},
        {"urun": "tost", "fiyat": 60, "adet": 1},
    ]
    assert en_pahali_urun(sepet) == "tost"
