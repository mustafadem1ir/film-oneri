# Kullanıcı Girişi
def kullanici_girisi():
    kullanici_adi = input("Kullanıcı Adınızı Girin: ")
    ilgi_duyulan_turler = input("İlgi Duyduğunuz Film Türlerini Virgülle Ayırarak Girin: ").split(",")
    return kullanici_adi, ilgi_duyulan_turler

# Film Tercihlerinin Kaydedilmesi
def tercihleri_kaydet(kullanici_adi, tercihler):
    with open("kullanici_tercihleri.txt", "a") as file:
        file.write(f"{kullanici_adi}: {','.join(tercihler)}\n")

# Öneri Algoritması
def film_oneri(kullanici_tercihleri):
    # Öneri algoritmasını burada geliştirin
    # Kullanıcının tercihlerine uygun filmleri analiz edin ve benzer türlerdeki filmleri önerin
    # Öneri sonuçlarını bir liste olarak döndürün

    # Örnek olarak sabit bir öneri listesi döndürelim
    return ["Film1", "Film2", "Film3"]

# Öneri Sonucunun Gösterilmesi
def oneri_sonucunu_goster(onerilen_filmler):
    print("Önerilen Filmler:")
    for film in onerilen_filmler:
        print(film)

# Ana Program
def main():
    kullanici_adi, ilgi_duyulan_turler = kullanici_girisi()
    tercihleri_kaydet(kullanici_adi, ilgi_duyulan_turler)
    onerilen_filmler = film_oneri(ilgi_duyulan_turler)
    oneri_sonucunu_goster(onerilen_filmler)

if __name__ == "__main__":
    main()
