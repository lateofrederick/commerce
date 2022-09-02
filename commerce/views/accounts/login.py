from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from commerce.forms.login import UserAuthForm
from commerce.models.user_profile import UserProfile


def signin(request):
    """ allows a registered user to login into their account"""

    if request.method == 'POST':
        form = UserAuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user:
                group = user.groups.all().first()
                login(request, user)
                messages.add_message(request, messages.SUCCESS, message='Login successful')

                if group.name == UserProfile.SELLER:
                    return redirect('commerce:seller_homepage')
                elif group.name == UserProfile.BUYER:
                    return redirect('commerce:buyer_homepage')
            else:
                messages.add_message(request, messages.ERROR, message='Input correct username or password')
                return redirect('commerce:login_into_account')
        else:
            messages.error(request, form.errors)
            return redirect('commerce:login_into_account')

    else:
        form = UserAuthForm()
        return render(request, 'commerce/account/login.html', {
            'form': form,
        })
