from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,View
from.models import CustUser
from django.urls import reverse_lazy
from.forms import RegForm,LogForm
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator


def signin_required(fun):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fun(request,*args,**kwargs)
        else:
            return redirect("log")
    return wrapper

class LogView(FormView):
    template_name="login.html"
    form_class=LogForm
    def post(self,request,*args,**kwargs):
        form_data=self.form_class(data=request.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("username")
            ps=form_data.cleaned_data.get("password")
            user=authenticate(request,username=un,password=ps)
            if user:
              if user.usertype=="Custumer":
                login(request,user)
                return redirect("viewprdt")
              elif user.usertype=="Seller":
                 login(request,user)
                 return redirect("storehome")
        
            else:
                return redirect("log")

class RegView(CreateView):
    model=CustUser
    template_name="register.html"
    form_class=RegForm
    success_url=reverse_lazy("log")



    
@method_decorator(signin_required,name="dispatch")
class LogoutView(View):
     def get(self,request,*args,**kwargs):
       logout(request)
       return redirect("log")