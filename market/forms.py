from django import forms
from .models import Dynamic,comment,Category

class DynamicForm(forms.ModelForm):
    class Meta:
        model = Dynamic
        fields=['title','content','img','kind']



class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields= ['content']