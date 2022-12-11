from django.urls import path
from . import views 
 
urlpatterns = [
    path("", views.index, name = "index"),
    path("<str:name>", views.greet, name = "greet"),# when a user types a content in url of hello app, call a function called 
    path("brian", views.brian, name = "brian"),          #greet  in view.py and give it the content typed in, in variable called  
    path("caes", views.caes, name = "caes")              # name
]