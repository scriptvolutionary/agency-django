from django.db import models
from django.urls import reverse
from django.utils import timezone

IMMOVABLE_STATUS_CHOICES = (  # Статусы недвижимости
    ('черновик', 'Черновик'),
    ('опубликовано', 'Опубликовано'),
    ('арендовано', 'Арендованно'),
    ('куплено', 'Куплено')
)

IMMOVABLE_TYPES_CHOICES = (  # Типы недвижимости
    ('не определен', 'Не определен'),
    ('дом', 'Дом'),
    ('квартира', 'Квартира'),
    ('помещение', 'Помещение'),
    ('участок', 'Участок')
)

CONTRACT_STATUS_CHOICES = (  # Статусы договора
    ('черновик', 'Черновик'),
    ('действителен', 'Действителен'),
    ('истек', 'Истек')
)


class Realtor(models.Model):  # Модель риелтора
    name = models.CharField(  # Имя риелтора
        max_length=255,
        verbose_name='ФИО'
    )

    mail = models.CharField(  # Почта риелтора
        max_length=100,
        verbose_name='Почта'
    )
    tel = models.CharField(  # Телефон риелтора
        max_length=20,
        verbose_name='Номер телефона'
    )

    createdAt = models.DateTimeField(  # Дата создания
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updatedAt = models.DateTimeField(  # Дата обновления
        auto_now=True,
        verbose_name='Дата обновления'
    )

    class Meta:
        verbose_name = 'риелтора'
        verbose_name_plural = "Риелторы"

    def __str__(self):
        return self.name


class Holder(models.Model):  # Модель владельца недвижимости
    name = models.CharField(  # Имя владельца
        max_length=255,
        verbose_name='ФИО'
    )

    mail = models.CharField(  # Почта владельца
        max_length=100,
        verbose_name='Почта'
    )
    tel = models.CharField(  # Телефон владельца
        max_length=20,
        verbose_name='Номер телефона'
    )

    createdAt = models.DateTimeField(  # Дата создания
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updatedAt = models.DateTimeField(  # Дата обновления
        auto_now=True,
        verbose_name='Дата обновления'
    )

    class Meta:
        verbose_name = 'владельца'
        verbose_name_plural = "Владельцы"

    def __str__(self):
        return self.name


class Contract(models.Model):  # Модель договора
    identity = models.IntegerField(  # Номер договора
        verbose_name='Номер договора'
    )

    status = models.CharField( 	# Статус договора
        max_length=12,
        choices=CONTRACT_STATUS_CHOICES,
        default='черновик',
        verbose_name='Статус'
    )

    holderName = models.ForeignKey(  # Имя владельца
        Holder,
        on_delete=models.CASCADE,
        related_name='estate_contracts',
        verbose_name='Владелец'
    )
    realtorName = models.ForeignKey(  # Имя риелтора
        Realtor,
        on_delete=models.CASCADE,
        related_name='estate_contracts',
        verbose_name='Риелтор'
    )

    summ = models.IntegerField(  # Сумма договора
        verbose_name='Сумма'
    )

    slug = models.SlugField(  # Ссылка на договор
        max_length=255,
        unique=True,
        verbose_name='Метка'
    )

    executionAt = models.DateTimeField(  # Дата оформления
        default=timezone.now,
        verbose_name='Дата оформления'
    )
    createdAt = models.DateTimeField(  # Дата создания
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updatedAt = models.DateTimeField(  # Дата обновления
        auto_now=True,
        verbose_name='Дата обновления'
    )

    class Meta:
        verbose_name = 'договор'
        verbose_name_plural = "Договора"

    def __str__(self):
        return self.slug


class Immovable(models.Model):  # Модель недвижимости
    review = models.ImageField(  # Фото / обзор недвижимости
        upload_to='estate/static/immovables',
        height_field=None,
        width_field=None,
        max_length=100,
        verbose_name='Фотография'
    )
    label = models.CharField(  # Название недвижимости
        max_length=255,
        verbose_name='Название'
    )
    description = models.TextField(  # Описание недвижимости
        verbose_name='Описание'
    )
    address = models.CharField(  # Местоположение недвижимости
        max_length=255,
        verbose_name='Адрес'
    )

    type = models.CharField(  # Тип недвижимости
        max_length=12,
        choices=IMMOVABLE_TYPES_CHOICES,
        default='не определен',
        verbose_name='Тип недвижимости'
    )
    status = models.CharField( 	# Статус недвижимости
        max_length=12,
        choices=IMMOVABLE_STATUS_CHOICES,
        default='черновик',
        verbose_name='Статус'
    )

    holder = models.ForeignKey(  # Владелец недвижимости
        Holder,
        on_delete=models.CASCADE,
        related_name='estate_immovables',
        verbose_name='Владелец'
    )

    contract = models.BooleanField(  # Договор на недвижимость
        verbose_name='Договор'
    )
    contractIdentity = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        related_name='estate_immovables',
        null=True,
        verbose_name='Номер договора'
    )

    slug = models.SlugField(  # Ссылка на недвижимость
        max_length=255,
        unique=True,
        verbose_name='Метка'
    )

    publishAt = models.DateTimeField(  # Дата публикации
        default=timezone.now,
        verbose_name='Дата публикации'
    )
    createdAt = models.DateTimeField(  # Дата создания
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updatedAt = models.DateTimeField(  # Дата обновления
        auto_now=True,
        verbose_name='Дата обновления'
    )

    class Meta:
        verbose_name = 'недвижимость'
        verbose_name_plural = "Недвижимости"

    def get_absolute_url(self):
        return reverse('estate:immovable_detail', args=[self.slug])
