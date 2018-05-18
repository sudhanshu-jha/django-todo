from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Todo

# Create your views here.


def index(request):
    todos = Todo.objects.all()[:40]
   
    context={
        'todos': todos
    }
    return render(request,'todos/index.html',context) 


def add(request):
    if(request.method == 'POST'):
        Serial= request.POST['Serial']
        Title = request.POST['Title']
        Description = request.POST['Description']
        
        todo = Todo(Serial=Serial,Title=Title, Description=Description)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'todos/add.html')


def details(request, id):
    
    todo = Todo.objects.get(id=id)

    context = {
        'todo':todo
    }
    return render(request, 'todos/details.html', context)

def edit(request, pk):

    if (request.method=='GET'):
        todo = Todo.objects.filter(id=pk).first()
        # print( "the description is", todo.Description)
        context={
            'todos': todo
            }
        return render(request,'todos/edit.html',context) 
        
    elif (request.method=='POST'):
        Serial= request.POST['Serial']
        Title = request.POST['Title']
        Description = request.POST['Description']
        
        todo = Todo.objects.get(id=pk)
        todo.Serial= Serial
        todo.Title = Title
        todo.Description = Description
        todo.save()
        return redirect('/todos/')
        
def delete(request, pk):
    if (request.method=='GET'):
        todo = Todo.objects.filter(id=pk).first()
        
        context={
            'todos': todo
            }
        return render(request,'todos/delete.html',context) 
        
    elif (request.method=='POST'):
        Serial= request.POST['Serial']
        Title = request.POST['Title']
        Description = request.POST['Description']
        
        todo = Todo.objects.get(id=pk)
        todo.Serial= Serial
        todo.Title = Title
        todo.Description = Description        
        todo.delete()
        
        return redirect('/todos/')


    






