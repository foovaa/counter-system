from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, "app/login.html", context=None)
def nationalCard(request):
    return render(request, "app/nationalCard.html", context=None)
def passport(request):
    return render(request, "app/passport.html", context=None)
def carLicense(request):
    return render(request, "app/carLicense.html", context=None)
def carViolation(request):
    return render(request, "app/carViolation.html", context=None)
def check(request):
    return render(request, "app/check.html", context=None)