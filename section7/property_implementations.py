class BouncyBall1:
    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if isinstance(new_price, float) and new_price > 0:
            self._price = new_price

    price = property(get_price, set_price)

    def get_size(self):
        return self._size

    def set_size(self, new_size):
        if isinstance(new_size, str) and new_size != "":
            self._size = new_size

    size = property(get_size, set_size)

    def get_brand(self):
        return self._brand

    def set_brand(self, new_brand):
        if isinstance(new_brand, str) and new_brand != "":
            self._brand = new_brand

    brand = property(get_brand, set_brand)


class BouncyBall2:
    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, float) and new_price > 0:
            self._price = new_price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if isinstance(new_size, str) and new_size != "":
            self._size = new_size

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, new_brand):
        if isinstance(new_brand, str) and new_brand != "":
            self._brand = new_brand
