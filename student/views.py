from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from .forms import StudentCreationForm, StudentAuthenticationForm

def register(request):
    if request.method == 'POST':
        form = StudentCreationForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request,'index.html',{'user':user})
    else:
        form = StudentCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = StudentAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            visit_count = request.session.get('visit_count', 0)
            return render(request,'index.html',{'user':user,'visit_count': visit_count})
    else:
        form = StudentAuthenticationForm()
    return render(request, 'login.html', {'form': form})


   
def logoutme(request):
    logout(request)
    request.session.pop('logged_in', None)
    return redirect("/")