from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from todolist.models import Task
def todolist(request):
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
    return render(request,"todolist.html",context)

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




