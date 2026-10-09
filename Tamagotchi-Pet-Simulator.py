import os
import time
from random import choice, randrange


# Ana Sınıf (Base Class)
class Pet:

    def __init__(self, isim):
        self.isim = isim
        self.yem = 5  # Max 10
        self.enerji = 5  # Max 10
        self.saglik = 10  # Max 10
        self.mutluluk = 5  # Max 10
        self.soz = ["Purrr...", "Meowww!", "Mrrrp?"]

    def __zaman_akisi(self):
        """Her hamlede zaman geçer ve değerler doğal olarak düşer"""
        self.yem -= 1
        self.mutluluk -= 1

        # Eğer çok acıktıysa veya hiç enerjisi kalmadıysa sağlığı düşsün
        if self.yem <= 1 or self.enerji <= 1:
            self.saglik -= 2
            print(f"\n {self.isim} kendini hiç iyi hissetmiyor! (Canı düştü)")

        # Sınırlandırmalar
        self.yem = max(0, min(10, self.yem))
        self.enerji = max(0, min(10, self.enerji))
        self.saglik = max(0, min(10, self.saglik))
        self.mutluluk = max(0, min(10, self.mutluluk))

    def bar_goster(self, deger, max_deger=10):
        """[█████░░░░░] şeklinde durum çubuğu çizer"""
        dolu = "█" * deger
        bos = "░" * (max_deger - deger)
        return f"[{dolu}{bos}] {deger}/{max_deger}"

    @property
    def ascii_art(self):
        """Hayvanın ruh haline göre resmini döndürür"""
        if self.saglik <= 3:
            return """
               /\_/\  
              ( x.x )  <-- (Hastalandı / Çok Halsiz)
               > ^ <  
            """
        elif self.enerji <= 2:
            return """
               /\_/\  
              ( -.- ) zzz <-- (Çok Uykusu Var)
               > ^ <  
            """
        elif self.mutluluk >= 7:
            return """
               /\_/\  
              ( ^.^ ) <3 <-- (Çok Mutlu!)
               > ^ <  
            """
        else:
            return """
               /\_/\  
              ( o.o )  
               > ^ <  
            """

    def status(self):
        """Oyun ekranını çizer"""
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 40)
        print(f"      TAMAGOTCHI - {self.isim.upper()}")
        print("=" * 40)
        print(self.ascii_art)
        print(f" Can (Sağlık): {self.bar_goster(self.saglik)}")
        print(f" Açlık Durumu: {self.bar_goster(self.yem)}")
        print(f" Enerji      : {self.bar_goster(self.enerji)}")
        print(f" Mutluluk    : {self.bar_goster(self.mutluluk)}")
        print("=" * 40)

    def feed(self):
        if self.yem >= 10:
            print(f"\n{self.isim} zaten tıka basa dolu!")
        else:
            print(f"\n🍖 {self.isim} yemeğini afiyetle yedi!")
            self.yem += 3
            self.enerji += 1
            self.__zaman_akisi()

    def play(self):
        if self.enerji <= 2:
            print(f"\n {self.isim} çok yorgun, oyun oynayamaz! Önce uyutmalısın.")
        else:
            print(f"\n {self.isim} ile koşturdunuz, çok eğlendi!")
            self.mutluluk += 3
            self.enerji -= 2
            self.__zaman_akisi()

    def sleep(self):
        print(f"\n🌙 {self.isim} kıvrıldı ve uykuya daldı... zzz")
        time.sleep(2)  # Bekleme efekti
        self.enerji = 10
        self.yem -= 2
        print(f"\n {self.isim} uyandı! Enerjisi tavan yaptı.")
        self.__zaman_akisi()

    def heal(self):
        if self.saglik >= 10:
            print(f"\n {self.isim} zaten turp gibi!")
        else:
            print(f"\n {self.isim}'e vitamin ve ilaç verdin.")
            self.saglik += 4
            self.__zaman_akisi()


# Pet sınıfından türeyen Kedi Sınıfı (OOP Inheritance)
class Cat(Pet):

    def teach_word(self, word):
        self.soz.append(word)
        print(f"\n {self.isim} yeni bir ses/kelime öğrendi: '{word}'")
        self._Pet__zaman_akisi()

    def talk(self):
        ses = choice(self.soz)
        print(f"\n {self.isim} sana baktı ve dedi ki: '{ses}'")
        self._Pet__zaman_akisi()


# Oyun Döngüsü
def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("🐾 TAMAGOTCHI PET SIMULATOR 🐾\n")
    isim = input("Kedine bir isim ver (Örn: Abbas): ").strip()
    if not isim:
        isim = "Abbas"

    pet = Cat(isim)

    while True:
        pet.status()

        # Sağlık 0 olduysa oyun biter
        if pet.saglik <= 0:
            print(
                f"\n Maalesef {pet.isim} hastalandı ve bayıldı... Oyunu kaybettin!"
            )
            break

        print("\n1 - Besle (Feed)")
        print("2 - Oyna (Play)")
        print("3 - Uyut (Sleep)")
        print("4 - İlaç/Tedavi Et (Heal)")
        print("5 - Konuş (Talk)")
        print("6 - Yeni Kelime Öğret")
        print("0 - Çıkış")

        secim = input("\nNe yapmak istersin?: ").strip()

        if secim == "1":
            pet.feed()
        elif secim == "2":
            pet.play()
        elif secim == "3":
            pet.sleep()
        elif secim == "4":
            pet.heal()
        elif secim == "5":
            pet.talk()
        elif secim == "6":
            kelime = input("Öğretmek istediğin kelime: ")
            pet.teach_word(kelime)
        elif secim == "0":
            print(f"\nGörüşürüz! {pet.isim} sana el sallıyor 👋")
            break
        else:
            print("\nGeçersiz seçim!")

        input("\nDevam etmek için Enter'a bas...")


if __name__ == "__main__":
    main()