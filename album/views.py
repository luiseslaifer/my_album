from django.shortcuts import render
from django.http import HttpResponse
from album.models import Category,Photo #a  importar category y Photo para las clases
from django.views.generic import ListView, DetailView # a
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
# Create your views here.

class PhotoUpdate(UpdateView):
	model = Photo
	fields = '__all__'


class PhotoCreate(CreateView):
	model=Photo
	fields = '__all__'


class PhotoDelete(DeleteView):
	model=Photo
	success_url=reverse_lazy('photo-list')

def first_view(request):
	return render(request,'base.html')

def category(request):
	category_list=Category.objects.all() #Guarda el contenido del modelo -> Category
	context={'object_list':category_list}
	return render(request,'album/category.html',context)

def category_detail(request,category_id):#parametro cate... recibe la llave prim
	category=Category.objects.get(id=category_id)
	context={'object':category}#para enviar al template se crea un diccionario
	return render(request,'album/category_detail.html',context)
#Herencia clase por defecto de django
class PhotoListView(ListView):
	model=Photo

class PhotoDetailView(DetailView):
	model=Photo

	
