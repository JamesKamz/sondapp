from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,  HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import QuestionForm
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

def home(request):
   questions = Question.objects.all()
   return render(request, 'home.html', {'questions': questions})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'add_question.html', {'form': form})

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_list.html', {'questions': questions})

def get_question(request, pk):
    question=Question.objects.get(pk=pk)
    options=question.choix.all()
    return render(request, 'detail.html', {'question': question, 'options': options})

def result(request, pk):
    question = Question.objects.get(pk=pk)
    options = question.choix.all()
    if request.method == 'POST':
        inputvalue = request.POST['choix']
        selection_option = options.get(pk=inputvalue)
        selection_option.nombre_de_votes += 5
        selection_option.save()
    return render(request, 'result.html', {'question': question, 'options': options})

@login_required
def delete_question(request, pk):
    question = Question.objects.get(pk=pk)
    return render(request, 'delete_question.html', {'question': question})

@login_required
def succefull(request, pk):
    question=Question.objects.get(pk=pk)
    if question.user == request.user and request.method == 'POST':
       question.delete()
    return render(request, 'succefull.html', {'question': question})


@login_required
def dashboard(request):
    user = request.user
    questions = Question.objects.filter(user=user)
    return render(request, 'dashboard.html', {'user': user, 'questions': questions})
