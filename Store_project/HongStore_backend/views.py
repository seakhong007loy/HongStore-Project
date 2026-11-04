from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from HongStore_app.models import OrderLaptop, OrderKeyboard, OrderMouse, Computer, Keyboard, Mouse, Customer
from HongStore_app.forms import ComputerForm, KeyboardForm, MouseForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import allowed_user
# Create your views here. 

@login_required(login_url='register_page')
def home_b(request):
    return  render(request=request, template_name='home_b.html')

# Add products
@login_required(login_url='register_page')
@allowed_user(allowed_roles=['admin'])
def addLaptop(request):
    com = ComputerForm()

    if request.method == "POST":
        com = ComputerForm(request.POST, request.FILES)

        if com.is_valid():
            com.save()
            return redirect('add_laptop')
    
    return render(request, template_name="add_laptop.html", context={'com': com})

@login_required(login_url='register_page')
@allowed_user(allowed_roles=['admin'])
def addKeyboard(request):
    key = KeyboardForm()

    if request.method == "POST":
        key = KeyboardForm(request.POST, request.FILES)

        if key.is_valid():
            key.save()
            return redirect('add_keyboard')
    
    return render(request, template_name="add_keyboard.html", context={'key': key})

@login_required(login_url='register_page')
@allowed_user(allowed_roles=['admin'])
def addMouse(request):
    mou = MouseForm()

    if request.method == "POST":
        mou = MouseForm(request.POST, request.FILES)

        if mou.is_valid():
            mou.save()
            return redirect('add_mouse')
    
    return render(request, template_name="add_mouse.html", context={'mou': mou})

# Views Orders
@login_required(login_url='register_page')
def viewOrder(request):
    view_laptop = OrderLaptop.objects.all()
    view_keyboard = OrderKeyboard.objects.all()
    view_mouse = OrderMouse.objects.all()

    return render (request, template_name='view_order.html', context={'view_laptop': view_laptop, 'view_keyboard': view_keyboard, 'view_mouse': view_mouse,})

# Views Products
@login_required(login_url='register_page')
def viewProduct(request):
    laptop = Computer.objects.all()
    total_laptop = laptop.count()
    keyboard = Keyboard.objects.all()
    mouse = Mouse.objects.all()

    return render(request, template_name="view_product.html", context={
        'laptop': laptop, 
        'keyboard': keyboard, 
        'mouse': mouse,
        'total_laptop': total_laptop,
    })

# View All Customer Order
@login_required(login_url='register_page')
@allowed_user(allowed_roles=['admin'])
def viewOrderCustomer(request):

    customers = Customer.objects.prefetch_related(
        'ordermouse_set',
        'orderkeyboard_set',
        'orderlaptop_set',
    ).all()

    return render(request, template_name='view_order_customer.html', context={'customers': customers})


# Delete Product
@login_required(login_url='register_page')
def deleteLaptop(request, id):
    delete_laptop = Computer.objects.get(id=id)

    if request.method == 'POST':
        delete_laptop.delete()

        return redirect('view_product')

    return render(request, template_name='delete_laptop.html', context={'delete_laptop':delete_laptop})


@login_required(login_url='register_page')
def deleteKeyboard(request, id):
    delete_keyboard = Keyboard.objects.get(id=id)

    if request.method == 'POST':
        delete_keyboard.delete()

        return redirect('view_product')

    return render(request, template_name='delete_keyboard.html', context={'delete_keyboard': delete_keyboard})


@login_required(login_url='register_page')
def deleteMouse(request, id):
    delete_mouse = Mouse.objects.get(id=id)

    if request.method == 'POST':
        delete_mouse.delete()

        return redirect('view_product')

    return render(request, template_name='delete_mouse.html', context={'delete_mouse': delete_mouse})

# Register Account
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home_b')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Account was created for {user}')
                return redirect('login_page')

        return render(request, template_name='register_page.html', context={'form': form})

# Login & Logout
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home_b')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_b')
            else:
                messages.info(request, f'Wrong Username or Password!!')

        return render (request, template_name='login_page.html')

def logoutPage(request):
    logout(request)
    return redirect('login_page')