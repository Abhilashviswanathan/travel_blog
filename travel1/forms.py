from django import forms
from .models import blogmodel  
from .models import Profile
from django.contrib.auth.models import User

class blogform(forms.ModelForm):
    class Meta:
        model = blogmodel  
        fields = ('title', 'content', 'travel_photos')  

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blog title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your blog content here...'}),
            'travel_photos': forms.FileInput(), 
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture'] 

