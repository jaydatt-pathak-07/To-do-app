
from django.contrib import messages
from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
   return render(request,'index.html')



@login_required
def submit(request):
    obj = Todo()
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.user_id = request.user.id
    obj.priority = request.GET['priority']
   

    check_priority = Todo.objects.filter(user_id=request.user.id, priority=request.GET['priority'])
    if check_priority:
            messages.info(request, "Please select different priority")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    obj.save()
    mydictionary = {
        "alltodos" : Todo.objects.filter(user_id=request.user.id)
    }
    return render(request,'list.html',context=mydictionary)

@login_required
def delete(request,id):
    obj = Todo.objects.get(id=id)
    obj.user_id = request.user.id
    obj.delete()
    mydictionary = {
        "alltodos" : Todo.objects.filter(user_id=request.user.id)
    }
    return render(request,'list.html',context=mydictionary)

@login_required
def list(request):
    # mydictionary= list(**kwargs)
    print(f"user if  = {request.user.id}")
    mydictionary = {
        # "alltodos" : Todo.objects.all()
        "alltodos" : Todo.objects.filter(user_id=request.user.id)
    }

    # def get_context_data(self, **kwargs):
    #       context = get_context_data(**kwargs)
    #       context['title'] = context['title'].filter(user=self.request.user)
    #       context['count'] = context['title'].filter(complete=False).count()
    #       return context  

    return render(request,'list.html',context=mydictionary)

@login_required
def sortdata(request):
    mydictionary ={
        "alltodos" : Todo.objects.filter(user_id=request.user.id).order_by('priority')
    }
    print(mydictionary)
    return render(request,'list.html',context=mydictionary)

@login_required
def searchdata(request):
    q = request.GET['query']
    mydictionary = {
        "alltodos" : Todo.objects.filter(title__contains=q,user_id=request.user.id)
    }
    
    return render(request,'list.html',context=mydictionary)

@login_required
def edit(request,id):
    # obj = Todo()
    obj = Todo.objects.get(id=id)
    mydictionary = {
        "title" : obj.title ,
        "description" : obj.description,
        "priority" : obj.priority,
        "id" : obj.id
    }
    
    return render(request,'edit.html',context=mydictionary)

@login_required
def update(request,id):
    obj = Todo(id=id)
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    obj.user_id = request.user.id
    import datetime
    updated_at = datetime.datetime.now()
    obj.created_at = updated_at

    check_priority = Todo.objects.filter(user_id=request.user.id, priority=request.GET['priority'])
    if check_priority:
            messages.info(request, "Please select different priority")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # if len(check_priority) > 1 :
    #     messages.info(request, "Please select different priority.")
    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # elif len(check_priority) == 2:
    #      messages.info(request, "Please select different priority.")
    #      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # elif len(check_priority) < 1:
    #      pass

    obj.save()
    mydictionary = {
        "alltodos" : Todo.objects.filter(user_id=request.user.id)
    }
    return render(request,'list.html',context=mydictionary)


