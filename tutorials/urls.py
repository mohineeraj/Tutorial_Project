from django.urls import path
from .views import tutorial, category, new_tutorial, display_tutorial
from userauth.views import Logout
urlpatterns = [
    path('category/<str:category>', tutorial),
    path('category', category),
    path('new_tutorial', new_tutorial),
    path('<int:tutorial_id>', display_tutorial),
    path('Logout',Logout)
]
    