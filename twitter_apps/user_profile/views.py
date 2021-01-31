from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .forms import UserProfileForm


# Create your views here.
def user_profile(request, username):
    context = {
        'user': get_object_or_404(User, username=username),
    }
    return render(request, 'user_profile/profile.html', context)


@login_required
def do_follow(request, username):
    user = get_object_or_404(User, username=username)
    request.user.user_profile.follows.add(user.user_profile)
    return redirect('user_profile', username=username)


@login_required
def do_unfollow(request, username):
    user = get_object_or_404(User, username=username)
    request.user.user_profile.follows.remove(user.user_profile)
    return redirect('user_profile', username=username)


@login_required
def settings_user(request, username):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile', username=request.user.username)
    else:
        form = UserProfileForm(instance=request.user.user_profile)
    context = {
        'user': request.user,
        'form': form
    }
    return render(request, 'user_profile/settings_user.html', context)


def follows(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'user_profile/follows.html', {'user': user})


def followers(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'user_profile/followers.html', {'user': user})
