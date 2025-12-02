#from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from api.serializers import ProductSerializer, OrderSerializer, OrderItemSerializer
from api.models import Product, Order, OrderItem
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serialzer = ProductSerializer(products, many=True)
    return Response(serialzer.data)

@api_view(['GET'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serialzer = ProductSerializer(product)
    return Response(serialzer.data)

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serialzer = OrderSerializer(orders, many=True)
    return Response(serialzer.data)