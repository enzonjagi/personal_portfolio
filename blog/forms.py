from django import forms

class CommentForm(forms.Form):
    """A form to allow users to add comments to posts"""

    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your Name"
            }
        )
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "We unaonaje hii story?"
            }
        )
    )