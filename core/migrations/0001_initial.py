# Generated by Django 5.0.6 on 2024-06-26 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_name', models.CharField(max_length=200)),
                ('budget_period', models.DurationField()),
                ('buget_total', models.IntegerField(blank=True, null=True)),
                ('budget_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Expense_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('category_description', models.CharField(max_length=100)),
                ('value', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Financial_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=100)),
                ('account_type', models.CharField(max_length=100)),
                ('account_ballance', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Financial_Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('transaction_type', models.CharField(max_length=100)),
                ('transaction_value', models.IntegerField(blank=True, null=True)),
                ('transaction_description', models.CharField(max_length=300)),
                ('expense_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.expense_category')),
                ('financial_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.financial_account')),
            ],
        ),
    ]
