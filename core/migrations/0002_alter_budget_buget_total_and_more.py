# Generated by Django 5.0.6 on 2024-06-26 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='buget_total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expense_category',
            name='value',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='financial_account',
            name='account_ballance',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='financial_transaction',
            name='transaction_value',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
