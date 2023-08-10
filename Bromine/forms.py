from django import forms
from .models import MyBlogInfo, Category, Comment




choices = Category.objects.all().values_list('name', 'name')

choices_items = []

for items in choices:
    choices_items.append(items)



class AddPostForm(forms.ModelForm):
    class Meta:
        model = MyBlogInfo
        fields = ('title', 'author', 'image', 'category', 'content')

        widgets = {
           'title' : forms.TextInput(attrs={'class':'form-control'}),
           'author':forms.TextInput(attrs={'class': 'form-control','value': '','id': 'jay', 'type': 'hidden'}),
            #'author' : forms.Select(attrs={'class':'form-control'}),
           'category' : forms.Select(choices = choices_items, attrs={'class':'form-control'}),      # Category field
        
           'content' : forms.Textarea(attrs={'class':'form-control'}),
        }


    
class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
           'name' : forms.TextInput(attrs={'class':'form-control'}),
           
            #'author' : forms.Select(attrs={'class':'form-control'}),
           
           'body' : forms.Textarea(attrs={'class':'form-control'}),
        }