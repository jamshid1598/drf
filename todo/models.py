from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
# from rest_framewrk.serializers import Modelserializers


# Create your models here.



class Category(models.Model):
	name    = models.CharField(max_length=200, unique=True, verbose_name="Category name")
	slug    = models.SlugField(max_length=250, verbose_name='Slug')

	image   = models.ImageField(upload_to='category-image/', blank=True, null=True, verbose_name='Category Image')
	caption = models.CharField(max_length=500, blank=True, null=True, verbose_name='Image Caption')

	def __str__(self):
		return self.name
	
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		return super().save(*args, **kwargs)

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url


class ToDo(models.Model):
	class Reapeted(models.TextChoices): # level of importances of tesk
		RED    = 'red', _('Red')
		ORANGE = 'orange', _('Orange')
		YELLOW = 'yellow', _('Yellow')
		GREEN  = 'green', _('Green')
		BLUE   = 'blue', _('Blue')
		PURPLE = 'purple', _('Purple')
		__empty__ = _('(not importent)')

	category  = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL, related_name='activity_category', verbose_name='Category')
	task_marked_as = models.CharField(max_length=100, choices=Reapeted.choices, default=Reapeted.__empty__, blank=True, null=True, verbose_name='Level Of Task')

	task      = models.CharField(max_length=500, unique=True, verbose_name='Activity')
	slug      = models.SlugField(max_length=600, verbose_name='Slug')
	started   = models.DateTimeField(blank=True, null=True, verbose_name='Starting Time') # determines activity starts time for activity
	ended     = models.DateTimeField(blank=True, null=True, verbose_name='Ending Time') # determines activity ends time for activity  
	completed = models.BooleanField(default=False, verbose_name='Completed') # determines that activity is completed or not

	def __str__(self):
		return self.activity + " | " + str(self.completed)
	
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.activity)
		return super().save(*args, **kwargs)


class Image(models.Model):
	todo = models.ForeignKey(ToDo, on_delete=models.CASCADE, related_name='todo_image', verbose_name='Activity')

	image = models.ImageField(upload_to='activity/%d/%m/%Y/', verbose_name='Activity Image')
	caption = models.CharField(max_length=300, blank=True, null=True, verbose_name='Caption')

	def __str__(self):
		return str(self.pk) + " | " + self.todo.task

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url	