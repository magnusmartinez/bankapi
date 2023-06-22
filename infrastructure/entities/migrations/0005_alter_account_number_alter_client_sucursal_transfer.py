# Generated by Django 4.1.7 on 2023-06-21 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0004_alter_client_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='number',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='CLIENT_SUCURAL', to='entities.sucursal'),
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('S01', 'done'), ('S02', 'pending'), ('S03', 'completed'), ('S04', 'canceled')], default='S02', max_length=3)),
                ('reference', models.CharField(blank=True, default='N/A', max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('destination_account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='TRANSFERS_DESTINATION_ACCOUNT', to='entities.account')),
                ('source_account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='TRANSFERS_SOURCE_ACCOUNT', to='entities.account')),
            ],
            options={
                'db_table': 'transfer',
            },
        ),
    ]