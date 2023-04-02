from django.utils.text import slugify
import random


def unique_slug_generator(text):
    new_slug = slugify(text)
    from .models import Post
    if Post.objects.filter(slug=new_slug).exists():
        return unique_slug_generator(text + str(random.randint(1, 100000)))
    return new_slug