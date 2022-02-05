from django import forms

from .models import TutorialCategory, TutorialDetails

class TutorialCategoryForm(forms.ModelForm):
	class Meta:
		model = TutorialCategory
		fields = ['name']

class TutorialDetailsForm(forms.ModelForm):
	class Meta:
		model = TutorialDetails
		fields = ['category_name', 'topic', 'body']