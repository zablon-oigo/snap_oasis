from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model=ConversationMessage
        fields=('content',)
        widgets={
            'content':forms.Textarea(attrs={
                'placeholder':'Leave a message here and the seller will contact you in a short while ☺️☺️☺️...',
                'class':'w-full py-4 px-6 rounded-xl border border-gray-700'
            })
        }
