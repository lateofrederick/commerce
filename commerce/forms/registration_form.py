from django import forms


class RegistrationForm(forms.Form):
    USER_TYPES = (
        ('BUYER', 'buyer'),
        ('SELLER', 'seller')
    )
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    user_type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=USER_TYPES)

    def clean(self):
        super().clean()

        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if len(password) < 8:
            self._errors['password'] = self.error_class(['Minimum of 8 characters required'])

        if password != confirm_password:
            self._errors['confirm_password'] = self.error_class(['Password mismatch'])
