from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    user = "Admin"
    return render(request, "orders/index.html", {
        "user": user,
    })