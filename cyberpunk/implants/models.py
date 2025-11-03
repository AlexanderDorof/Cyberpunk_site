from django.db import models


class GeneralItem(models.Model):
    category = models.CharField(max_length=40, verbose_name="Название")
    description = models.TextField(
        max_length=500, verbose_name="Описание", default="Some text"
    )
    href = models.CharField(
        max_length=25, verbose_name="Гиперссылка", default="implants"
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.category


class Menu_category(GeneralItem):
    pass


class Card_category(GeneralItem):
    photo = models.ImageField(
        upload_to="illustration/Menu_preview/", verbose_name="Миниатюра", blank=True
    )

    class Meta:
        abstract = True


class Cyberware_category(Card_category):
    pass


class Auto_category(Card_category):
    pass


class Weapon_category(Card_category):
    pass


class Clothes_category(Card_category):
    pass


class Items_category(Card_category):
    pass


class Cyberware(GeneralItem):
    BODY = "BODY"
    REFLEX = "REFLEX"
    TECHNICK = "TECHNICK"
    COOL = "COOL"
    INTELLIGENCE = "INTELLIGENCE"
    CHARACTERISTIC = [
        (BODY, "Сила"),
        (REFLEX, "Реакция"),
        (TECHNICK, "Техника"),
        (COOL, "Холоднокровие"),
        (INTELLIGENCE, "Нетраннер"),
    ]
    Characteristic = models.CharField(
        max_length=12,
        choices=CHARACTERISTIC,
        default=BODY,
        verbose_name="Характеристика",
    )
    photo = models.ImageField(
        upload_to="illustration/cyberware/", verbose_name="Иллюстрация"
    )
    is_available = models.BooleanField(default=True, verbose_name="Доступно")
    cyberware_category = models.ForeignKey(
        "Cyberware_category",
        on_delete=models.CASCADE,
        verbose_name="Категория тела",
        blank=True,
        null=True,
    )
    capacity = models.PositiveIntegerField(default=0, verbose_name="Емкость")
    price = models.PositiveIntegerField(default=0, verbose_name="Цена")


class Vehicle(GeneralItem):
    photo = models.ImageField(
        upload_to="illustration/vehicle/", verbose_name="Иллюстрация"
    )
    is_available = models.BooleanField(default=True, verbose_name="Доступно")
    auto_category = models.ForeignKey(
        "Auto_category", on_delete=models.CASCADE, verbose_name="Тип авто"
    )
    max_speed = models.PositiveIntegerField(
        default=0, verbose_name="Максимальная скорость"
    )
    price = models.PositiveIntegerField(default=0, verbose_name="Цена")


class Weapon(GeneralItem):
    photo = models.ImageField(
        upload_to="illustration/weapon/", verbose_name="Иллюстрация"
    )
    is_available = models.BooleanField(default=True, verbose_name="Доступно")
    weapon_category = models.ForeignKey(
        "Weapon_category", on_delete=models.CASCADE, verbose_name="Категория оружия"
    )
    damage = models.PositiveIntegerField(default=0, verbose_name="Урон")
    load_capacity = models.PositiveIntegerField(
        default=0, verbose_name="Вместимость обоимы"
    )
    price = models.PositiveIntegerField(default=0, verbose_name="Цена")
