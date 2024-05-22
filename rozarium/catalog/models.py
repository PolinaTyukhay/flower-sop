from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200, help_text='Введите заголовок новости')
    text = models.TextField(help_text='Введите текст новости')
    pub_date = models.DateTimeField('date published', help_text='Выберите дату и время публикации новости')


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=200, help_text="Напишите категория")
    descriptionCategory = models.TextField(max_length=2000,
                                           help_text="Напишите описание категории")
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    #slug = models.SlugField(max_length=70, unique=True)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        
        return self.name
    
    def get_absolute_url(self):
        return reverse('catalog:product_list_by_category',
                        args=[self.slug])

class Plant(models.Model):
    '''
    plant_id = models.AutoField(primary_key=True, help_text='Уникальный идентификатор растения')
    name = models.CharField(max_length=100, help_text='Название растения')
    description = models.TextField(help_text='Описание растения')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text='Цена растения')
    availability = models.BooleanField(default=True, help_text='Наличие на складе')
    image = models.ImageField(upload_to='images/', help_text='Изображение растения')
    '''

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Растение'
        verbose_name_plural = 'Растения'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('catalog:product_detail',
                        args=[self.id, self.slug])


'''
class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True, help_text='Уникальный идентификатор распродажи')
    name = models.CharField(max_length=100, help_text='Название распродажи')
    date = models.DateField(help_text='Дата проведения распродажи')
    discount_percentage = models.IntegerField(help_text='Процент скидки')

    class Meta:
        verbose_name = 'Распродажа'
        verbose_name_plural = 'Распродажа'

    def __str__(self):
        return self.name

class PlantSale(models.Model):
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE, help_text='ID растения')
    sale_id = models.ForeignKey(Sale, on_delete=models.CASCADE, help_text='ID распродажи')

    def __str__(self):
        return f"{self.plant_id} - {self.sale_id}"


class Client(models.Model):
    client_id = models.AutoField(primary_key=True, help_text='Уникальный идентификатор клиента')
    first_name = models.CharField(max_length=50, help_text='Имя клиента')
    last_name = models.CharField(max_length=50, help_text='Фамилия клиента')
    email = models.EmailField(help_text='Адрес электронной почты клиента')
    phone = models.CharField(max_length=15, help_text='Номер телефона клиента')
    address_id = models.ForeignKey('DeliveryAddress', on_delete=models.SET_NULL, blank=True, null=True, help_text='ID адреса доставки')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f"Client ID: {self.id}, Name: {self.first_name} {self.last_name}, Email: {self.email}, Phone: {self.phone}, Delivery Address: {self.address_id}"



class DeliveryAddress(models.Model):
    address_id = models.AutoField(primary_key=True, help_text='Уникальный идентификатор адреса доставки')
    client_id = models.ForeignKey('Client', on_delete=models.CASCADE, help_text='ID клиента', related_name='delivery_addresses')
    index = models.CharField(max_length=10, help_text='Индекс адреса доставки')
    city = models.CharField(max_length=100, help_text='Город адреса доставки')
    street = models.CharField(max_length=100, help_text='Улица адреса доставки')
    house = models.CharField(max_length=10, help_text='Номер дома адреса доставки')
    apartment = models.CharField(max_length=10, help_text='Номер квартиры адреса доставки')

    class Meta:
        verbose_name = 'Адрес доставки'
        verbose_name_plural = 'Адреса доставки'

    def __str__(self):
        return f"Address ID: {self.address_id}, Index: {self.index}, Region: {self.region}, City: {self.city}, Street: {self.street}, House: {self.house}, Apartment: {self.apartment}"

class Review(models.Model):
    review_id = models.AutoField(primary_key=True, help_text='Уникальный идентификатор отзыва')
    plant = models.ForeignKey('Plant', on_delete=models.CASCADE, help_text='ID растения', related_name='reviews')
    client = models.ForeignKey('Client', on_delete=models.CASCADE, help_text='ID клиента', related_name='reviews')
    rating = models.IntegerField(help_text='Оценка (от 1 до 5)')
    text = models.TextField(help_text='Текст отзыва')
    publication_date = models.DateTimeField(auto_now_add=True, help_text='Дата публикации')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'Отзыв {self.review_id} - Растение: {self.plant}, Клиент: {self.client}, Оценка: {self.rating}'
    
class CartContent(models.Model):
    cart_id = models.AutoField(primary_key=True, help_text='ID корзины')
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='carts', help_text='ID растения')
    quantity = models.PositiveIntegerField(help_text='Количество растений в корзине')

    def __str__(self):
        return f'Корзина {self.cart_id} - Растение {self.plant.name} ({self.quantity} шт.)'

class Cart(models.Model):
    cart_id = models.ForeignKey(CartContent, on_delete=models.CASCADE, help_text='ID корзины')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, help_text='ID клиента')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Дата и время создания корзины')

    def __str__(self):
        return f'Корзина {self.cart_id} для клиента {self.client.client_id}'
    
class Order(models.Model):
    order_id = models.AutoField(primary_key=True, help_text='Уникальный ID заказа')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, help_text='ID корзины')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, help_text='ID клиента')
    order_datetime = models.DateTimeField(auto_now_add=True, help_text='Дата и время размещения заказа')

    ORDER_STATUS_CHOICES = [
        ('новый', 'Новый'),
        ('в_обработке', 'В обработке'),
        ('выполнен', 'Выполнен'),
    ]
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='новый', help_text='Статус заказа')

    order_total = models.DecimalField(max_digits=10, decimal_places=2, help_text='Общая сумма заказа')

    def __str__(self):
        return f'Заказ #{self.order_id} от {self.client}'

class OrderComposition(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, help_text='ID заказа (внешний ключ)')
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, help_text='ID растения (внешний ключ)')
    quantity = models.PositiveIntegerField(help_text='Количество')

    def __str__(self):
        return f'{self.quantity} шт. {self.plant.name} в заказе #{self.order.order_id}'
    
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, help_text='ID заказа (внешний ключ)')
    order_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text='Сумма заказа')
    shipping_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text='Сумма доставки')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text='Итого')

    def save(self, *args, **kwargs):
        self.total_amount = self.order_amount + self.shipping_amount
        super(Payment, self).save(*args, **kwargs)

    def __str__(self):
        return f'Оплата для заказа #{self.order_id}'
    
class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True, help_text='ID доставки (первичный ключ)')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, help_text='ID заказа (вторичный ключ)')
    delivery_address = models.ForeignKey(DeliveryAddress, on_delete=models.CASCADE, help_text='ID адреса доставки (необязательно для самовывоза)', blank=True, null=True)
    delivery_method_choices = [
        ('self_pickup', 'Самовывоз'),
        ('mail', 'Почта'),
    ]
    delivery_method = models.CharField(max_length=20, choices=delivery_method_choices, help_text='Способ доставки')

    def __str__(self):
        return f'Доставка для заказа #{self.order_id}'

    def save(self, *args, **kwargs):
        if self.delivery_method == 'self_pickup':
            self.delivery_address = None
        super(Delivery, self).save(*args, **kwargs)
'''
