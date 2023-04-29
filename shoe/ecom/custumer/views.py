from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,View
from seller.models import Product
from.models import CartItem
from.forms import Cartform
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.
class ViewProduct(TemplateView):
     template_name="viewcusprdt.html"
     def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['products']=Product.objects.all()
        return context
   

class AddCart(CreateView):
    template_name="addcart.html"
    form_class=Cartform
    model=CartItem
    success_url=reverse_lazy("cart")
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['pro']=Product.objects.get(id=self.kwargs.get("pid"))
        return context
    def form_valid(self, form):
        form.instance.user=self.request.user
        form.instance.product=Product.objects.get(id=self.kwargs.get("pid"))
        self.object=form.save()
        return super().form_valid(form)
    
class CartView(TemplateView):
    template_name="cart.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['cartitems']=CartItem.objects.filter(user=self.request.user)
        return context
class  RemoveCart(View):
    def get(self,request,*args,**kwargs):
        sid=kwargs.get("ssid")
        stu=CartItem.objects.get(id=sid)
        stu.delete()
        return redirect("cart")    

class LogoutView(View):
     def get(self,request,*args,**kwargs):
       logout(request)
       return redirect("log")