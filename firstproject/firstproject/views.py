from django.http import HttpResponse
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse
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
		return render(request,'firstproject/success.html',{'name' : request.user.username })
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
			return HttpResponse('Duplicate username')

	args={}
	args.update(csrf(request))
	args['form']=UserCreationForm()
	return render_to_response('firstproject/register.html',args)
def logout(request):
	auth.logout(request)
	return render_to_response('firstproject/index.html')

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
