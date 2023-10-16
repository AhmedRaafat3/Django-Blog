from django.shortcuts import render
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
    else:
        form= postform()
    return render(request,'new.html',{form})