from django import forms

class PostForm(forms.Form):
    title = forms.CharField(
        max_length=128,
        label='Заголовок',
        required=False
    )

    text = forms.CharField(
        max_length=512,
        label='Текст',
        widget= forms.Textarea,
        required=False
    )