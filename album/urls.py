from django.conf.urls import url
from album import views # a importar views.py

urlpatterns = [
    url(r'^$', views.first_view, name="first-view"),
    url(r'^category/$', views.category, name="category-list"),
    url(r'^category/(?P<category_id>[0-9])/detail/$', views.category_detail, name="category-detail"),
    url(r'^photo/$', views.PhotoListView.as_view(), name="photo-list"),
    url(r'^photo/(?P<pk>[0-9]+)/detail/$', views.PhotoDetailView.as_view(), name="photo-detail"),
    # Update
	url(r'^photo/(?P<pk>[0-9]+)/update/$', views.PhotoUpdate.as_view(),name='photo-update'),
	#Create
	url(r'^photo/create/$', views.PhotoCreate.as_view(),name='photo-create'),
	#Delete
	url(r'^photo/(?P<pk>[0-9]+)/delete/$', views.PhotoDelete.as_view(),name='photo-delete'),  

]