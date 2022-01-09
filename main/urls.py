from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name="main-homepage"),
	path('boards/<int:id>', views.board, name='main-board')
]
