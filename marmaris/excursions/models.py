from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название страны")
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name = "Страны"
        verbose_name_plural = "Страны"

    def __str__(self):
        return self.name


class Town(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey('Country', on_delete=models.PROTECT, verbose_name='Страна')
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Города"
        verbose_name_plural = "Город"


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категория"


class Excursions(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    short_description = models.CharField(max_length=400, verbose_name='Краткое описание')
    description = models.TextField(blank=True, verbose_name='Описание')
    excursion_category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    slug = models.SlugField(max_length=50)
    active = models.BooleanField(default=True, verbose_name="Активно")
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    cost_dollar = models.IntegerField(verbose_name="Стоимость $")
    cost_rubles = models.IntegerField(verbose_name="Стоимость RUR")

    class Meta:
        verbose_name = "Экскурсии"
        verbose_name_plural = "Экскурсия"

    def __str__(self):
        return self.name


# Create your models here.
