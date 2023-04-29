from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,View
from .models import Product
from .forms import ProductForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator


def signin_required(fun):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fun(request,*args,**kwargs)
        else:
            return redirect("log")
    return wrapper


@method_decorator(signin_required,name="dispatch")
class StoreHome(TemplateView):
    template_name="storehome.html"


@method_decorator(signin_required,name="dispatch")
class AddProduct(View):
    def get(self,request,*args,**kwargs):
        f=ProductForm()
        return render (request,"addproduct.html",{"form":f})
    def post(self,request,*args,**kwargs):
        form_data=ProductForm(data=request.POST,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Product added successfully")
            return redirect("viewpdt")
        else:
            messages.error(request,"Product added failed") 
            return render(request,"addproduct.html",{"form":form_data})
        


@method_decorator(signin_required,name="dispatch")
class ViewProduct(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            
          res=Product.objects.all()
          return render(request,"viewproduct.html",{"data":res})
        else:
            return redirect("log")
        

@method_decorator(signin_required,name="dispatch")       
class ProductDeleteView(View):
    def get(self,request,*args,**kwargs):
        sid=kwargs.get("ssid")
        stu=Product.objects.get(id=sid)
        stu.delete()
        return redirect("viewpdt")

@method_decorator(signin_required,name="dispatch")      
class ProductEdit(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("sid")
        pdt=Product.objects.get(id=id)
        f=ProductForm(instance=pdt)
        return render(request,"editpdt.html",{"form":f})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("sid")
        pdt=Product.objects.get(id=id)
        form_data=ProductForm(data=request.POST,instance=pdt,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Product details updated successfully!!")
            return redirect("viewpdt")
        else:
            messages.error(request,"updation failed")
            return render(request,"editpdt.html",{"form":form_data})
