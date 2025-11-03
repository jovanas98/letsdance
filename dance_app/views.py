from django.shortcuts import render

def landing(request):
    return render(request, 'dance_app/landing.html')

def register_dancer(request):
    if request.method == "POST":
        pass
    return render(request, 'dance_app/register_dancer.html')

def register_school(request):
    if request.method == "POST":
        pass
    return render(request, 'dance_app/register_school.html')