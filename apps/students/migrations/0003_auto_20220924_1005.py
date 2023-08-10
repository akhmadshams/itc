# Generated by Django 3.2.5 on 2022-09-24 10:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20201124_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='current_status',
            field=models.CharField(choices=[('active', 'Aktiv'), ('inactive', 'Ketgan')], default='active', max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('male', 'Erkak'), ('female', 'Ayol')], default='male', max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='parent_mobile_number',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message="Iltimos e'tibotli bo'ling!", regex='^[0-9]{9,13}$')]),
        ),
    ]