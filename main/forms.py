from django import forms


class PostToBoard(forms.Form):
	sender = forms.CharField(max_length=15)
	subject = forms.CharField(max_length=30)
	content = forms.CharField(widget=forms.Textarea)
