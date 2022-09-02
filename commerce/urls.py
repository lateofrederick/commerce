from django.urls import path

from . import views

app_name = 'commerce'

urlpatterns = [
    path('accounts/register/', views.create_new_account, name='create_new_account'),
    path('accounts/login/', views.signin, name='login_into_account'),

    # buyer's url
    path('', views.buyer_homepage, name='buyer_homepage'),
    path('add_book_to_cart/<int:book_id>/', views.add_item_to_cart, name='add_book_to_cart'),
    path('checkout_items/', views.checkout_items, name='checkout_items'),
    path('order_items/', views.order_items, name='order_items'),
    path('search_books/', views.search_book, name='search_books'),
    path('completed_orders/', views.purchases, name='purchases'),

    # sellers's url
    path('seller/homepage/', views.seller_homepage, name='seller_homepage'),
    path('seller/upload_book/', views.upload_new_book, name='upload_new_book'),

]
