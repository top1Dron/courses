# Generated by Django 3.1.3 on 2021-04-10 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Курс', 'verbose_name_plural': 'Курси'},
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Назва'),
        ),
    ]