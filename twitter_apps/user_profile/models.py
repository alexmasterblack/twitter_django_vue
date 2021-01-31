from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # symmetrical=False не будет автоматически подписываться в ответ
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    avatar = models.ImageField(upload_to='uploads/', blank=True, null=True)


User.user_profile = property(lambda person: UserProfile.objects.get_or_create(user=person)[0])
