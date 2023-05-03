from django.shortcuts import render, redirect
from .models import Campaign, Lead
from .forms import CampaignForm, LeadForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def index(request):
    total_campaigns = Campaign.objects.filter(client=request.user).count()
    total_leads = Lead.objects.filter(campaign__client=request.user).count()
    ctx = {'total_campaigns':total_campaigns,'total_leads':total_leads}
    return render(request,"campaigns/index.html", ctx)

@login_required
def create_campaign(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST,request.FILES)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.client = request.user
            campaign.save()
            messages.success(request,"Campaign created successfully")
            return redirect('campaigns')
    else:
        form = CampaignForm()
    ctx = {'form':form}
    return render(request,"campaigns/create.html", ctx)

@login_required
def show_campaign(request, slug):
    camp = Campaign.objects.get(slug=slug)
    leads = Lead.objects.filter(campaign=camp)
    ctx = {'campaign':camp,'leads':leads}
    return render(request,"campaigns/show.html", ctx)

@login_required
def edit_campaign(request, slug):
    camp = Campaign.objects.get(slug=slug)
    if request.method == 'POST':
        form = CampaignForm(request.POST,request.FILES,instance=camp)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.client = request.user
            campaign.save()
            messages.success(request,"Campaign updated successfully")
            return redirect('campaigns')
    else:
        form = CampaignForm(instance=camp)
    ctx = {'form':form}
    return render(request,"campaigns/edit.html", ctx)

@login_required
def delete_campaign(request, slug):
    camp = Campaign.objects.get(slug=slug)
    camp.delete()
    messages.success(request,"Campaign deleted successfully")
    return render(request,"campaigns/delete.html")