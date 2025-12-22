### APIView class
ref doc for [APIView class](https://www.django-rest-framework.org/api-guide/views/)

Step 1: In `api/views.py` replace function based view with APIView class for Product_info
```
from rest_framework.views import APIView

class ProductInfoAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductInfoSerializer({
            'products': products,
            'count': len(products),
            'max_price': products.aggregate(max_price=Max('price'))['max_price']
        })
        return Response(serializer.data)
```

Step 2: In `mysite/urls.py`, change the view callable to class for product info url
path('products/info/', views.ProductInfoAPIView.as_view()),

** runserver and verify the url works like before
