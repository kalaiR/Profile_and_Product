from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from firstproject.forms import *
# from django.contrib.auth.models import User

#Different ways of rendering HTML page
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
    
def index(request):
	print "request.user", request.user.id
	# if request.user.is_authenticated():
	# 	userprofile = User.objects.get(id=request.user.id)
	# 	print "userprofile123", userprofile	
	# else:
	# 	userprofile = None 

	return render_to_response('firstproject/index.html',context_instance=RequestContext(request)) 


def userprofileedit(request, pk):
	print "request.user", request.user.id
	if request.user.is_authenticated():
		userprofile = User.objects.get(id=request.user.id)
		print "userprofile123", userprofile	
	else:
		userprofile = None 

	return render_to_response('firstproject/edit.html', {'userprofile':userprofile}, context_instance=RequestContext(request)) 

def process(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request,user)

		return render(request,'firstproject/update.html',{'user_id':user.id}, context_instance=RequestContext(request))

	else:
		return HttpResponse('Invalid login')
def success(request):
	return render(request,'firstproject/success.html')
def register(request):
	if request.method == 'POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('user created')
		else:
			return render(request, 'firstproject/register.html', {'form':form,})
	args={}
	args.update(csrf(request))
	args['form']=UserCreationForm()
	return render_to_response('firstproject/register.html',args)

def logout(request):
	auth.logout(request)
	return render_to_response('firstproject/index.html')

def save(request ,pk):
	obj=User.objects.get(id=pk)
	obj.username=request.POST.get('username')
	obj.password=request.POST.get('password1')
	obj.conformpassword=request.POST.get('password2')
	obj.email=request.POST.get('email')
	obj.first_name=request.POST.get('first_name')
	obj.last_name=request.POST.get('last_name')
	obj.save()
	return render(request,'firstproject/update1.html')
# def savechanges(request):
# 	return render(request,'firstproject/update.html')


def reset(request,template_name='firstproject/password_change_form.html',password_change_form=PasswordChangeForm,extra_context=None):
    if request.method == "POST":
        form = password_change_form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Password successfully Changed.<a href="../success">Click here</a>')
    else:
        form = password_change_form(user=request.user)
    context = {
        'form': form,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context)
