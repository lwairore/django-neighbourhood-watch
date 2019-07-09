from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile, Neighbourhood
from .forms import NewProfile, EditProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
def profile(request):
    current_user = request.user
    user_neighbourhood_id = Profile.objects.get(user_id=current_user.id)
    print(user_neighbourhood_id.neighbourhood)
    # user_neighbourhood_name = Neighbourhood.objects.get(id=user_neighbourhood_id.neighbourhood)
    try:
        user_profile_details = Profile.objects.get(user_id=current_user.id)
    except:
        return redirect(new_profile)
    
    
    
    return render(request, 'profile.html', {"user_profile_details":user_profile_details, 'current_user':current_user, 'user_neighbourhood_id':user_neighbourhood_id.neighbourhood})

def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfile(request.POST, request.FILES)
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.user_id = current_user
            new_profile.save()
            return redirect(profile)
    else:
        form = NewProfile()

    return render(request, 'new_profile.html', {'form':form})


def edit_profile(request):
    current_user = request.user
    user_profile = Profile.objects.get(user_id=current_user)
    if request.method == 'POST':
        form = EditProfile(request.POST)
        if form.is_valid():
            if request.POST.get('bio'):
                user_profile.bio = request.POST.get('bio')
                user_profile.save()
            if request.POST.get('location'):
                user_profile.location = request.POST.get('location')
                user_profile.save()
            if request.POST.get('neighbourhood'):
                print('-' * 30)
                print(request.POST.get('neighbourhood'))

                user_neighbourhood = Neighbourhood.objects.get(id=request.POST.get('neighbourhood'))
                user_profile.neighbourhood = user_neighbourhood
                user_profile.save()

    else:        
        form = EditProfile()
    return render(request, 'edit_profile.html', {'form':form})
