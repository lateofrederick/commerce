from django import forms

from commerce.models.book import Book


class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'description':
                field.widget = forms.Textarea(attrs={'class': 'form-control', 'placeholder': field_name})
            else:
                field.widget.attrs = {'class': 'form-control', 'placeholder': field_name}
