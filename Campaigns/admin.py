from django.contrib import admin

from .models import Campaign, Lead,LeadConversion, CampaignLandingPage, Subscriber

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ['name','client','budget','start_date','end_date','status']
    list_filter = ['client','status']
    search_fields = ['name','client__username']

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['name','email','campaign']
    list_filter = ['campaign']
    search_fields = ['name','email','campaign__name']


@admin.register(LeadConversion)
class LeadConversionAdmin(admin.ModelAdmin):
    list_display = ['lead','converted','converted_at']
    list_filter = ['converted']
    search_fields = ['lead__name','lead__email','lead__campaign__name']

@admin.register(CampaignLandingPage)
class CampaignLandingPageAdmin(admin.ModelAdmin):
    list_display = ['title','campaign']
    list_filter = ['campaign']
    search_fields = ['title','campaign__name']

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone','city']
    list_filter = ['city']
    search_fields = ['first_name','last_name','email','phone','city']
    