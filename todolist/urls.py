from django.urls import path,include
from todolist import views
urlpatterns = [
    path('',views.homepage, name="homepage"),
    path('contact/',views.contact, name="contact"),
    path('about/',views.about, name="about"),
    path('todolist/',views.todolist, name="todolist"),
    path('todolist/delete_task/<int:task_id>/', views.delete_task, name="delete_task"),
    path('todolist/edit_task/<int:task_id>/', views.edit_task, name="edit_task"),
    path('todolist/complete/<int:task_id>/', views.complete_task, name="complete_task"),
    path('todolist/pending/<int:task_id>/', views.pending_task, name="pending_task"),
]

