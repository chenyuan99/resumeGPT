from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from hello.forms import NewUserForm
from hello.models import Greeting
from hello.models import Tutorial
from hello.forms import ContactForm
import markdown

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def homepage(request):
    return render(request = request,
                  template_name='main/home.html',
                  context = {"tutorials":Tutorial.objects.all})


def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, "db.html", {"greetings": greetings})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("index.html")

def login_request(request):
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "main/login.html",
                  context={"form":form})

def register(request):
    form = UserCreationForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

def resumematch(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "main/resumematch.html")

# add to your views
def contact(request):
    form_class = ContactForm
    return render(request, 'main/contact.html', {
        'form': form_class,
    })

# add to your views
def about(request):
    form_class = ContactForm
    return render(request, 'main/about.html')