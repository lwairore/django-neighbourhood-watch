from django.shortcuts import render, redirect
from .models import Events
from .forms import NewEvent
from profile_user.models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def event(request):
    current_user = request.user
    user_location = Profile.objects.get(user_id=current_user.id)
    user_location_events = Events.objects.filter(location=user_location.location)

    if request.method == 'POST':
        form = NewEvent(request.POST, request.FILES)
        if form.is_valid():
            new_event = form.save(commit=False)
            new_event.location = user_location.location
            new_event.save()
            form = NewEvent()

    else:
        form = NewEvent()
    return render(request, 'events.html', {'form':form, 'events': user_location_events})
