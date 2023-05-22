from django.shortcuts import render
from Campaigns.models import Campaign
import pytz
import datetime

def landing(request):
    # get all campaigns for current month and year with the help of updated_at field
    campaigns = Campaign.objects.filter(
        updated_at__month=pytz.utc.localize(datetime.datetime.now()).month,
        updated_at__year=pytz.utc.localize(datetime.datetime.now()).year)
    ctx = {'campaigns':campaigns}
    return render(request,"landing.html", ctx)

def about(request):
    return render(request,"about.html")