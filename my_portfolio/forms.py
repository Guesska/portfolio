from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', widget=forms.TextInput(attrs={'class': 'form-control col-md-6'}))
    user_email = forms.EmailField(label='Your email', widget=forms.TextInput(attrs={'class': 'form-control col-md-6'}))
    subject = forms.CharField(label='Subject', widget=forms.TextInput(attrs={'class': 'form-control col-md-12'}))
    message = forms.CharField(label='Your message', widget=forms.Textarea(attrs={'class': 'form-control col-md-12', 'rows': 5}))
