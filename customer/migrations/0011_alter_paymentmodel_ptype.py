# Generated by Django 4.2 on 2023-04-20 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_paymentmodel_pbook_reservationmodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmodel',
            name='ptype',
            field=models.CharField(max_length=100),
        ),
    ]
