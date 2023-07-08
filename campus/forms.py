from typing import Text
from django import forms

from libs.validators import PHONE_REGEX


class ParticipantForm(forms.Form):
    full_name = forms.CharField(max_length=100,
                                label="Your Full Name",
                                error_messages={
                                    'required': 'Please let us know what to call you!'},
                                widget=forms.TextInput(attrs={'placeholder': 'Enter your full name (required)'}))
    email = forms.EmailField(label="You Email",
                             widget=forms.EmailInput(
                                 attrs={'placeholder': 'Enter your Email (required) '}),
                             error_messages={"invalid": " *Enter a valid Email address"})
    phone_number = forms.CharField(max_length=15,
                                   validators=[PHONE_REGEX],
                                   label="Your Phone Number",
                                   widget=forms.TextInput(attrs={
                                       'placeholder': 'Enter your phone number (optional) '
                                   }),
                                   required=False)
    message = forms.CharField(widget=forms.Textarea)