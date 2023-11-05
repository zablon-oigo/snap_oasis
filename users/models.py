from django.db import models
from PIL import Image
from django.contrib.auth import get_user_model
User=get_user_model()

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='users/%Y/%m/%d', default='avatar.jpg')
    date_joined=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['user']
        indexes=[
            models.Index(fields=['-user',])
        ]
    def __str__(self):
        return f'Profile of {self.user.username}'
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

        img=Image.open(self.photo.path)
        if img.height > 300 and img.width > 300:
            output_size=(300,200)
            img.thumbnail(output_size)
            img.save(self.photo.path)

