# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from product.models import *
def product_detail(request):
	return render_to_response('product/product_detail.html',context_instance=RequestContext(request)) 


def save(request):
	print "save"
	product= Product_detail()
	product.product_name=request.POST.get('name')
	product.price=request.POST.get('price')
	product.product_model=request.POST.get('selected')
	print "product.product_model",product.product_model
	product.product_description=request.POST.get('description')
	# pro.product_image=request.POST.get('photo')
	# print "ready to save record"
	product.save()
	# return HttpResponseRedirect('/')
	return render_to_response('product/save.html',{})


def details(request):
	detail=Product_detail.objects.all()
	return render_to_response('product/details.html',{'detail':detail})

def particular_details(request, pk):
	# print "pk",pk
	productid= Product_detail.objects.get(id=pk)
	# print "productid",productid
	return render_to_response('product/particular_details.html',{'productid':productid})
