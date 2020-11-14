from django import forms

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'type': 'text', 'name': 'First name', 'placeholder': 'Имя'}),
        label='Имя')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.save()