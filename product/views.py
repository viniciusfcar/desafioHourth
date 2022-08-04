from itertools import count
from django.shortcuts import render
from .models import Product

import requests
import json
from django.db.models.aggregates import Sum
from rest_framework import viewsets
from .serializers import ProductSerializer

class GetProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.values('product_url').annotate(total_vendas=Sum('vendas_no_dia'))
        return queryset

def list_products(request):
    response = requests.get('https://mc3nt37jj5.execute-api.sa-east-1.amazonaws.com/default/hourth_desafio')
    
    retorno = json.loads(response.content)
    for obj in retorno:
        Product.objects.get_or_create(product_url_image=obj['product_url__image'], product_url=obj['product_url'],
                                        product_url_created_at=obj['product_url__created_at'], vendas_no_dia=int(obj['vendas_no_dia']),
                                        consult_date=obj['consult_date'])

    produtos = Product.objects.values('product_url').annotate(total_vendas=Sum('vendas_no_dia'))
    
    context = { 
        'products': produtos
    }

    return render(request, 'list_products.html', {'context': context})