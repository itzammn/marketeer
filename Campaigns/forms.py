from django import forms
from .models import Campaign, Lead


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

    