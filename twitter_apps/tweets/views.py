from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tweet


# Create your views here.
@login_required
def tweets(request):
    user_id = [request.user.id]
    # те на кого подписаны будут показаны в списке
    for user_by in request.user.user_profile.follows.all():
        user_id.append(user_by.user.id)
    all_tweets = Tweet.objects.filter(created_by_id__in=user_id)
    return render(request, 'tweets/tweets.html', {'tweets': all_tweets})
