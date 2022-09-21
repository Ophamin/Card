from django.db import models
from django.contrib.auth.models import User


class MarketCard(models.Model):
    '''Модель карты'''
    title = models.CharField('Название карты', max_length=100, unique=True, db_index=True)
    avatar = models.ImageField('Аватар карты', upload_to='card_avatars/')
    history = models.TextField('История карты')
    data_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)
    old_price = models.PositiveIntegerField('Старая цена карты')
    new_price = models.PositiveIntegerField('Новая цена карты')
    intelligence = models.PositiveSmallIntegerField('Интеллект карты')
    agility = models.PositiveSmallIntegerField('Ловкость карты')
    strength = models.PositiveSmallIntegerField('Сила карты')
    
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-data_created']
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

class Category(models.Model):
    '''Модель категории'''
    name = models.CharField('Название категории', max_length=150)
    discription = models.TextField('Описание категории')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']



class Replicas(models.Model):
    replica = models.TextField('Реплика')
    card = models.ForeignKey('MarketCard', on_delete=models.CASCADE)

    def __str__(self):
        return self.replica

    class Meta:
        verbose_name = 'Реплика'
        verbose_name_plural = 'Реплики'



class RatingStar(models.Model):
    '''Звезда рейтинга'''
    value = models.PositiveSmallIntegerField('', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'

class Rating(models.Model):
    '''Рейтинг'''
    ip = models.CharField('IP адресс', max_length=15)
    star = models.ForeignKey('RatingStar', on_delete=models.CASCADE)
    card = models.ForeignKey('MarketCard', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.star} - {self.card}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

class Reviews(models.Model):
    '''Отзывы к карте'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    card = models.ForeignKey('MarketCard', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.card}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'    






