from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm,RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Case,When,IntegerField
# Create your views here.
#Here main Logic
def add_task(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)   # don't save yet
            task.user = request.user
            form.save()
            return redirect('detail')
    form=TaskForm()
    context={
        'form': form
    }
    return render(request,'list/add_task.html',context)

@login_required
def detail(request):
    tasks=Task.objects.filter(user=request.user).annotate(
        priority_order=Case(
            When(priority='high',then=1),
            When(priority='medium',then=2),
            When(priority='low',then=3),
            output_field=IntegerField()
        )
    ).order_by('complete','priority_order')
    return render(request,'list/detail.html',{'tasks':tasks})


def update_task(request,id):
    task=Task.objects.get(id=id)
    form=TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('detail')
    context={
        'form':form
    }
    return render(request,'list/update_task.html',context)

def delete_task(request,id):
    task=Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('detail')
    return render(request,'list/delete_task.html')

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail')
    form=RegisterForm()
    return render(request,'list/register.html',{'form':form})

def logout_view(request):
    logout(request)
    return render(request,'list/logout.html')


def complete_task(request,id):
    task=Task.objects.get(id=id,user=request.user)
    task.complete=True
    task.save()
    return redirect('detail')