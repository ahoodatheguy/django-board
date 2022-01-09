from django.db import models


class MessageBoard(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField()

	def __str__(self) -> str:
		return self.name


class Messages(models.Model):
	sender = models.CharField(max_length=15)
	subject = models.CharField(max_length=30)
	content = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True)
	board = models.ForeignKey(MessageBoard, on_delete=models.CASCADE)

	def __str__(self) -> str:
		return f'{self.sender} - {self.content}'
