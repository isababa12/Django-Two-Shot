from django.shortcuts import render
from receipts.models import Receipt

# Create your views here.


def show_receipt(request):
    receipt = Receipt.objects.all()
    context = {
        "receipt_object": receipt,
    }
    return render(request, "receipts/myreceipts.html", context)
