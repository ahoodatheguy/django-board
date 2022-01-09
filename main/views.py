from django.shortcuts import redirect, render

from main.forms import PostToBoard
from main.models import MessageBoard, Messages


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


def post_message(response, id):
	board = MessageBoard.objects.get(id=id)
	messages = board.messages_set.all()

	form = PostToBoard()
	if response.method == 'POST':
		if response.POST.get('post'):
			form = PostToBoard(response.POST)

		if form.is_valid():
			sender = form.cleaned_data['sender']
			subject = form.cleaned_data['subject']
			content = form.cleaned_data['content']
			new_post = Messages(sender=sender, subject=subject,
			                    content=content, board=board)
			new_post.save()
			return redirect('/')
	else:
		form = PostToBoard()
	context = {
		'title': f'Post to {board.name}',
		'id': id,
		'board': board,
		'messages': messages,
		'form': form
        }
	return render(response, 'main/post.html', context)
