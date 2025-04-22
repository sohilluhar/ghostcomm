# core/forms.py

from django import forms
from .models import Message

class CreateGroupForm(forms.Form):
    topic = forms.CharField(
        max_length=255,
        label="Group Topic",
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Cybersecurity Talk'})
    )

class JoinGroupForm(forms.Form):
    group_id = forms.CharField(
        max_length=6,
        label="Group ID",
        widget=forms.TextInput(attrs={'placeholder': 'Enter 6-digit Group ID'})
    )
    username = forms.CharField(
        max_length=30,
        label="Your Anonymous Name",
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Phantom1023'})
    )

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Type your anonymous message...',
                'rows': 2
            })
        }
