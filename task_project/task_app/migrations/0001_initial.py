# Generated by Django 4.1.2 on 2022-10-22 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('address', models.CharField(max_length=40, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Барбершоп',
                'verbose_name_plural': 'Барбершопы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя клиента')),
                ('barber_name', models.CharField(max_length=20, verbose_name='Имя сотрудника')),
                ('record_date', models.CharField(choices=[(None, 'Выберите дату записи'), ('tomorrow_12', '23.10 в 12:00'), ('tomorrow_16', '23.10 в 16:00'), ('tomorrow_20', '23.10 в 20:00'), ('d_a_tomorrow_12', '24.10 в 12:00'), ('d_a_tomorrow_16', '24.10 в 16:00'), ('d_a_tomorrow_20', '24.10 в 20:00')], max_length=40)),
                ('bshop', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='task_app.bshop', verbose_name='Барбершоп')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
                'ordering': ['record_date'],
            },
        ),
    ]
