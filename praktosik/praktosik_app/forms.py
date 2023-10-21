from django import forms


class FeedBackForm(forms.Form):
    subject = forms.CharField(
        max_length=20,
        min_length=3,
        strip=True,
        label='Тема отзыва'
    )
    body_subject = forms.CharField(
        max_length=150,
        min_length=3,
        strip=True,
        label='Содержание отзыва'
    )
    stars = forms.FloatField(
        max_value=5,
        min_value=0,
        step_size=0.5,
        label='Рейтинг отзыва',
        initial=2.5
    )
    img_FeedBack = forms.DateField(
        label='Фото отзыва',
        help_text='Загрузите фото товара'
    )


