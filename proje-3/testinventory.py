from inventory import Item, Inventory #item ve inventory sınıflarını içe aktarıyoruz

def test_inventory():
    """
    Envanter yönetim sistemini test eden fonksiyon.
    Bu fonksiyon, envanter yönetim sistemi üzerinde çeşitli testler yapar
    ve sonuçları kontrol eder.
    """
    inventory = Inventory()  # Inventory sınıfından bir envanter nesnesi oluşturur.

    # Öğe ekleme testleri
    item1 = Item("1", "Kalem", 100, 1.5)  # Yeni bir öğe oluşturur.
    item2 = Item("2", "Silgi", 50, 0.75)  # Yeni bir öğe oluşturur.
    inventory.add_item(item1)  # Öğeyi envantere ekler.
    inventory.add_item(item2)  # Öğeyi envantere ekler.
    
    assert len(inventory.items) == 2  # Envanterdeki öğe sayısının 2 olduğunu doğrular.
    
    # Öğe güncelleme testi
    inventory.update_item("1", quantity=120)  # Öğenin miktarını günceller.
    assert inventory.items["1"].quantity == 120  # Öğenin miktarının doğru güncellendiğini doğrular.
    
    # Öğe kaldırma testi
    inventory.remove_item("2")  # Öğeyi envanterden kaldırır.
    assert len(inventory.items) == 1  # Envanterdeki öğe sayısının 1 olduğunu doğrular.

    print("Tüm testler başarılı.")  # Tüm testler başarılı olduğunda mesajı yazdırır.

if __name__ == "__main__":
    # Eğer bu dosya doğrudan çalıştırılıyorsa, test_inventory fonksiyonunu çağırır.
    test_inventory()
