from django.db.models import Sum, Count

from commerce.models.cart import Cart
from commerce.models.order import Order


def get_cart_items(request):
    user = request.user
    try:
        cart = Cart.objects.filter(buyer=user)
        return {
            'cart': cart
        }
    except Exception as e:
        return {
            'cart': []
        }


def get_total_sales_and_customers(request):
    """ retrieves the total sales of books for a seller """
    try:
        total = Order.objects.filter(status=True).aggregate(total=Sum('book__price'))
        customers = Order.objects.filter(status=True).values('buyer_id').distinct().count()

        total_orders = 0
        if total['total'] is not None:
            total_orders = total['total']

        return {
            'sales_total': total_orders,
            'customers': customers
        }
    except Exception as e:
        return {
            'sales_total': 0,
            'customers': 0
        }
