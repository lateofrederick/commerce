from django.contrib import messages
from django.shortcuts import redirect, render

from commerce.forms.registration_form import RegistrationForm
from commerce.models.user_profile import UserProfile


def create_new_account(request):
    """
    This view creates a new user associated with a profile and given a group
    as a buyer or seller
    """

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            user_type = form.cleaned_data['user_type']

            role = None
            if user_type == 'BUYER':
                role = UserProfile.BUYER

            if user_type == 'SELLER':
                role = UserProfile.SELLER
                
            try:
                UserProfile.create_user(username=username, password=password, first_name=first_name,
                                        last_name=last_name, email=email, user_role=role)
                messages.success(request, 'account created successfully')
                return redirect('commerce:login_into_account')
            except KeyError as e:
                messages.error(request, f"Failed to create account. Please try again {e}")
        return redirect('commerce:create_new_account')

    else:
        form = RegistrationForm()
        return render(request, 'commerce/account/register.html', {
            'register_form': form
        })

