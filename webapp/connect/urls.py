
from django.urls import path

from connect import views
app_name='connect'
urlpatterns = [
    path('',views.Movies,name='Movies'),
    path('movies/<int:slno>/',views.description,name='description'),
    path('add/',views.add_elements,name="add_elements"),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:id>/',views.delete,name='delete'),
]