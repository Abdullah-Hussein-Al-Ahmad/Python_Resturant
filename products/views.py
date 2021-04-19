from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Product

# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, r'index.html', {'products': products})
    return HttpResponse("Hello world")

def index2(request):
    products = Product.objects.all()
    return render(request, r'index2.html', {'products' : products})

def home(request):
    products = Product.objects.all()
    return render(request, r'arabicfood.html')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            print(form.get('Password'))
            print(Password)
        
        # print(form)
        return redirect('/login/')



# def new_topic(request):
#  """Add a new topic."""
#     if request.method != 'POST':
#     # No data submitted; create a blank form.
#         form = TopicForm()
#     else:
#     # POST data submitted; process data.
#         form = TopicForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('http://0.0.1:8000/:topics'))
# context = {'form': form}
# return render(request, 'http://0.0.1:8000//new_topic.html', context)