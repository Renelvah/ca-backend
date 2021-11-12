from django.db import models


# Модель шаблонов альбомов
class AlbumPattern(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"Заголовок")
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE, default=1, verbose_name=u"Тема")
    photo = models.ImageField('Photo', upload_to='albums', null=True)

    class Meta:
        db_table = 'albumPattern'
        verbose_name = u'Шаблон альбома'
        verbose_name_plural = u'Шаблоны альбомов'

    def __str__(self):
        return self.title


# Модель тем альмов
class Theme(models.Model):
    theme = models.CharField(max_length=100, default='Универсальный')
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'theme'
        verbose_name = u'Тема'
        verbose_name_plural = u'Темы'

    def __str__(self):
        return self.theme


# Модель размеров
class Size(models.Model):
    size = models.CharField(max_length=15)

    class Meta:
        db_table = 'size'
        verbose_name = u'Размер'
        verbose_name_plural = u'Размеры'

    def __str__(self):
        return self.size


# Модель типа
class AlbumType(models.Model):
    type = models.CharField(max_length=100)

    class Meta:
        db_table = 'albumType'
        verbose_name = u'Тип альбомов'
        verbose_name_plural = u'Типы альбомов'

    def __str__(self):
        return self.type


# Модель макета
class AlbumLayout(models.Model):
    type = models.ForeignKey('AlbumType', on_delete=models.CASCADE, default=1, verbose_name=u"Тип альбома")
    size = models.ForeignKey('Size', on_delete=models.CASCADE, default=1, verbose_name=u"Размер")
    minPages = models.IntegerField(default=10, verbose_name=u"Минимальное кол-во страниц")

    class Meta:
        db_table = 'albumLayout'
        verbose_name = u'Макет альбомов'
        verbose_name_plural = u'Макеты альбомов'

    def __str__(self):
        return f"{self.type} - {self.size}"


# Модель заказов
class Order(models.Model):
    STATUS = [
        ('in_progress', 'В процессе'),
        ('completed', 'Выполнен'),
        ('canceled', 'Отменен'),
    ]
    name = models.CharField(max_length=45, default='', verbose_name=u"Имя")
    email = models.CharField(max_length=500, default='', verbose_name=u"E-mail")
    albumPattern = models.ForeignKey('AlbumPattern', on_delete=models.PROTECT, default=1, verbose_name=u"Шаблон альбома")
    albumLayout = models.ForeignKey('AlbumLayout', on_delete=models.PROTECT, verbose_name=u"Макет альбома")
    date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name=u"Дата")
    pagesCount = models.IntegerField(default=10, verbose_name=u"Кол-во страниц")
    description = models.TextField(blank=True, null=True, verbose_name=u"Описание")
    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='in_progress',
        verbose_name=u"Статус"
    )

    class Meta:
        db_table = 'order'
        verbose_name = u'Заказ'
        verbose_name_plural = u'Заказы'

    def __str__(self):
        return f'{self.id}'


# Модель отзывов
class Review(models.Model):
    name = models.CharField(max_length=500, default='', verbose_name=u"Имя")
    email = models.CharField(max_length=100, null=True, verbose_name=u"Почта")
    rate = models.IntegerField(default=5, verbose_name=u"Оценка")
    date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name=u"Дата")
    text = models.TextField(blank=False, default='', verbose_name=u"Текст")

    class Meta:
        db_table = 'review'
        verbose_name = u'Отзыв'
        verbose_name_plural = u'Отзывы'

    def __str__(self):
        return f"{self.name} - {self.rate}"