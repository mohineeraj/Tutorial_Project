from django.shortcuts import render
from .forms import TutorialCategoryForm, TutorialDetailsForm
from .models import TutorialCategory, TutorialDetails
from django.http import HttpResponse

# Create your views here.
def tutorial(request, category):
	category_id = TutorialCategory.objects.get(name=category).id
	details = TutorialDetails.objects.filter(category_name_id=category_id)
	category = TutorialCategory.objects.all()
	return render(request,'tutorials.html', {'details': details, 'category': category})

def category(request):
	if request.method == 'POST':
		form = TutorialCategoryForm(request.POST)
		if form.is_valid():
			form.save()
			category = TutorialCategory.objects.all()
			return render(request, 'tutorial_category_successfully.html')
	else:
		form = TutorialCategoryForm()
		category = TutorialCategory.objects.all()
		return render(request, 'category.html', {'category':category, 'form': form})

def new_tutorial(request):
	if request.method == 'POST':
		form = TutorialDetailsForm(request.POST)
		if form.is_valid():
			form.save()
			category = TutorialCategory.objects.all()
			return render(request, 'tutorial_created_successfully.html', {'category': category})
	else:
		form = TutorialDetailsForm()
		category = TutorialCategory.objects.all()
	return render(request, 'new_tutorial.html', {'category': category, 'form': form})

 
def display_tutorial(request, tutorial_id):
	details = TutorialDetails.objects.filter(id=tutorial_id)
	category = TutorialCategory.objects.all()
	return render(request, 'display_tutorial.html', {'details': details, 'category': category})