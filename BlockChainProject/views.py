from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "BlockChainProject/index.html")


def transaction(request):
    return render(request, "BlockChainProject/transaction.html")


def test(request):
    return render(request, "BlockChainProject/test.html")