from django.db import models

# Create your models here.
class Financial_Account(models.Model):
    account_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)
    account_ballance = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self) -> str:
        return self.account_name

class Expense_Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self) -> str:
        return self.category_name

class Financial_Transaction(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=100)
    transaction_value = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_description = models.CharField(max_length=300)
    financial_account = models.ForeignKey(Financial_Account, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.transaction_value

class Budget(models.Model):
    budget_name = models.CharField(max_length=200)
    budget_period = models.DurationField()
    buget_total = models.DecimalField(max_digits=10, decimal_places=2)
    budget_description = models.CharField(max_length=200)



