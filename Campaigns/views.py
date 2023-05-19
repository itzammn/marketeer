from django.shortcuts import render, redirect
from .models import Campaign, Lead, Subscriber, LeadConversion
from .forms import CampaignForm, LeadForm
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
    ctx = {
        'camp':camp,
        'leads':leads,
        'days':days,
        'total_leads':total_leads,
        'line_graph':line_graph, 
        'lead_conversion':lead_conversion}
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
   