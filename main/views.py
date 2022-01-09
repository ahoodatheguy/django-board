from django.shortcuts import render

from main.models import MessageBoard


def homepage(response):
	boards = MessageBoard.objects.all()

	context = {
		'boards': boards
        }
	return render(response, 'main/index.html', context)


def board(response, id):
	board = MessageBoard.objects.get(id=id)
	messages = board.messages_set.all()
	context = {
		'title': board.name,
		'board': board,
		'messages': messages
        }
	return render(response, 'main/board.html', context)
