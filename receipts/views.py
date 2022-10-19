from django.shortcuts import render
from receipts.models import Receipt

# Create your views here.


def receipt_list(request):
    receipt = Receipt.objects.all()
    context = {
        "receipt_object": receipt,
    }
    return render(request, "receipts/receipt_list.html", context)
