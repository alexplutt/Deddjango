# Generated by Django 4.0.5 on 2022-10-31 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('orders', '0003_salesorder_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.acc'),
        ),
    ]
