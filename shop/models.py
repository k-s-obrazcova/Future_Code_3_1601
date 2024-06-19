from django.db import models

# Create your models here.
MAX_LENGTH_CHAR = 255

class Supplier(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Название компании')
    agent_firstname = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Фамилия представителя')
    agent_name = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Имя представителя')
    agent_surname = models.CharField(max_length=MAX_LENGTH_CHAR, blank=True, null=True, verbose_name='Отчество представителя')
    agent_telephone = models.CharField(max_length=20, verbose_name='Телефон представителя')
    address = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Адрес')
    is_exists = models.BooleanField(default=True, verbose_name='Логическое удаление')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Название')
    description = models.CharField(max_length=MAX_LENGTH_CHAR, blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Tag(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Название')
    description = models.CharField(max_length=MAX_LENGTH_CHAR, blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Parametr(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

class Order(models.Model):
    SHOP = "SH"
    COURIER = "CR"
    PICKUPPOINT = "PP"
    TYPE_DELIVERY = [
        (SHOP, "Магазин"),
        (COURIER, "Курьер"),
        (PICKUPPOINT, "Пункт выдачи"),
    ]
    buyer_name = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Имя покупателя')
    buyer_firstname = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Фамилия покупателя')
    buyer_surname = models.CharField(max_length=MAX_LENGTH_CHAR, blank=True, null=True, verbose_name='Отчество покупателя')
    comment = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Комментарий')
    delivery_address = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Адрес доставки')
    delivery_type = models.CharField(max_length=2, choices=TYPE_DELIVERY, default=SHOP, verbose_name='Способ доставки')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    date_finish = models.DateTimeField(null=True, blank=True,verbose_name='Дата завершения заказа')

    product = models.ManyToManyField('Product', through='Pos_order', verbose_name='Товар')

    def __str__(self):
        return f'{self.pk} - ({self.buyer_firstname} {self.buyer_name}) {self.date_create}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Product(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Название')
    description = models.CharField(max_length=MAX_LENGTH_CHAR, null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    exists = models.BooleanField(default=True, verbose_name='В наличии?')

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    tag = models.ManyToManyField(Tag, blank=True, null=True, verbose_name='Тег')

    parametr = models.ManyToManyField(Parametr, through='Pos_parametr', verbose_name='Характеристики')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Pos_parametr(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Продукт')
    parametr = models.ForeignKey(Parametr, on_delete=models.PROTECT, verbose_name='Характеристика')
    value = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Значение')

    def __str__(self):
        return f'{self.product.name} - {self.value}'

    class Meta:
        verbose_name = 'Характеристика товара'
        verbose_name_plural = 'Характеристики товара'


class Pos_order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Продукт')
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')
    count = models.PositiveIntegerField(default=1, verbose_name='Количество продукта')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка на продукт')

    def __str__(self):
        return f'{self.pk} {self.product.name} {self.order.buyer_firstname} {self.order.buyer_name}'

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'

