# Generated by Django 4.1.7 on 2023-06-22 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0009_alter_transfer_create_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='type',
            new_name='account_type',
        ),
        migrations.AlterField(
            model_name='transfer',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
