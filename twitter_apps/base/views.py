from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.
def startpage(request):
    return render(request, 'base/startpage.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # проверка на валидность, если все ок, то логиним и перенаправляем на главную страницу
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('startpage')
    else:
        form = UserCreationForm()
    return render(request, 'base/signup.html', {'form': form})
