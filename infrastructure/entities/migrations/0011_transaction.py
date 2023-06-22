# Generated by Django 4.1.7 on 2023-06-22 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0010_rename_type_account_account_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(choices=[('C001', 'bank teller'), ('C002', 'atm')], default='C001', max_length=4)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('status', models.CharField(choices=[('S01', 'pending'), ('S02', 'completed'), ('S03', 'canceled')], default='S01', max_length=3)),
                ('is_active', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(blank=True, default='N/A', max_length=255)),
                ('transaction_type', models.CharField(choices=[('T001', 'deposit'), ('T002', 'withdrawal')], max_length=4)),
                ('commission', models.FloatField(editable=False)),
                ('reference_number', models.CharField(max_length=16, unique=True)),
                ('additional_notes', models.TextField(blank=True, default='N/A')),
                ('destination_account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='TRANSACTION_DESTINATION_ACCOUNT', to='entities.account')),
            ],
            options={
                'db_table': 'transaction',
            },
        ),
    ]