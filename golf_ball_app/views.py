from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'golf_balls/home.html')

def about(request):
    return HttpResponse("<h1>This is the About page</h1>")

def golf_ball_index(request):
    return render(request, 'golf_balls/index.html')