# Generated by Django 4.2.7 on 2024-01-02 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('implants', '0012_cyberware_category_vehicle_weapon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto_category',
            name='category',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='clothes_category',
            name='category',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='cyberware',
            name='category',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='cyberware_category',
            name='category',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='items_category',
            name='category',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='menu_category',
            name='category',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='category',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='category',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='weapon_category',
            name='category',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
    ]
