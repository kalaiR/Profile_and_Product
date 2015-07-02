from django.http import HttpResponse
from django.contrib import auth
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from firstproject.forms import *
    
def index(request):
    return render(request, 'firstproject/index.html')
def process(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request,user)
		return render(request,'firstproject/success.html')
	else:
		return HttpResponse(username)
def register(request):
	if request.method == 'POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('user created')

	args={}
	args.update(csrf(request))
	args['form']=UserCreationForm()
	return render_to_response('firstproject/register.html',args)