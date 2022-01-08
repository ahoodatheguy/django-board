from django.shortcuts import render


def homepage(response):
	context = {'title': 'Heres a title'}
	return render(response, 'main/index.html', context)
