from django.shortcuts import render
from .models import post
	
def home(request):
	all_post= post.objects.all()
	for Post in all_post:
		print(Post.description)
	return render(request, 'blog/index.html',{'all_post_list':all_post})

def post_list(request):
	post_list= post.objects.all()
	return render(request,'blog/post_list.html',{'post_li':post_list})

def single_post(request, post_id):
	Post=post.objects.get(pk=post_id)
	print(Post)
	return render(request,'blog/single_post.html',{'Post':Post})


# Create your views here.
