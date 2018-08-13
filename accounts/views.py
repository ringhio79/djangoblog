from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import ProfileRegistrationForm

def register(request):
    if request.method == 'POST':
        # load the http request into two forms, user and profile
        form = UserCreationForm(request.POST)
        profile_form = ProfileRegistrationForm(request.POST, request.FILES)
        
        
        # if both forms are valid, we craeate the USer and Profile in the Database
        if form.is_valid() and profile_form.is_valid():
            # Save the User object to DB, by calling the save directly on the Form.Save
            # Retun the USer object so that we can use it later to set the user of the Profile
            user = form.save()
            
            # Get the Profile from the profile_form, without actually saving anything to the DB (using commit=false)
            profile = profile_form.save(commit=False)
            # use the user created above as a value for the user in profile
            profile.user = user
            # save the new profile to the database
            profile.save()
            
            # now we can log in as the user
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        profile_form = ProfileRegistrationForm
    return render(request, 'accounts/register.html', {'form': form, 'profile_form': profile_form})