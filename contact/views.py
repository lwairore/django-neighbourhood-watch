from django.shortcuts import render, redirect
from .models import Contact
from .forms import NewContact
from profile_user.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def contact(request):
    current_user = request.user
    user_location = Profile.objects.get(user_id=current_user.id)
    location_specific_contact = Contact.objects.filter(location=user_location.location)
    if request.method == 'POST':
        form = NewContact(request.POST)
        if form.is_valid():
            new_contact = form.save(commit=False)
            new_contact.location = user_location.location
            new_contact.save()

    else:
        form = NewContact()
    return render(request, 'contact.html', {'form':form, 'locations':location_specific_contact})
