from django.shortcuts import render, redirect
from django.views.generic import  TemplateView,ListView
from beauty.models import contact, appointment, feedback, service, category, FAQs, career, Product
from beauty.forms import contactform, appointmentform, feedbackform, FAQsform, careerform
from django.contrib.auth.models import User
from django.views.generic import TemplateView,ListView
from cart.forms import CartAddProductForm
# Create your views here.
class Homepageview(TemplateView):
	template_name="home.html"
class Aboutpageview(TemplateView):
	template_name="about.html"
class Gallerypageview(TemplateView):
	template_name="gallery.html"
class Blogpageview(TemplateView):
	template_name="blog.html"
class Offerspageview(TemplateView):
	template_name="offers.html"
class Contactpageview(TemplateView):
	template_name="contact.html"
class Appointmentpageview(TemplateView):
	template_name="appointment.html"
class Feedbackpageview(TemplateView):
	template_name="feedback.html"
class Naturalpageview(TemplateView):
	template_name="natural.html"	
class Mehndipageview(TemplateView):
	template_name="mehndi.html"		
class Hairpageview(TemplateView):
	template_name="hair.html"				
class Pedicurepageview(TemplateView):
	template_name="pedicure.html"	
class Bridalpageview(TemplateView):
	template_name="bridal.html"
class Careerpageview(TemplateView):
	template_name="career.html"
class cartdetailview(TemplateView):
	template_name="cartdetail.html"
	

class Servicespageview(ListView):
	template_name="services.html"
	def get_queryset(self):
		return category.objects.all()
		
def servicedetail(request,id):
	serv = service.objects.filter(category_id=id)
  
	context = {
    'serv': serv,
        
    }
	return render(request, "servicedetail.html", context)	
	
class FAQspageview(ListView):
	template_name="FAQs.html"
	def get_queryset(self):
		return FAQs.objects.all()

	
def contact(request):
	if request.method=='POST':
		form=contactform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/contact')
			except:
				pass
	else: 
		form=contactform()
	return render(request,'contact.html',{'form':form})


def appointment(request):
	if request.method=='POST':
		form=appointmentform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/appointment')
			except:
				pass
	else: 
		form=appointmentform()
	return render(request,'appointment.html',{'form':form})
	
def feedback(request):
	if request.method=='POST':
		form=feedbackform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/feedback')
			except:
				pass
	else: 
		form=feedbackform()
	return render(request,'feedback.html',{'form':form})


def career(request):
	if request.method=='POST':
		form=careerform(request.POST, request.FILES)
		if form.is_valid():
			try:
				form.save()
				return redirect('/career')
			except:
				pass
	else: 
		form=careerform()
	return render(request,'career.html',{'form':form})



def product_list(request):
	products=Product.objects.all()
	cart_product_form=CartAddProductForm()
	context={
		'products':products,
		'cart_product_form':cart_product_form
	}
	return render(request,'Product.html',context)