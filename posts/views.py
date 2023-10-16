from django.shortcuts import render, redirect
from .models import post
from.forms import postform

# Create your views here.

def post_list(requset):
    data=post.objects.all()
    return render(requset,'posts.html',{'posts':data})

def post_detail(requset,post_id):
    data=post.objects.get(id=post_id)
    return render(requset,'post_detail.html',{'post': data})

def add_post(request):

    if request.method=='POST':
        form=postform(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author=request.user
            myform.save()
            return redirect('/blog/')
    else:
        form= postform()
    return render(request,'new.html',{'form':form})



def edit_post(request,post_id):
    data=post.objects.get(id=post_id)
    if request.method=='POST':
        form=postform(request.POST,request.FILES,instance=data)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author=request.user
            myform.save()
            return redirect('/blog/')
    else:
        form= postform(instance=data)
    return render(request,'edit.html',{'form':form})



def post_delete(requset,post_id):
     data=post.objects.get(id=post_id)
     data.delete()
     return redirect('/blog/')