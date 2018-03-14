from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserForm, ProfileForm


def home(request):

    return render(request, 'account/home.html', {})

def signup(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            obj = User.objects.get(username=user_form.cleaned_data['username'])
            profile = Profile.objects.get(user=obj)
            profile.contact = profile_form.cleaned_data['contact']
            profile.save()

            return redirect('/')




    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'account/signup.html', {
                        'user_form': user_form,
                        'profile_form': profile_form
                })
