# Generated by Django 4.1.1 on 2022-09-18 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название категории')),
                ('discription', models.TextField(verbose_name='Описание категории')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MarketCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Название карты')),
                ('avatar', models.ImageField(upload_to='card_avatars/', verbose_name='Аватар карты')),
                ('history', models.TextField(verbose_name='История карты')),
                ('data_created', models.DateTimeField(auto_now_add=True)),
                ('data_updated', models.DateTimeField(auto_now=True)),
                ('old_price', models.PositiveIntegerField(verbose_name='Старая цена карты')),
                ('new_price', models.PositiveIntegerField(verbose_name='Новая цена карты')),
                ('intelligence', models.PositiveSmallIntegerField(verbose_name='Интеллект карты')),
                ('agility', models.PositiveSmallIntegerField(verbose_name='Ловкость карты')),
                ('strength', models.PositiveSmallIntegerField(verbose_name='Сила карты')),
                ('is_published', models.BooleanField(default=False)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Market.category')),
            ],
            options={
                'verbose_name': 'Карта',
                'verbose_name_plural': 'Карты',
                'ordering': ['-data_created'],
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=0, verbose_name='')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Market.marketcard')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Market.reviews')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Replicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replica', models.TextField(verbose_name='Реплика')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Market.marketcard')),
            ],
            options={
                'verbose_name': 'Реплика',
                'verbose_name_plural': 'Реплики',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адресс')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Market.marketcard')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Market.ratingstar')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
    ]
