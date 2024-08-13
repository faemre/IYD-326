class Item:
    def __init__(self, item_id, name, quantity, price):
        """
        Item sınıfı, her bir öğenin kimliğini, ismini, miktarını ve fiyatını tutar.
        :param item_id: Öğenin kimliği.
        :param name: Öğenin ismi.
        :param quantity: Öğenin miktarı.
        :param price: Öğenin fiyatı.
        """
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, quantity):
        """
        Öğenin miktarını günceller.
        :param quantity: Yeni miktar.
        """
        self.quantity = quantity

    def update_price(self, price):
        """
        Öğenin fiyatını günceller.
        :param price: Yeni fiyat.
        """
        self.price = price

    def __str__(self):
        """
        Öğenin detaylarını döner.
        :return: Öğenin kimliği, ismi, miktarı ve fiyatı.
        """
        return f"ID: {self.item_id}, Name: {self.name}, Quantity: {self.quantity}, Price: {self.price}"


class Inventory:
    def __init__(self):
        #'self.items' adında bir sözlük oluşturur.Bu sözlük , envanterdeki öğeleri 'item_id' anahtarı ile saklar.
        """
        Inventory sınıfı, envanteri yönetir ve öğe ekleme, güncelleme, kaldırma işlemlerini yapar.
        items sözlüğü, öğeleri item_id anahtarı ile saklar.
        """
        self.items = {}

    def add_item(self, item):
        """
        Envantere yeni bir öğe ekler.
        :param item: Eklenmek istenen öğe.
        """
        if item.item_id in self.items:
            # Öğenin zaten mevcut olup olmadığını kontrol eder.
            print("Item already exists.")
        else:
            # Öğeyi envantere ekler.
            self.items[item.item_id] = item

    def update_item(self, item_id, quantity=None, price=None):
        """
        Envanterdeki bir öğeyi günceller.
        :param item_id: Güncellenecek öğenin kimliği.
        :param quantity: Yeni miktar (opsiyonel).
        :param price: Yeni fiyat (opsiyonel).
        """
        if item_id in self.items:
            # Eğer öğe envanterde varsa, miktar veya fiyat bilgilerini günceller.
            if quantity is not None:
                self.items[item_id].update_quantity(quantity)
            if price is not None:
                self.items[item_id].update_price(price)
        else:
            # Eğer öğe envanterde yoksa, hata mesajı verir.
            print("Item not found.")

    def remove_item(self, item_id):
        """
        Envanterden bir öğeyi kaldırır.
        :param item_id: Kaldırılacak öğenin kimliği.
        """
        if item_id in self.items:
            # Eğer öğe envanterde varsa, öğeyi siler.
            del self.items[item_id]
        else:
            # Eğer öğe envanterde yoksa, hata mesajı verir.
            print("Item not found.")

    def list_items(self):
        """
        Envanterdeki tüm öğeleri listeler.
        """
        if not self.items:
            # Eğer envanterde hiç öğe yoksa, envanterin boş olduğunu belirtir.
            print("Envanter boş.")
        for item in self.items.values():
            # Envanterdeki her bir öğeyi yazdırır.
            print(item)