from django import forms

from catalog.models import Product, Version


forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin,forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

        #fields = ('name', 'description' ) определенные атрибуты
        #exclude = ('preview') для исключения какого-либо атрибута


    def clean_name(self):
        name = self.cleaned_data.get('name', '')

        for word in forbidden_words:
            if word.lower() in name.lower():
                raise forms.ValidationError(f"Использование слова '{word}' запрещено в названии продукта.")

        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')

        for word in forbidden_words:
            if word.lower() in description.lower():
                raise forms.ValidationError(f"Использование слова '{word}' запрещено в описании продукта.")

        return description


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


