from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Deck(models.Model):
		name = models.CharField(default='SpyCat', max_length=100)

		def _str_(self):
			return self.name

class Match(models.Model):
	player = models.ForeignKey(User, on_delete=models.CASCADE)
	mformat = models.CharField(default='Legacy', max_length=100)
	deck = models.ForeignKey(Deck, related_name="matches", on_delete=models.CASCADE)
	oppdeck = models.ForeignKey(Deck, related_name="opp_matches", on_delete=models.CASCADE)
	record = models.IntegerField(default=0)
	date = models.DateTimeField(default=timezone.now)

	def _str_(self):
		return self.date
		
	def get_absolute_url(self):
		return reverse('match-detail', kwargs={'pk': self.pk})
