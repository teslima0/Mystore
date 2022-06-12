

# Create your views here.
from django.shortcuts import redirect, render
from django.http import JsonResponse, response, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse, response
from django.urls import reverse
from django.shortcuts import render

from django.core.mail import send_mail
import re
from django.conf import settings
# Create your views here.
from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy

class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('website:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)

class ContactSuccessView(TemplateView):
    template_name = 'contact/success.html'

def portfolio(request,*args,**kwargs):
    
    return render(request, 'portfolio_details.html', {})

def service(request,*args,**kwargs):
    
    return render(request, 'service.html', {})

def contact(request,*args,**kwargs):
    
    return render(request, 'contact.html', {})

def about(request,*args,**kwargs):
    
    return render(request, 'about.html', {})

def product(request,*args,**kwargs):
    
    return render(request, 'product.html', {})

def laptops(request,*args,**kwargs):
    
    return render(request, 'laptops.html', {})

def pcs(request,*args,**kwargs):
    
    return render(request, 'pcs.html', {})

def accessories(request,*args,**kwargs):
    
    return render(request, 'accessories.html', {})

def phone(request,*args,**kwargs):
    
    return render(request, 'phone.html', {})

def home(request,*args,**kwargs):
    
    return render(request, 'index.html', {})

def send_gmail(request):
    if request.method=="POST":
        
        #name= request.POST.get('name')
        email=request.POST.get('email') 
        message= request.POST.get('message')
        subject= request.POST.get('subject')
        
        #print(name, subject, message, email)
        #mss='message sent'
    
        send_mail( 
            #name,
            email,
            message,
            subject, 
           
            #settings.EMAIL_HOST_USER,
            #'agesinkole@gmail.com',
            #['agesinkole@gmail.com'], 
            recipient_list=['agesinkole@gmail.com'], 
            fail_silently=False, 
            #auth_user=None, 
            #auth_password=None, 
            #connection=None, 
            #html_message=None
        )
        return HttpResponseRedirect(reverse('website:homepage'))

def contactpage1(request,*args,**kwargs):
    
    if request.method== 'POST':
        name=request.POST['name']
        subject=request.POST['subject']
        message=request.POST['message']
        message_email=request.POST['email']
        send_mail(
        name, subject, message, message_email, 
          ['agesinkole@gmail.com'], 
        #fail_silently=False, 
        #auth_user=None, 
        #auth_password=None, 
        #connection=None, 
        #html_message=None
          )
        return render(request, 'contact.html',{'name':name})
    else:
        return render(request, 'contact.html',{'name':name})

def contactpage(request,*args,**kwargs):
    if request.method=="POST":
        
        #name= request.POST.get('name')
        email=request.POST.get('email') 
        message= request.POST.get('message')
        subject= request.POST.get('subject')
        
        #print(name, subject, message, email)
        #mss='message sent'
    
        send_mail( 
            #name,
            email,
            message,
            subject, 
           
            #settings.EMAIL_HOST_USER,
            #'agesinkole@gmail.com',
            #['agesinkole@gmail.com'], 
            recipient_list=['agesinkole@gmail.com'], 
            fail_silently=False, 
            #auth_user=None, 
            #auth_password=None, 
            #connection=None, 
            #html_message=None
        )
        return render(request, 'contact.html',{'name':email})
