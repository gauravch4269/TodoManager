from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from todolist.models import Task
from todolist.forms import TaskForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect


def todolist(request):
    if request.method == 'POST':
        form_data=TaskForm(request.POST or None)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Task added successfully.")
            return redirect("todolist")
        messages.success(request,"Something went wrong!")
    
    all_tasks = Task.objects.all()
    context = {
        "page":"todolist",
        "all_tasks":all_tasks,
    }
    #return HttpResponse("<h1> this is my todolist</h1>")
    '''data = {
        "name":"gaurav",
        "location":"Ghaziabad"
    } 
    return JsonResponse(data)'''
    #return render(request, "todolist.html",{})
    return render(request,"todolist.html",{"all_tasks":all_tasks})

def homepage(request):
    context = {
        "page":"homopage"
    }
    return render(request,"main.html",context)

def contact(request):
    context = {
        "page":"contact"
    }
    return render(request,"contact.html",context)

def about(request):
    context = {
        "page":"about"
    }
    return render(request,"about.html",context)

def delete_task(request,task_id):
    task_obj=Task.objects.get(id=task_id)
    task_obj.delete()
    messages.success(request,"Task deleted")
    return redirect("todolist")

def edit_task(request,task_id):
    task_obj=Task.objects.get(id=task_id)
    if request.method == "POST":
        form_data=TaskForm(request.POST or None, instance=task_obj)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Task Updated successfully.")
            return redirect("todolist")
        messages.success(request,"Something went wrong!")
    else:
        context={
            "task_obj":task_obj
        }
        return render(request,"edit.html", context)






