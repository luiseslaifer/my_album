from django.shortcuts import render
from django.http import HttpResponse
from album.models import Category,Photo #a  importar category y Photo para las clases
from django.views.generic import ListView, DetailView # a
# Create your views here.
def first_view(request):
	return HttpResponse("<h1>Esta es mi primer vista</h1>")

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
