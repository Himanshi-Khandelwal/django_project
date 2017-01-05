from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.name


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField(blank=True)
	def __unicode__(self):
		return self.user.username
