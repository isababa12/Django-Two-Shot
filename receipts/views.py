from django.shortcuts import render, redirect
from receipts.models import Receipt, Account, ExpenseCategory
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm, ExpenseCategoryForm

# Create your views here.


@login_required
def receipt_list(request):
    receipt = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_object": receipt,
    }
    return render(request, "receipts/receipt_list.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()
    context = {
        "form": form,
        }
    return render(request, "receipts/create.html", context)


@login_required
def category_list(request):
    expense = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "expense_object": expense,
    }
    return render(request, "receipts/category.html", context)


@login_required
def account_list(request):
    account = Account.objects.filter(owner=request.user)
    context = {
        "account_object": account,
    }
    return render(request, "receipts/accounts.html", context)


@login_required
def create_category(request):
    if request.method == "POST":
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(False)
            category.owner = request.user
            category.save()
            return redirect("category_list")
    else:
        form = ExpenseCategoryForm()
    context = {
        "form": form,
        }
    return render(request, "receipts/category_create.html", context)
