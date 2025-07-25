from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import EnquiryForm
from django.shortcuts import render
from django.http import JsonResponse
from .models import Enquiry
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            # elif user is not None and user.is_employee:
            #     login(request, user)
            #     return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')


def customer(request):
    return render(request,'customer.html')


# def employee(request):
#     return render(request,'employee.html')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('dashboard')  # Redirect to the user dashboard or desired page
#         else:
#             return render(request, 'login.html', {'error': 'Invalid credentials.'})
#     else:
#         return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page

def save_enquiry(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST, request.FILES)
        if form.is_valid():
            enquiry = form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page
    else:
        form = EnquiryForm()
    return render(request, 'cutomer.html', {'form': form})
def success_view(request):
    return render(request, 'success.html')

from django.shortcuts import render
from .models import Enquiry
def admin_page(request):
    enquiries = Enquiry.objects.all()  # Retrieve all Enquiry objects from the database
    return render(request, 'admin.html', {'enquiries': enquiries})

def enquiry_data(request):
    enquiries = Enquiry.objects.all()
    data = []

    for enquiry in enquiries:
        data.append({
            'name': enquiry.name,
            'mobile': enquiry.mobile,
            'longitude': enquiry.longitude,
            'latitude': enquiry.latitude,
            'image_url': enquiry.image.url,
            'ecSocket': enquiry.ecSocket,
            'boxCondition': enquiry.boxCondition,
            'loopResistance': enquiry.loopResistance,
        })

    return JsonResponse(data, safe=False)


