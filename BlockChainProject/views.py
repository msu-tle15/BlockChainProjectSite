from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "BlockChainProject/index.html")


def transaction(request):
    return HttpResponse("Transaction page.")


def test(request):
    return HttpResponse("Test Page.")