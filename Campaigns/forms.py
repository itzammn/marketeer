from django import forms
from .models import Campaign, Lead, Subscriber, CampaignLandingPage


class CampaignForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    
    class Meta:
        model = Campaign
        fields = ['name', 'start_date', 'end_date', 'budget', 
                  'description', 'target_audience', 'platform', 'image']
        
    
class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'campaign']

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['first_name', 'last_name', 'email', 'phone', 'city','gender']

class CampaignLandingPageForm(forms.ModelForm):
    class Meta:
        model = CampaignLandingPage
        fields = ['title', 'description', 'image']
    

    