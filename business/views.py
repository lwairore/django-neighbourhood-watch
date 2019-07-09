from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Business
from profile_user.models import Profile, Neighbourhood
from .forms import NewBusiness
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def business(request):
    current_user = request.user
    user_location = Profile.objects.get(user_id=current_user.id)
    user_location_id = Neighbourhood.objects.get(id=user_location.neighbourhood_id)
    all_business = Business.objects.filter(neighbourhood_id=user_location_id.id)
    if request.method == 'POST':
        form = NewBusiness(request.POST, request.FILES)
        if form.is_valid():
            new_business = form.save(commit=False)
            new_business.user_id = current_user
            new_business.neighbourhood_id = user_location_id
            new_business.save()
    else:
        form = NewBusiness()

    return render(request, 'business.html', {'form':form, 'businesses':all_business})
        

