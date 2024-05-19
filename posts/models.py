from django.db import models

class Category(models.Model):
    name = models.CharField('Категория', max_length=200)
    slug = models.SlugField('Slug', max_length=100, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

class Supplier(models.Model):
    name = models.CharField('Название', max_length=200)
    adres = models.CharField('Адрес', max_length=200)
    city = models.CharField('Город', max_length=200)
    phone = models.CharField('Номер телефона', max_length=200)
    email = models.CharField('E-mail', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщиков'
        verbose_name_plural = 'Поставщики'


class Flower(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Категория')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Поставщик')
    name = models.CharField('Наименование', max_length=200)
    img = models.ImageField('Фото', upload_to='flowers')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    markup = models.DecimalField(max_digits=10, decimal_places=2)
    accounted_quantity = models.IntegerField(default=0)
    actual_quantity = models.IntegerField(default=0)
    archived = models.BooleanField('Архив', default=False)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цветы'
        verbose_name_plural = 'Цветы'




