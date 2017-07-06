from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from models import Profile


class SignUpForm(UserCreationForm):
    utype = forms.CharField(max_length=30, required=False,initial='3',widget=forms.HiddenInput(),label='')
    

    class Meta:
        model = User
        fields = ('username','password1')
		
#class Profile(forms.ModelForm):
 #   class Meta:
  #      model = Profile
   #     fields = ('utype')		
		 
def save(self, commit=True):
        user = Super(RegistrationForm, self).save(commit=False)
        user.profile.utype = self.cleaned_data['utype']

        if commit:
            user.save()

        return user	
	
class EditProfileform(UserChangeForm):
    utype = forms.CharField(max_length=30, required=False)

    class Meta:
        model =User
        fields = {
		
		
		
		}
		

    
   