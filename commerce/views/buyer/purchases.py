from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from commerce.models.order import Order
from commerce.utils.custom_decorators import is_buyer


@login_required(login_url='/commerce/accounts/login')
@is_buyer()
def purchases(request):
    """ List all purchases completed by user"""

    orders = Order.objects.filter(buyer=request.user)
    return render(request, 'commerce/homepage/buyer/purchases.html', {'orders': orders})
