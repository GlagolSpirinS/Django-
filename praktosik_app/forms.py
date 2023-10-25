from django import forms

class FeedBackForm(forms.Form):
    subject = forms.CharField(
        max_length=20,
        min_length=3,
        strip=True,
        label='Тема отзыва',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    body_subject = forms.CharField(
        max_length=150,
        min_length=3,
        strip=True,
        label='Содержание отзыва',
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    stars = forms.FloatField(
        max_value=5,
        min_value=0,
        step_size=0.5,
        label='Рейтинг отзыва',
        initial=2.5,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    img_FeedBack = forms.DateField(
        label='Фото отзыва',
        help_text='Загрузите фото товара',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

class PoiskPeopl(forms.Form):
    subject = forms.CharField(
        max_length=20,
        min_length=3,
        strip=True,
        label='Имя продавца/Название магазина',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    stars = forms.FloatField(
        max_value=5,
        min_value=0,
        step_size=0.5,
        label='Рейтинг продавца/магазина',
        initial=2.5,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class Item_search(forms.Form):
    subject = forms.CharField(
        max_length=20,
        min_length=3,
        strip=True,
        label='Название товара',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    stars = forms.FloatField(
        max_value=5,
        min_value=0,
        step_size=0.5,
        label='Рейтинг товара',
        initial=2.5,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class ProductForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Название товара',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    opis = forms.CharField(
        max_length=200,
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        label='Описание товара'
    )
    price = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        label='Цена товара',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    image = forms.ImageField(
        label='Изображение товара',
        help_text='Загрузите изображение товара',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    category = forms.ChoiceField(
        choices=[('электроника', 'Электроника'), ('одежда', 'Одежда'), ('дом', 'Дом')],
        label='Категория товара',
        widget=forms.Select(attrs={'class': 'form-control'})
    )