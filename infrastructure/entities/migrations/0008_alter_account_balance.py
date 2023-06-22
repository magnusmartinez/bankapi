# Generated by Django 4.1.7 on 2023-06-21 23:47

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0007_transfer_commission_alter_transfer_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=11),
        ),
    ]
