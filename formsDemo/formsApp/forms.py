from typing import Any
from django import forms
from django.core import validators

class UserRegistrationForm(forms.Form):

    GENDER = [('male','Male'),('female','FEMALE')]

    firstName = forms.CharField(validators= [
        validators.MinLengthValidator(5), validators.MaxLengthValidator(20)
    ]) # type: ignore
    lastName = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    gender = forms.CharField(widget=forms.Select(choices=GENDER))
    ssn = forms.IntegerField()




    # def clean_firstName(self):
    #     inputFirstName = self.cleaned_data['firstName']
    #     if len(inputFirstname) > 20:
    #         raise forms.ValidationError('the max length of firstname is 20 characters')
    #     return inputFirstname
    
    # def clean_email(self):
    #     inputEmail = self.cleaned_data['email']

    #     if inputEmail.find('@')== -1:
    #         raise forms.ValidationError('The email should contain @')
    #     return inputEmail


    # def clean(self):
    #     user_cleaned_data = super().clean()
    #     inputFirstName =  user_cleaned_data['firstName']
    #     if len(inputFirstName) > 20:
    #         raise forms.ValidationError('the max length of firstname is 20 characters')
        
    #     inputEmail = user_cleaned_data['email']

    #     if inputEmail.find('@')== -1:
    #         raise forms.ValidationError('The email should contain @')