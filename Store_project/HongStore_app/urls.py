from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    
    # Computer
    path('computer/', views.computer, name='computer'),
    path('com_view/<int:id>/', view=views.com_view, name='com_view'),
        
    # Keyboard
    path('keyboard/', views.keyboard, name='keyboard'),
    path('key_view/<int:id>/', view=views.key_view, name='key_view'),

    # Mouse
    path('mouse/', views.mouse, name='mouse'),
    path('mouse_view/<int:id>/', view=views.mouse_view, name='mouse_view'),

    # All The Products
    path('shop/', views.shop, name='shop'),

    # Order Products
    path('order_laptop/<int:id>/', views.orderLaptop, name='order_laptop'),
    path('order_keyboard/<int:id>/', views.orderKeyboard, name='order_keyboard'),
    path('order_mouse/<int:id>/', views.orderMouse, name='order_mouse'),

    # Search
    path('search/', views.search, name='search'),

    # Register Page
    path('register/', views.registerPage, name='register'),

    # Sign In Page
    path('signin/', views.signinPage, name='signin'),

    # Sign Out Page
    path('signout/', views.signoutPage, name='signout'),

    # Account Page Customer
    path('customer/', views.customer, name='customer'),
]