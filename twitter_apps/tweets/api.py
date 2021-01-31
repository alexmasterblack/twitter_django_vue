import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Tweet


@login_required
def add_new_tweet(request):
    data = json.loads(request.body)
    body = data['body']
    tweet = Tweet.objects.create(body=body, created_by=request.user)
    return JsonResponse({'success': True})
