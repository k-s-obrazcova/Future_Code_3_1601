# Generated by Django 5.0.6 on 2024-06-20 07:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_pos_parametr_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager', models.CharField(max_length=255, verbose_name='Фамилия управляющего')),
                ('location', models.CharField(max_length=255, verbose_name='Расположение')),
                ('capacity', models.PositiveIntegerField(verbose_name='Вместимость')),
            ],
            options={
                'verbose_name': 'Склад',
                'verbose_name_plural': 'Склады',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('rating', models.PositiveIntegerField(verbose_name='Рейтинг')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.product', verbose_name='Товар')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.warehouse', verbose_name='Склад')),
            ],
            options={
                'verbose_name': 'Инвентарь',
                'verbose_name_plural': 'Инвентари',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='warehouse',
            field=models.ManyToManyField(through='shop.Inventory', to='shop.warehouse', verbose_name='Склад'),
        ),
    ]
