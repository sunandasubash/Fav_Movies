from django.contrib import messages
from django.shortcuts import render, redirect

from app1.forms import movieform
from app1.models import Movie


# Create your views here.
def home(request):
    movie = Movie.objects.all()
    context ={
        'movie_list' :movie
    }
    return render(request,'home.html',context)
def details(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':movie})

def add(request):
    if request.method == "POST":
        name = request.POST.get('name',)
        des = request.POST.get('des', )
        year = request.POST.get('year',)
        img = request.FILES['img']
        movie = Movie(name=name,des=des,year=year,img=img)
        movie.save()
    return render(request,'add.html')

def update(request,id):
    if request.method == 'POST':
        mov=Movie.objects.get(id=id)
        form=movieform(request.POST or None, request.FILES,instance=mov)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = movieform()
    return render(request,'update.html',{'form':form})


def delete(request,id):
    if request.method == 'POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
