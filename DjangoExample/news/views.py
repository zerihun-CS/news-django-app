from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Comment
# Create your views here.


def index(request):
   post = Post.objects.all()
   
   return render(request, 'index.html',{'post':post})


def post_detail(request,post_title:str):
   single_post = Post.objects.filter(title = post_title).first()
   
   # comment = Comment.objects.filter(post__title = post_title)
   comment = Comment.objects.filter(post__id = single_post.id, status = True)
   
   category = Category.objects.all()
   
   
   if request.method == "POST":
      
      name = request.POST.get('name')
      email = request.POST.get('email')
      website = request.POST.get('website')
      comment = request.POST.get('comment')
      
      obj = Comment()
      obj.name = name
      obj.email = email
      obj.website = website
      obj.comment = comment
      # obj.post = get_object_or_404(Post, title = post_title)
      obj.post = single_post
      obj.save()

      
   return render(request, 'post_detail.html',{'single_post':single_post,'category':category,'comment':comment})


def category_post(request, category_name:str):

   post = Post.objects.filter(category__name = category_name)   
      
   return render(request, 'index.html',{'post':post})
