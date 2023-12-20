from django.shortcuts import render

def Home_Display(request):
    return render(request, "Home.html")