from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    #define a text with limited nummber of characters
    title = models.CharField(max_length=200)

    # this is for long text without a limit
    text = models.TextField()

    #this is a date and time
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #this is link to another model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    #publish method
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #method that will return string representation of the object Post
    def __str__(self):
        return self.title
