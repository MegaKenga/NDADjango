# Generated by Django 4.2.4 on 2023-09-16 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unittocategory',
            name='group',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.group', verbose_name='Уникальный ID группы,                                                                                         принадлежащей направлению'),
        ),
    ]