from django import forms
from django.forms import ValidationError
from .models import Post

class PostForm(forms.ModelForm):
    tag = forms.CharField()

    class Meta:
            model = Post
            fields = ('category', 'content',)

    def clean_content(self):
        content = self.cleaned_data['content']
        if '바보' in content:
            raise ValidationError('금지어가 있습니다.')

        return content


#class SimpleForm(forms.Form):
#    title = forms.CharField(min_length=3, max_length=10)
#    content = forms.CharField(widget=forms.Textarea)
