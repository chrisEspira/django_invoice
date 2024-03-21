from django.shortcuts import render
from django.views import View
from .models import *
from django.contrib import messages

# Create your views here.
class HomeView(View):
    """Main View"""
    
    template_name = 'index.html'
    
    invoices = Invoice.objects.select_related('customer','save_by').all()
    
    context = {
        'invoices': invoices
    }
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,self.context)
    
    
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
    
class AddCustomerView(View):
    """Add new Customer view"""
    
    template_name = 'addCustomer.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        
        data = {
          'name':request.POST.get('name'),
          'email':request.POST.get('email'),
          'phone':request.POST.get('phone'),
          'address':request.POST.get('address'),
          'sex':request.POST.get('sex'),
          'age':request.POST.get('age'),
          'city':request.POST.get('city'),
          'zip':request.POST.get('zip'),  
          'save_by':request.user
        }
        
        try:
            created = Customer.objects.create(**data)
            
            if created:
                messages.success(request, "Customer registered successfully.")
            else:
                messages.error(request, "Sorry, please try again the sent data is corrupt")
                
        except Exception as e:
            messages.error(request, f"Sorry our system is detecting the following issues {e}.")
            
        return render(request, self.template_name)
    