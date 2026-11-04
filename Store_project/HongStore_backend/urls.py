from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_b, name='home_b'),
    path('home_b/', views.home_b, name='home_b'),
    
    # Add Products
    path('add_laptop/', views.addLaptop, name='add_laptop'),
    path('add_keyboard/', views.addKeyboard, name='add_keyboard'),
    path('add_mouse/', views.addMouse, name='add_mouse'),

    # View Orders
    path('view_order/', views.viewOrder, name='view_order'),

    # View Products
    path('view_product/', views.viewProduct, name='view_product'),

    # Delete Product
    path('delete_laptop/<int:id>/', views.deleteLaptop, name='delete_laptop'),
    path('delete_keyboard/<int:id>/', views.deleteKeyboard, name='delete_keyboard'),
    path('delete_mouse/<int:id>/', views.deleteMouse, name='delete_mouse'),

    
    # Login & Logout
    path('login_page/', views.loginPage, name='login_page'),
    path('logout_page/', views.logoutPage, name='logout_page'),

    # Register Account
    path('register_page/', views.registerPage, name='register_page'),
 
    # View All Customer Orders
    path('view_order_customer/', views.viewOrderCustomer, name='view_order_customer'),
 

] 