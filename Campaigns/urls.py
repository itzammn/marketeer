from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='campaigns'),
    path('create/', views.create_campaign, name='create_campaign'),
    path('<slug:slug>/details', views.show_campaign, name='campaign_detail'),
    path('<slug:slug>/edit', views.edit_campaign, name='campaign_edit'),
    path('<slug:slug>/delete', views.delete_campaign, name='campaign_delete'),
<<<<<<< HEAD
    # path('<slug:slug>/leads/form', views.lead_form, name='lead_form'),
    # path('<slug:slug>/leads/update', views.show_leads, name='show_leads'),
    # path('<slug:slug>/report/view', views.view_report, name='view_report'),
=======
    path('<slug:slug>/leads/form', views.lead_form, name='lead_form'),
    path('<slug:slug>/leads/update', views.show_leads, name='show_leads'),
    path('<slug:slug>/report/view', views.view_report, name='view_report'),
>>>>>>> 66f0d4c3294bad9a9f6f18e4bff207d65eb1bedf
]