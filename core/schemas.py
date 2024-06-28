from ninja.orm import create_schema
from core.models import Financial_Account, Financial_Transaction, Expense_Category, Budget
from datetime import date, datetime
from ninja import Schema
from pydantic import BaseModel

class FinancialAccountSchema(Schema):
    account_name: str
    account_type: str
    account_ballance: float

class ExpenseCategorySchema(Schema):
    category_name: str
    category_description: str
    value: float

class FinancialTransactionSchema(Schema):
    date: datetime
    transaction_type: str
    transaction_value: float
    transaction_description: str
    financial_account: FinancialAccountSchema
    expense_category: ExpenseCategorySchema




