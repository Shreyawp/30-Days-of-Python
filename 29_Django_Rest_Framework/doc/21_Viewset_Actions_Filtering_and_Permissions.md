### Viewset Actions, Filtering and Permissions

Step 1: Add class OrderFilter in "api/filters.py"
```
class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = {
            'status': ['exact'],
            'created_at': ['lt', 'gt', 'exact']
        }
```

Step 2: Import OrderFilter to views.py and add following attributes to class OrderViewSet
```
filterset_class = OrderFilter
filter_backends = [DjangoFilterBackend]
```

Miscellaneous Step: To sort the imports in views.py
>> pip install isort
>> isort .\api\views.py
Fixing C:\Users\Admin\Desktop\python\30 days with vscode\29_Django_Rest_Framework\mysite\api\views.py


** Testing:
Filter orders with status;
![alt text](media/21_order_filter_status.PNG)

Filter orders with created_at;
![alt text](media/21_order_filter_created_at.PNG)

For exact date filter the response will be empty
Step 3: Add the following field to class OrderFilter
``` created_at = django_filters.DateFilter(field_name='created_at__date') ```
![alt text](media/21_order_filter_created_at_exact.PNG)

[Extra Actions for routing](https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing)

Step 4: Add action decorator followed by user_orders to "views/class OrderViewSet"
```
@action(detail=False, methods=['get'], url_path='user-orders')
    def user_orders(self, request):
        orders = self.get_queryset().filter(user=request.user)
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)
```

** Testing
for user-orders/ url, cannot access as anonymous user, since above orders has filter "request.user"
so login with admin user

This response contains orders that belongs to logged in user, here admin
![alt text](media/21_user_orders.PNG)

Step 5: Add `permission_classes=[IsAuthenticated]` to above action decorator
![alt text](media/21_user_orders_authentication.PNG)

Step 6: Remove permission_classes from @action, and replace permission_classes in OrderViewSet from AllowAny to IsAuthentic
The response of both url "orders/" and "user-orders/" is now Unauthorized.
![alt text](media/21_orders_authentication.PNG)


