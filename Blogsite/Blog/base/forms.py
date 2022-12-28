from . models import BlogPost,Comment
from django import forms

class BlogPostForm(forms.ModelForm):
    class Meta():
        model = BlogPost
        fields = ['title','text','category']

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontents'})
        }

    
class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['text']
        

        widgets = {
            'text':forms.Textarea(attrs={'class':' form-control'})
        }

