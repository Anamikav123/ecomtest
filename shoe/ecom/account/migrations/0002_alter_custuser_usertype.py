# Generated by Django 4.1.5 on 2023-04-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custuser',
            name='usertype',
            field=models.CharField(choices=[('Seller', 'Seller'), ('Custumer', 'Custumer')], default='Custumer', max_length=100),
        ),
    ]