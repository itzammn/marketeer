from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='campaigns'),
    path('create/', views.create_campaign, name='create_campaign'),
    path('<slug:slug>/', views.clicked_campaign, name='clicked_campaign'),
    path('<slug:slug>/details', views.show_campaign, name='campaign_detail'),
    path('<slug:slug>/edit', views.edit_campaign, name='campaign_edit'),
    path('<slug:slug>/delete', views.delete_campaign, name='campaign_delete'),
    path('<slug:slug>/leads/<int:id>/', views.lead_details, name='lead_details'),
    path('<slug:slug>/leads/<int:id>/convert', views.convert_lead, name='convert_lead'),
    path('<slug:slug>/landing/create', views.create_campaign_landing, name='create_campaign_landing'),
    path('<slug:slug>/landing/edit', views.edit_campaign_landing, name='edit_campaign_landing'),
]