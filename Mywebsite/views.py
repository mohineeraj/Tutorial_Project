from django.shortcuts import render
from tutorials.models import TutorialDetails, TutorialCategory

def index(request):
	all_tutorials = TutorialDetails.objects.all()
	category = TutorialCategory.objects.all()
	return render(request, 'index.html', {'all_tutorials': all_tutorials, 'category': category})

def about_us(request):
	category = TutorialCategory.objects.all()
	return render(request, 'about_us.html',{'category': category})