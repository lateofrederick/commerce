from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


from commerce.models.cart import Cart
from commerce.utils.custom_decorators import is_buyer


@login_required(login_url='/commerce/accounts/login')
@is_buyer()
def add_item_to_cart(request, book_id):
    """ allow an authenticated user to add a book to cart"""
    try:
        cart = Cart.objects.create(book_id=book_id, buyer=request.user)
        cart.save()
        messages.success(request, "Item added to cart successfully")
    except Exception:
        messages.error(request, "Failed to add item to cart")
    return redirect('commerce:buyer_homepage')
