from django.urls import path
from .views import show_receipt

urlpatterns = [
    path("", show_receipt, name="home"),
]
