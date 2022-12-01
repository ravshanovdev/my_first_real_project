from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

from .models import Teacher

User = get_user_model()


class TeacherForm(UserCreationForm):
    phone = forms.CharField(max_length=200)
    about = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name',
            'username', 'phone', 'about',
            'password1', 'password2'
        )

    def save(self, commit: bool = ...):
        try:
            phone = self.cleaned_data.pop('phone')
            about = self.cleaned_data.pop('about')
        except:
            phone, about = None, None
        user = super().save(commit)
        teacher = Teacher(phone=phone, about=about, user=user)
        teacher.save()
