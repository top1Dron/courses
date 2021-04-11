# Generated by Django 3.1.3 on 2021-04-10 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Назва')),
                ('start_date', models.DateTimeField(verbose_name='Дата початку')),
                ('end_date', models.DateTimeField(verbose_name='Дата закінчення')),
                ('lections_quantity', models.IntegerField(verbose_name='Кількість лекцій')),
            ],
        ),
    ]