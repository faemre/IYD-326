from inventory import Item, Inventory

def main():
    """Kullanıcı etkileşimi için ana fonksiyon. Bu fonksiyon, kullanıcıya envanter yönetim sistemi ile ilgili seçenekler sunar ve kullanıcının seçimine göre işlemler yapar."""
    inventory = Inventory()  # Inventory sınıfından bir envanter nesnesi oluşturur.
    
    while True:
        # Kullanıcıya seçenekleri sunar.
        print("\nEnvanter Yönetim Sistemi")
        print("1. Öğe Ekle")
        print("2. Öğe Güncelle")
        print("3. Öğe Kaldır")
        print("4. Tüm Öğeleri Listele")
        print("5. Çıkış")
        choice = input("Seçiminizi yapın: ")  # Kullanıcının seçimini alır.

        if choice == '1':
            # Kullanıcıdan yeni öğe bilgilerini alır.
            item_id = input("Öğe ID: ")
            name = input("Öğe Adı: ")
            quantity = int(input("Miktar: "))
            price = float(input("Fiyat: "))
            item = Item(item_id, name, quantity, price)  # Yeni bir öğe oluşturur.
            inventory.add_item(item)  # Öğeyi envantere ekler.
        elif choice == '2':
            # Kullanıcıdan güncellenecek öğe bilgilerini alır.
            item_id = input("Güncellenecek Öğe ID: ")
            quantity = input("Yeni Miktar (boş bırakabilirsiniz): ")
            price = input("Yeni Fiyat (boş bırakabilirsiniz): ")
            quantity = int(quantity) if quantity else None  # Miktar bilgisini alır, boş bırakılırsa None yapar.
            price = float(price) if price else None  # Fiyat bilgisini alır, boş bırakılırsa None yapar.
            inventory.update_item(item_id, quantity, price)  # Öğeyi günceller.
        elif choice == '3':
            # Kullanıcıdan kaldırılacak öğenin ID'sini alır.
            item_id = input("Kaldırılacak Öğe ID: ")
            inventory.remove_item(item_id)  # Öğeyi envanterden kaldırır.
        elif choice == '4':
            # Envanterdeki tüm öğeleri listeler.
            inventory.list_items()
        elif choice == '5':
            # Döngüden çıkar ve programı sonlandırır.
            break
        else:
            # Geçersiz seçim yapıldığında uyarı mesajı verir.
            print("Geçersiz seçenek. Tekrar deneyin.")

if __name__ == "__main__":
    # Eğer bu dosya doğrudan çalıştırılıyorsa, main fonksiyonunu çağırır.
    main()
