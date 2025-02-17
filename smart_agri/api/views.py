from django.shortcuts import render,redirect
from .models import SensorData
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import random
from django.http import JsonResponse
# Create your views here.

def landing(request):
    return render(request,'landing.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Basic checks
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already in use.')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1
                )
                user.save()
                messages.success(request, 'You have successfully signed up!')
                return redirect('signin')  # Adjust to your sign-in route name
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')
    
    return render(request, 'signup.html')
    
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(username=username, password=password)
        try:
            if user is not None:
                login(request,user)
                messages.success(request,'Login Successfull!!')
                return redirect('dashboard')
            else:
                messages.error(request,'Invalid username or password credentials')
                return redirect('signin')     
        except Exception as e:
            messages.error(request, 'An error occurred during signin. Please try again.')        
    return render(request,'signin.html')

def dashboard(request):
    if request.user.is_authenticated:
        data = SensorData.objects.last()
    else:
        messages.error(request, 'please signin first!!!')
        return redirect(request,'signin')
    
    return render(request, 'dashboard.html', {'sensor_data': data})


# API to Toggle Devices
def toggle_device(request, device):
    if device not in ["water_pump", "led"]:
        return JsonResponse({"error": "Invalid device"}, status=400)

    status = random.choice([True, False])  # Simulate IoT state change
    return JsonResponse({"status": status})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('/')