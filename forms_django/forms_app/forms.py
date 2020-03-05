from django import forms
from django.core import validators

# def checkz(value):
#    if value[0].lower() != 'z':
#       raise forms.ValidationError(" name needs to start with z ")

class FormName(forms.Form):
    # name = forms.CharField(validators=[checkz])
    name = forms.CharField()
    email = forms.EmailField()
    vemail = forms.EmailField(label="email again")
    text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False,
    #                               widget= forms.HiddenInput,
    #                               validators = [validators.MaxLengthValidator(0)])

 # how to use all custom validator rather than use single validators
# i want to check email by varify email again
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['vemail']

        if email != vemail:
            raise forms.ValidationError(" make sure email match")


# validator for botcatcher
# clean is the default value we can call
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0 :
    #         raise forms.ValidationError('got you Bot !!!')
    #         print('hello bot ')
    #     return botcatcher
