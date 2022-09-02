from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from commerce.forms.new_book_form import NewBookForm
from commerce.utils.custom_decorators import is_seller


@login_required(login_url='/commerce/accounts/login')
@is_seller()
def upload_new_book(request):
    """ This view allows a seller to upload a new book into the system """
    if request.method == 'POST':
        form = NewBookForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Book successfully added')
        else:
            messages.error(request, 'Failed to add book')
        return redirect('commerce:upload_new_book')
    else:
        form = NewBookForm()
        return render(request, 'commerce/homepage/seller/upload_book.html', {'form': form})
