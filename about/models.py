from django.db import models

class About(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()
	date = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.title