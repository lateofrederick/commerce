from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.shortcuts import render, redirect

from commerce.models.book import Book
from commerce.models.cart import Cart
from commerce.models.order import Order
from commerce.utils.custom_decorators import is_buyer
from commerce.utils.email_user import send_checkout_email


@login_required(login_url='/accounts/login')
@is_buyer()
def checkout_items(request):
    """ List all cart items to be checked out"""
    items = Cart.objects.filter(buyer=request.user)
    total = items.aggregate(total=Sum('book__price'))

    sum_total = 0
    if total['total'] is not None:
        sum_total = total['total']

    return render(request, 'commerce/homepage/buyer/checkout.html', {
        'items': items,
        'total': sum_total
    })


@login_required(login_url='/commerce/accounts/login')
@is_buyer()
def order_items(request):
    """ List all cart items to be checked out"""
    items = Cart.objects.filter(buyer=request.user)

    # loop over items to create order instances
    for item in items:
        order = Order.objects.create(book=item.book, buyer=item.buyer, status=True)
        order.save()

    # remove all cart items for user
    Cart.objects.filter(buyer=request.user).delete()

    # send user email message upon ordering of items
    try:
        send_checkout_email("Order Completed", "You have successfully fulfilled your order", request.user.email)
    except Exception:
        print('authentication failed')

    messages.success(request, 'Items successfully ordered. Please wait for shipping')

    return redirect('commerce:buyer_homepage')


