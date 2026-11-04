from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .models import Computer, Keyboard, Mouse, OrderLaptop, OrderKeyboard, OrderMouse, Customer
from .forms import ComputerForm, KeyboardForm, MouseForm, OrderLaptopForm, OrderKeyboardForm, OrderMouseForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.
@login_required(login_url='register')
def home(request):
    return render(request=request, template_name='home.html')

# Computer
@login_required(login_url='register')
def computer(request):
    c=Computer.objects.all()
    return render(request=request, template_name='computer.html', context={'computer':c})

@login_required(login_url='register')
def com_view(request, id):
    cv=Computer.objects.get(id=id)
    return render (request=request, template_name='com_view.html', context={'cv':cv})

# Keyboard
@login_required(login_url='register')
def keyboard(request):
    k=Keyboard.objects.all()
    return  render(request=request, template_name='keyboard.html', context={'keyboard':k})

@login_required(login_url='register')
def key_view(request, id):
    kv=Keyboard.objects.get(id=id)
    return render (request=request, template_name='key_view.html', context={'kv':kv})

# Mouse
@login_required(login_url='register')
def mouse(request):
    m=Mouse.objects.all()
    return render (request=request, template_name='mouse.html', context={'mouse':m})

@login_required(login_url='register')
def mouse_view(request, id):
    mv=Mouse.objects.get(id=id)
    return render (request=request, template_name='mouse_view.html', context={'mv':mv})


# All The Products
@login_required(login_url='register')
def shop(request):
    c=Computer.objects.all()
    k=Keyboard.objects.all()
    m=Mouse.objects.all()
    return render(request, template_name="shop.html", context={'computer':c, 'keyboard': k, 'mouse':m})

# Order Products
@login_required(login_url='register')
def orderLaptop(request, id):
    laptop = Computer.objects.get(id=id)

    # create customer or use customer if it has
    customer, created = Customer.objects.get_or_create(
        user=request.user,
        defaults={'name': request.user.username}
    )

    order_laptop = OrderLaptop(laptop=laptop, customer=customer)

    order_laptop_form = OrderLaptopForm(instance=order_laptop)

    if request.method == 'POST':
        order_laptop_form = OrderLaptopForm(request.POST, instance=order_laptop)

        if order_laptop_form.is_valid():
            order_laptop_form.save()
            return redirect('computer')
    
    else:
        order_laptop_form = OrderLaptopForm(instance=order_laptop)


    return render(request, template_name='order_laptop.html', context={'order_laptop_form': order_laptop_form, 'laptop': laptop})

@login_required(login_url='register')
def orderKeyboard(request, id):
    keyboard = Keyboard.objects.get(id=id) 

    # create customer or use customer if it has
    customer, created = Customer.objects.get_or_create(
        user=request.user,
        defaults={'name': request.user.username}
    )

    order_keyboard = OrderKeyboard(keyboard=keyboard, customer=customer)

    order_keyboard_form = OrderKeyboardForm(instance=order_keyboard)

    if request.method == 'POST':
        order_keyboard_form = OrderKeyboardForm(request.POST, instance=order_keyboard)

        if order_keyboard_form.is_valid():
            order_keyboard_form.save()

            return redirect('keyboard')

    else:
        order_keyboard_form = OrderKeyboardForm(instance=order_keyboard)


    return render(request, template_name='order_keyboard.html', context={'order_keyboard_form': order_keyboard_form, 'keyboard': keyboard})


@login_required(login_url='register')
def orderMouse(request, id):
    mouse = Mouse.objects.get(id=id)

    # create customer or use customer if it has
    customer, created = Customer.objects.get_or_create(
        user=request.user,
        defaults={'name': request.user.username}
        )

    order_mouse = OrderMouse(mouse=mouse, customer=customer)

    order_mouse_form = OrderMouseForm(instance=order_mouse)

    if request.method == 'POST':
        order_mouse_form = OrderMouseForm(request.POST, instance=order_mouse)

        if order_mouse_form.is_valid():
            order_mouse_form.save()

            return redirect('mouse')
    else:

        order_mouse_form = OrderMouseForm(instance=order_mouse)


    return render(request, template_name='order_mouse.html', context={'order_mouse_form': order_mouse_form, 'mouse': mouse})

# Search MEthod
def search(request):

    query = request.GET.get('q', '').strip()

    computer = Computer.objects.none()
    keyboard = Keyboard.objects.none()
    mice = Mouse.objects.none()

    if query:
        computers = Computer.objects.filter( Q(name__icontains=query))
        keyboards = Keyboard.objects.filter( Q(name__icontains=query))
        mice = Mouse.objects.filter( Q(name__icontains=query))

    return render (request, 'search.html', context={ 'query': query, 'computers': computers, 'keyboards': keyboards, 'mice': mice, })

# Register View
def registerPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                user = form.save()
                
                # Add user to Customer Group
                group = Group.objects.get(name='customer')
                user.groups.add(group)

                username = form.cleaned_data.get('username')
                messages.success(request, f'Account was created for {username}')

                # Auto create Customer Models
                Customer.objects.create(user=user, name=username)

                return redirect('signin')

        return render(request, template_name='register.html', context={'form': form})

# Sign In View
def signinPage(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, f'Wrong Username Or Password!!!')

        return render(request, template_name='signin.html')

# Sign Out View
def signoutPage(request):
    logout(request)
    return redirect('signin')


# Customer Page
def customer(request):
    order_mouse = request.user.customer.ordermouse_set.all()
    order_keyboard = request.user.customer.orderkeyboard_set.all()
    order_laptop = request.user.customer.orderlaptop_set.all()

    total_order = order_mouse.count() + order_keyboard.count() + order_laptop.count()

    return render(request, template_name='customer.html', context={
                                                                    'order_mouse': order_mouse,
                                                                    'order_keyboard': order_keyboard,
                                                                    'order_laptop': order_laptop,
                                                                    'total_order': total_order
                                                                    })