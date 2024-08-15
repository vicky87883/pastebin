from django import forms
from .models import TextSnippet

class TextSnippetForm(forms.ModelForm):
    class Meta:
        model = TextSnippet
        fields = ['title', 'content', 'language']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'language': forms.Select(attrs={'class': 'form-control'})
        }

    language = forms.ChoiceField(
        choices=TextSnippet.LANGUAGE_CHOICES,
        initial='plaintext',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
