from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message',)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
