from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=20, db_index=True, default='Anonymous'
      )  
    body = models.CharField(
        'body', blank=True, null=True, max_length=140, db_index=True    
    )
    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )
    image= CloudinaryField('image', blank=True, db_index=True
    )

    like_count = models.PositiveIntegerField(
        'Like Count',default= 0, null=True, blank=True
        )