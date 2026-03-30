from django.urls import path,include
from todolist import views
urlpatterns = [
    path('todolist/',views.todolist, name="todolist"),
    path('',views.homepage, name="homepage"),
    path('contact/',views.contact, name="contact"),
    path('about/',views.about, name="about"),
]

