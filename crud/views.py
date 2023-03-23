from django.shortcuts import render,HttpResponse,redirect
from .models  import *
from .forms import StudentForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# for generic 
from django.views.generic import ListView,FormView,DeleteView,CreateView,UpdateView,View


class StudentView(ListView):
    model=StudentRecord
    template_name="./home.html"

    def get_queryset(self):
        search=self.request.GET.get("search","")
        return StudentRecord.objects.filter(name__icontains=search)



class StudentFormView(CreateView):
    template_name="./insert.html"
    model=StudentRecord
    fields='__all__'
    success_url='/'

class DeleteStudentView(DeleteView):
    model=StudentRecord
    success_url='/'
    template_name='./delete.html'

class StudentEditView(UpdateView):
    model=StudentRecord
    fields='__all__'
    success_url='/'
    template_name='./insert.html'

class LoginView(FormView):
    template_name='login.html'
    form_class=AuthenticationForm
    success_url='/'

    def post(self, request):
        # return HttpResponse("login checking")
        username=request.POST.get('username')
        password=request.POST.get('password')

        user =authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request , user)
                return redirect('home')
            else:
                return HttpResponse("Inactive User")
        else:
            return HttpResponse("invalid username or password")

class LogoutView(View):
    def get(self , req):
        logout(req)
        return redirect ('home')
    

class SignUpView(CreateView):
    model=User
    fields=["first_name","last_name","email","username","password"]
    template_name='register.html'
    success_url="/login/"

    def form_valid(self, form):
        user=form.save(commit=False)
        user.password=make_password(user.password)
        user.save()
        return super().form_valid(form)