class Item:
    def __init__(self, count=3, max_count=16):
        self._count = count
        self._max_count = max_count

    def update_count(self, val):
        if val <= self._max_count:
            self._count = val
            return True
        else:
            return False

    # Свойство объекта. Не принимает параметров кроме self, вызывается без круглых скобок
    # Определяется с помощью декоратора property
    @property
    def count(self):
        return self._count

    # Ещё один способ изменить атрибут класса
    @count.setter
    def count(self, val):
        if val <= self._max_count:
            self._count = val
        else:
            pass

    @staticmethod
    def static():
        print('I am function')

    @classmethod
    def my_name(cls):
        return cls.__name__

    def __add__(self, num):
        """ Сложение с числом """
        return self.count + num

    def __sub__(self, num):
        """ Вычитание числа """
        return self.count - num

    def __mul__(self, num):
        """ Умножение на число """
        return self.count * num

    def __lt__(self, num):
        """ Сравнение меньше """
        return self.count < num

    def __le__(self, num):
        """ Сравнение меньше или равно """
        return self.count <= num

    def __gt__(self, num):
        """ Сравнение больше """
        return self.count > num

    def __ge__(self, num):
        """ Сравнение больше или равно """
        return self.count >= num

    def __iadd__(self, num):
        self.count += num
        return self

    def __imul__(self, num):
        self.count *= num
        return self

    def __isub__(self, num):
        if self.count >= num:
            self.count -= num
        return self

    def __len__(self):
        """ Получение длины объекта """
        return self.count


class Banana(Item):
    def __init__(self, count=1, max_count=32, color='green'):
        super().__init__(count, max_count)
        self._color = color

    @property
    def color(self):
        return self._color


class Fruit(Item):
    def __init__(self, ripe=True, **kwargs):
        super().__init__(**kwargs)
        self._ripe = ripe


class Food(Item):
    def __init__(self, saturation, **kwargs):
        super().__init__(**kwargs)
        self._saturation = saturation

    @property
    def eatable(self):
        return self._saturation > 0


class Apple(Fruit, Food):
    def __init__(self, ripe, count=1, max_count=32, color='green', saturation=10):
        super().__init__(saturation=saturation, ripe=ripe, count=count, max_count=max_count)
        self._color = color

    @property
    def color(self):
        return self._color

    @property
    def eatable(self):
        return super().eatable and self._ripe

    def __str__(self):
        return f'Apple ({self.count})'


class Pineapple(Fruit, Food):
    def __init__(self, ripe, count=1, max_count=32, saturation=13):
        super().__init__(saturation=saturation, ripe=ripe, count=count, max_count=max_count)


class Orange(Fruit, Food):
    def __init__(self, ripe, count=1, max_count=32, saturation=10):
        super().__init__(saturation=saturation, ripe=ripe, count=count, max_count=max_count)


class PeanutButter(Food):
    def __init__(self, count=1, max_count=32, saturation=30):
        super().__init__(saturation=saturation, count=count, max_count=max_count)

    def __str__(self):
        return f'Peanut butter ({self.count})'


class Meat(Food):
    def __init__(self, count=1, max_count=32, saturation=50):
        super().__init__(saturation=saturation, count=count, max_count=max_count)


class Inventory:
    def __init__(self, size: int):
        self.size: int = size
        self.body: [Item] = [None] * self.size

    def store(self, idx: int, item: Item):
        if not 0 <= idx < self.size:
            raise Exception("Index out of range")

        is_empty = self.body[idx] is None
        is_another_type = not isinstance(item, type(self.body[idx]))
        if is_empty or is_another_type:
            self.body[idx] = item
        else:
            self.body[idx] += item.count

    def remove(self, idx: int):
        if not 0 <= idx < self.size:
            raise Exception("Index out of range")

        if self.body[idx] is None:
            return

        if self.body[idx].count > 1:
            self.body[idx] -= 1
        else:
            self.body[idx] = None


def main():
    item = Item(count=3, max_count=4)
    item += 2
    print(item.count)

    inventory = Inventory(5)
    print(' '.join([str(e) for e in inventory.body]))
    inventory.store(0, Apple(ripe=True))
    print(' '.join([str(e) for e in inventory.body]))
    inventory.store(0, Apple(ripe=True))
    print(' '.join([str(e) for e in inventory.body]))
    inventory.store(0, PeanutButter())
    print(' '.join([str(e) for e in inventory.body]))

    inventory.store(0, Apple(ripe=True))
    inventory.store(0, Apple(ripe=True))
    print(' '.join([str(e) for e in inventory.body]))
    inventory.remove(0)
    print(' '.join([str(e) for e in inventory.body]))
    inventory.remove(0)
    print(' '.join([str(e) for e in inventory.body]))


main()
