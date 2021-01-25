from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
posts = [
    {
        'title': '', 
        'content': '',
        'author': '',
        'date':'',
    },
    ]




def home(request):
    # return HttpResponse("<h1>Blog Home</h1>")
    context={
        'posts':Post.objects.all()
    }
    return render(request, 'home.html', context)

def about(request):
    #return HttpResponse("<h1>Blog About</h1>")
    return render(request, 'about.html')
