# Generated by Django 4.2.7 on 2023-11-27 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('implants', '0010_cyberware_bio_category_alter_cyberware_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=25, verbose_name='Название')),
                ('description', models.TextField(default='Some text', max_length=500, verbose_name='Описание')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Clothes_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=25, verbose_name='Название')),
                ('description', models.TextField(default='Some text', max_length=500, verbose_name='Описание')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Items_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=25, verbose_name='Название')),
                ('description', models.TextField(default='Some text', max_length=500, verbose_name='Описание')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Weapon_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=25, verbose_name='Название')),
                ('description', models.TextField(default='Some text', max_length=500, verbose_name='Описание')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='cyberware',
            name='category',
            field=models.CharField(max_length=25, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='menu_category',
            name='category',
            field=models.CharField(max_length=25, verbose_name='Название'),
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=25, verbose_name='Название')),
                ('description', models.TextField(default='Some text', max_length=500, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='illustration/transport/', verbose_name='Иллюстрация')),
                ('is_available', models.BooleanField(default=True, verbose_name='Доступно')),
                ('max_speed', models.PositiveIntegerField(default=0, verbose_name='Максимальная скорость')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('auto_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='implants.auto_category', verbose_name='Категория тела')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
