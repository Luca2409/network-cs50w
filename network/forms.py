from django import forms

class NewPost(forms.Form):
    body = forms.CharField(label='body', widget=forms.Textarea, max_length=300)