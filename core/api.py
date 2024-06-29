from ninja import NinjaAPI
from core.schemas import FinancialTransactionSchema, FinancialAccountSchema, ExpenseCategorySchema
from core.models import *
from django.shortcuts import get_object_or_404
from ninja.errors import HttpError
from django.http import JsonResponse
from django.db import transaction
from typing import List

api = NinjaAPI()



@api.post('create/financial', response=FinancialTransactionSchema)
def create_financial(request, data: FinancialTransactionSchema)->FinancialTransactionSchema:
    with transaction.atomic():
        financial_account = Financial_Account.objects.create(**data.financial_account.dict())
        expense_category = Expense_Category.objects.create(**data.expense_category.dict())
        financial_transaction = Financial_Transaction.objects.create(
            date = data.date,
            transaction_type = data.transaction_type,
            transaction_value = data.transaction_value,
            transaction_description = data.transaction_description,
            financial_account = financial_account,
            expense_category = expense_category
        )

        return financial_transaction

@api.get("finances", response=List[FinancialTransactionSchema])
def get_all_finances(request):
    finances = Financial_Transaction.objects.all()
    return finances

@api.get("/{financial_id}", response=FinancialTransactionSchema)
def get_transaction_by_id(request, financial_id:int):
    try:
        transaction = Financial_Transaction.objects.get(id=financial_id)
        return transaction
    except Financial_Transaction.DoesNotExist:
        raise HttpError(404, "No found financial transaction")
    

@api.put("/{financial_id}", response=FinancialTransactionSchema)
def update_finances(request, financial_id:int, data:FinancialTransactionSchema):
    finance = get_object_or_404(Financial_Transaction, id=financial_id)
    for attr, value in data.dict().items():
        setattr(finance, attr, value)
        finance.save()
        return data


@api.delete('/delete/{finances_id}', response=FinancialTransactionSchema)
def delete_finances(request, finances_id: int):
    try:
        finance = Financial_Transaction.objects.get(id=finances_id)
        finance.delete()
        return JsonResponse({"Sucess": True})
    except Financial_Transaction.DoesNotExist:
        raise HttpError(404, 'not found financial transaction ')
