from django.core.validators import MinLengthValidator
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()

    class Meta:
        verbose_name = 'Author'

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posts', null=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        related_name='posts',
        null=True,
    )
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique = True)
    content = models.TextField(validators = [MinLengthValidator(10)])
    tags = models.ManyToManyField('Tag', related_name='posts')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Post'

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.caption}'

    class Meta:
        verbose_name = 'Tag'
