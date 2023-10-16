from django.views import generic
from .models import post


class postlist(generic.ListView):
    model=post


class postDetail(generic.DetailView):
    model= post



class Addpost(generic.CreateView):
    model=post 
    fields=['author','title','content','tags','image']
    success_url='/blog/'


class Editpost(generic.UpdateView):
    model=post 
    fields=['author','title','content','tags','image']
    success_url='/blog/'
    template_name='posts/edit.html'


class Deletepost(generic.DeleteView):
    model=post
    success_url='/blog/'


