from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Classroom, Chapter, QuesModel
from django import forms
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Enter username...'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control','placeholder':'Enter password...'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control','placeholder':'Confirm password...'})
#Classroom form
class ClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ('section',)

class addQuestionform(ModelForm):
    class Meta:
        model=QuesModel
        fields="__all__"
#Chapter form
class ChapterForm(ModelForm):
    class Meta:
        model = Chapter
        fields = ('title', 'description')
