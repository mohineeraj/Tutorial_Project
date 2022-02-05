from django.db import models

# Create your models here.
class TutorialCategory(models.Model):
	"""TutorialCategory
	"""
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name.title()

class TutorialDetails(models.Model):
	"""TutorialDetails
	"""
	category_name = models.ForeignKey(TutorialCategory, on_delete=models.CASCADE)
	topic = models.CharField(max_length=255)
	body = models.TextField()
	