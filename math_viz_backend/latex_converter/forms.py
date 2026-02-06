from django import forms

class TextForm(forms.Form):
    text_input = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter a mathematical expression, text, equation, or LaTeX...',
            'class': 'text_form_control'
        }))
    
class UploadImageForm(forms.Form):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'image_form_control',
        })
    )

