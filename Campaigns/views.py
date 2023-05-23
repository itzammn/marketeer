from django.shortcuts import render, redirect
from .models import Campaign, Lead, Subscriber, LeadConversion, CampaignLandingPage
from .forms import CampaignForm, SubscriberForm, CampaignLandingPageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import plotly.express as px

@login_required
def index(request):
    total_campaigns = Campaign.objects.filter(client=request.user).count()
    total_leads = Lead.objects.filter(campaign__client=request.user).count()
    campaigns = Campaign.objects.filter(client=request.user)
    ctx = {
        'total_campaigns':total_campaigns,
        'total_leads':total_leads,
        'campaigns':campaigns
    }
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
    lead_conversion = LeadConversion.objects.filter(lead__campaign=camp)
    days, total_leads = [], []
    for lead in leads:
        days.append(lead.created_at.strftime("%d %b"))
        total_leads.append(lead.campaign.lead_set.filter(created_at__date=lead.created_at.date()).count())
        print(f'days: {days} => total_leads: {total_leads}')    
    try:
        line_graph = px.area(x=days, y=total_leads, title='Leads per day')
        line_graph.update_xaxes(title_text='Days')
        line_graph.update_yaxes(title_text='Leads')
        line_graph.update_traces(mode='lines+markers')
        line_graph.update_layout(
            title={
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
        line_graph = line_graph.to_html(full_html=False, default_height=500,)
    except:
        line_graph = None
    # check if campaign has a landing page
    landing_page = CampaignLandingPage.objects.filter(campaign=camp).first()
    if landing_page:
        has_landing_page = True
    else:
        has_landing_page = False
    ctx = {
        'camp':camp,
        'leads':leads,
        'days':days,
        'total_leads':total_leads,
        'line_graph':line_graph, 
        'lead_conversion':lead_conversion, 
        'has_landing_page':has_landing_page}
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

@login_required
def lead_details(request,slug, id):
    lead = Lead.objects.get(id=id)
    subcriber = Subscriber.objects.filter(email=lead.email).first()
    camp = Campaign.objects.get(slug=slug)
    ctx = {'lead':lead, 'subcriber':subcriber, 'camp':camp}
    return render(request,"campaigns/lead_details.html", ctx)

@login_required
def convert_lead(request, slug, id):
    lead = Lead.objects.get(id=id)
    camp = Campaign.objects.get(slug=slug)
    conversion = LeadConversion.objects.filter(lead=lead).first()
    if conversion:
        conversion.converted = True
        conversion.save()
    else:
        LeadConversion.objects.create(lead=lead, converted=True)
    messages.success(request,"Lead converted successfully")
    return redirect('campaign_detail', slug=slug)
   

@login_required
def clicked_campaign(request, slug):
    cam = Campaign.objects.get(slug=slug)
    # increase lead count in Lead
    # show campaign landing data
    try:
        Lead.objects.create(email=request.user.email, name=request.user.username, campaign=cam)
    except:
        print('Lead already exists')
    landing_page = CampaignLandingPage.objects.get(campaign=cam)
    # send subscriber form
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            subs= form.save(commit=False)
            subs.campaign = cam
            subs.save()
            # get lead from email and campaign
            lead = Lead.objects.filter(email=request.user.email, campaign=cam).first()
            print(lead)
            LeadConversion.objects.create(lead=lead, campaign=cam, converted=True)
            messages.success(request,"Your details have been submitted successfully")
            return redirect('clicked_campaign', slug=slug)
    else:
        form = SubscriberForm()
    ctx = {'landing_page':landing_page, 'form':form, 'cam':cam}
    return render(request,"campaigns/clicked_campaign.html", ctx)
    
        # print(e)
        # messages.error(request,"Campaign landing page not found")
        # return redirect('landing')
    

@login_required
def create_campaign_landing(request, slug):
    camp = Campaign.objects.get(slug=slug)
    if request.method == 'POST':
        form = CampaignLandingPageForm(request.POST,request.FILES)
        if form.is_valid():
            landing_page = form.save(commit=False)
            landing_page.campaign = camp
            landing_page.save()
            messages.success(request,"Campaign landing page created successfully")
            return redirect('campaign_detail', slug=slug)
    else:
        form = CampaignLandingPageForm()
    ctx = {'form':form, 'camp':camp}
    return render(request,"campaigns/create_campaign_landing.html", ctx)

@login_required
def edit_campaign_landing(request, slug):
    camp = Campaign.objects.get(slug=slug)
    landing_page = CampaignLandingPage.objects.get(campaign=camp)
    if request.method == 'POST':
        form = CampaignLandingPageForm(request.POST,request.FILES,instance=landing_page)
        if form.is_valid():
            landing_page = form.save(commit=False)
            landing_page.campaign = camp
            landing_page.save()
            messages.success(request,"Campaign landing page updated successfully")
            return redirect('campaign_detail', slug=slug)
    else:
        form = CampaignLandingPageForm(instance=landing_page)
    ctx = {'form':form, 'camp':camp}
    return render(request,"campaigns/edit_campaign_landing.html", ctx)
