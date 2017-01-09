from django.shortcuts import render_to_response, render
from .models import Post

#from django.http import HttpResponse
#from datetime import datetime

def hello_world(request):
    #return HttpResponse("Hello World!")
    return render_to_response( 'hello_world.html',{ 'current_time':'abcdef',})
#str(datetime.now())

def home(request):
	post_list = Post.objects.all()
	return render( request, 'home.html',{
			'post_list':post_list,
		})