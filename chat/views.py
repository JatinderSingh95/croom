from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.contrib.auth.models import User
from chat.form import SignUpForm, UserChangeForm, EditProfileform
#ProfileForm
data={}

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.utype = form.cleaned_data.get('utype')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('server_list')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


#class ServerForm(ModelForm):
 #   class Meta:
  #      model = Class
   #     fields = ['Title','user']
	
		
def server_list(request, template_name='server_list.html'):
	users = User.objects.all()
	#data = {}
	data['object_list'] = users
		
	return render(request, template_name)
	
def Function(request):
	
		return render(request, 'rest.html')
	
def Ateacher1(request, template_name='update.html'):

    users = User.objects.all()
	#data = {}
    data['object_list'] = users
    return render(request, template_name, data)

			
def server_update(request, pk, template_name='Addrest.html'):
    users = get_object_or_404(User, pk=pk)
    form = EditProfileform(request.POST or None, instance=users)
    if form.is_valid():
        user=form.save()
		#user.refresh_from_db()  # load the profile instance created by the signal
        user.profile.utype = form.cleaned_data.get('utype')
        user.save()
        return redirect('Ateacher1')
    return render(request, template_name, {'form':form})	

#def server_update(request,pk):
 #   users = User.objects.all().select_related('profile')
  #  if request.method == 'POST':
   #     user_form = SignUpForm(request.POST, instance=users)
   #     profile_form = EditProfileform(request.POST, instance=users)
   #     if user_form.is_valid() and profile_form.is_valid():
   #         user_form.save()
   #         profile_form.save()
   ##         messages.success(request, _('Your profile was successfully updated!'))
   #         return redirect('settings:profile')
   #     else:
   #         messages.error(request, _('Please correct the error below.'))
  #  else:
  #      user_form = SignUpForm(instance=request.user)
  #      profile_form = EditProfileform(instance=request.user.profile)
  #  return render(request, 'Addrest.html', {
  #      'user_form': user_form,
  #      'profile_form': profile_form
  #  })		   