from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class League(models.Model):
	player = models.ForeignKey(User, on_delete=models.CASCADE)
	mformat = models.CharField(max_length=100)
	deck = models.CharField(max_length=100)
	record = models.IntegerField(default=0)
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.deck

	def get_absolute_url(self):
		return reverse('league-detail', kwargs={'pk': self.pk})
