### Serializers Topic Covered:
- Nested Serializers
- SerializersMethodField
- Serializer Relations

Step 1: Create order serializer and define Meta class containing 
model = Order
fields = (order_id, created_at, user, status)

Step 2: Create order_item serializer and define Meta class containing 
model = OrderItem
fields = (product, quantity)

Step 3: Create Views order_list from order model and serializer

Step 4:Add url path in "api/urls.py"

#### Nested Serializers
** Nesting the order items into order serializers 
[more about Nested RelationShips](https://www.django-rest-framework.org/api-guide/relations/#nested-relationships)
Step 5: define variable items calling OrderSerializers with params:
many = True {passing all fields of order_items}
read_only = True {since this fields are not editable}
And add the items to fields

Step 6: Add following parameter to class OrderItem in api/models.py
related_name=items 

** run server url: http://localhost:8000/orders/ and look are the nested items having products and quantity
![alt text](media/3_nested_serializer.PNG)

(optional) : Add order to Orderitem serializer fields 
fields = ('product', 'quantity', 'order')
![alt text](media/3_optional_order.PNG)

** if we dont use nested serializer, the items field will by default print primary key, is the part of serializer relations [PrimaryKeyField](https://www.django-rest-framework.org/api-guide/relations/#primarykeyrelatedfield)
(comment the items in order serializer)
![alt text](media/3_pk.PNG)

#### SerializerMethodField
[SerializerMethodField](https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield) - read-only field
-gets its value by calling methodname

Step 7: Add total_price of an order to orderserializer
```
total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        order_items = obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)
```
![alt text](media/3_methodserilizefield_tot_price.PNG)

Step 8: Add methodname and rename function get_total_price to total
```total_price = serializers.SerializerMethodField(method_name='total')

    def total(self, obj):
```

Step 9: nesting product in orderitem
```
product = ProductSerializer()
```
it will print product id, name, prce, and stock 
![alt text](media/3_nested_product.PNG)

Step 10: Flatten the data, by removing key "product" and keep only product name, price and quantity. So , class OrderItemSerializer looks like this now
```
class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        source='product.price'
        )

    class Meta:
        model = OrderItem
        fields = ('product_name', 'product_price', 'quantity')
```
![alt text](media/3_flatten_product_details.PNG)

Now, we have item_subtotal function defined in `models.py/class OrderItem`, add that too in above fields
```
fields = ('product_name', 'product_price', 'quantity', 'item_subtotal')
```
![alt text](media/3_item_subtotal.PNG)
** Although `models.py/class OrderItem/property item_subtotal` is not part of DB col, but can be used as fields in serializers

#### Serializer Relations
we have seen use of PrimaryKeyField earlier, also check similar ones
- [StringRelatedField](https://www.django-rest-framework.org/api-guide/relations/#stringrelatedfield)
- [HyperlinkedRelatedField](https://www.django-rest-framework.org/api-guide/relations/#hyperlinkedrelatedfield)
- [SlugRelatedField](https://www.django-rest-framework.org/api-guide/relations/#slugrelatedfield)

