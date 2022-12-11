from django.urls import path
from . import views

app_name = "tasks" #To handle name conflict. because we have another file called idex.html, in hello app. 

urlpatterns = [
    path("", views.index, name = "index"),
    path("add", views.add, name = "add")
]