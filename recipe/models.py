from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length = 150)

    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE) # need to be fix
    recipe = models.CharField(max_length = 150)
    category = models.ForeignKey(Category, on_delete = models.SET_NULL,
                                  null = True, blank = True)
    desc = models.TextField(null = False, blank = False)
    date = models.DateField(auto_now_add = True) 
    image = models.ImageField(upload_to = 'recipe_images', blank = True, null = True)

    def __str__(self):
        return self.recipe

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)

            if img.height > 800 or img.width > 800:
                output_size = (800, 800)
                img.thumbnail(output_size)
                img.save(self.image.path)