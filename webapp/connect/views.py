from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import films
from . forms import film_form
def Movies(request):
    movies=films.objects.all()
    return render(request,'movies.html',{'movies':movies})
def description (request,slno):
    movies=films.objects.get(id=slno)
    return render(request,'details.html',{'movies':movies})
def add_elements(request):
    if request.method=='POST':
        name = request.POST.get('name')
        year = request.POST.get('year')
        desc = request.POST.get('desc')
        image = request.FILES['image']
        movies=films(name=name,year=year,desc=desc,image=image)
        movies.save()
    return render(request,'admin.html')
def update(request,id):
    movies=films.objects.get(id=id)
    form=film_form(request.POST or None, request.FILES, instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return  render(request, 'edit.html', {'form': form, 'movies': movies})
def delete(request,id):
    if request.method=='POST':
        ids=films.objects.get(id=id)
        ids.delete()
        return redirect('/')
    return render(request,'delete.html')



