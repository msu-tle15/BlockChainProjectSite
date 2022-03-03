from django.urls import path
from . import views

urlpatterns = [
    # /BlockChainProject/
    path('', views.index, name='index'),

    # /BlockChainProject/transaction
    path('transaction', views.transaction, name='transaction'),

    # /BlockChainProject/test
    path('test', views.test, name='test')
]