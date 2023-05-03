from django.shortcuts import render,redirect
from .models import Profile
from Campaigns.models import Campaign
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def dashboard(request):
    # check if the user has a profile
    try:
        profile = Profile.objects.get(user=request.user)
        campaigns = Campaign.objects.filter(client=request.user).order_by('-created_at')
        ctx = {'profile':profile,'campaigns':campaigns}
        return render(request,"profile/dashboard.html", ctx)
    except Profile.DoesNotExist:
        messages.error(request,"You don't have a profile yet, please add one")
        return redirect('add_profile')

def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)
    return render(request,"profile/edit.html")

def view_profile(request):
    profile = Profile.objects.get(user=request.user)
    ctx = {'profile':profile}
    return render(request,"profile/view.html", ctx)

def add_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('dashboard')
    else:
        form = ProfileForm()
    return render(request,"profile/add.html",{'form':form})