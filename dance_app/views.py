from django.shortcuts import render
from .models import DanceSchool

def landing(request):
    return render(request, 'dance_app/landing.html')

from django.shortcuts import render
from .models import Dancer

def register_dancer(request):
    success = False
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        age = request.POST.get("age")
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        dance_style = request.POST.get("dance_style")

        
        if first_name and last_name and age and phone and city and dance_style:
            Dancer.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                phone=phone,
                city=city,
                dance_style=dance_style
            )
            success = True

    return render(request, 'dance_app/register_dancer.html', {'success': success})

from django.shortcuts import render, redirect
from .models import DanceSchool

def register_school(request):
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        city = request.POST.get("city")
        contact_email = request.POST.get("contact_email")
        phone_number = request.POST.get("phone_number")
        dances_taught = request.POST.get("dances_taught")
        classes_per_week = request.POST.get("classes_per_week")

        DanceSchool.objects.create(
            name=name,
            address=address,
            city=city,
            contact_email=contact_email,
            phone_number=phone_number,
            dances_taught=dances_taught,
            classes_per_week=classes_per_week
        )

        return redirect('school_list')

    return render(request, 'dance_app/register_school.html')

def school_list(request):
    schools = DanceSchool.objects.all()
    return render(request, 'dance_app/school_list.html', {'schools': schools})

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                messages.success(request, f"Welcome back, {user.name}!")
                return redirect('landing')
            else:
                messages.error(request, "Invalid password.")
        except User.DoesNotExist:
            messages.error(request, "No user with that email found.")

    return render(request, 'dance_app/login.html')