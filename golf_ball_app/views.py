from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Brand, Ball
from django.views.generic.edit import CreateView

# Create your views here.
def home(request):
    return render(request, 'golf_balls/home.html')

def about(request):
    return HttpResponse("<h1>This is the About page</h1>")

def golf_ball_index(request):
    brand = Brand.objects.all()
    user = request.user
    
    if user:
        balls = Ball.objects.filter(user)
        return render(request, 'golf_balls/favorites.html', 
        {'balls': balls,
        'brand': brand,
        }
    )
    
    else:
     balls = Ball.objects.all()
     
    return render(request, 'golf_balls/index.html', 
        {'balls': balls,
        'brand': brand,
        }
    ) 
    
def golf_ball_detail(request, ball_id): 
    ball = Ball.objects.get(id=ball_id)
    return render(request, 'golf_balls/detail.html', {'ball': ball })


def assoc_brand(request, ball_id, brand_id):
    Ball.objects.get(id=ball_id).brand.add(brand_id)
    return redirect('detail', ball_id=ball_id)

class BallCreate(CreateView):
    model = Ball
    fields = '__all__'
    success_url = '/list/'
   
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) 
    