from django.urls import path
from .views import save_enquiry
from .views import admin_page
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import enquiry_data

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('User/', views.customer, name='customer'),
    # path('employee/', views.employee, name='employee'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('saveEnquiry', views.saveEnquiry, name='saveEnquiry')
    path('save-enquiry/', save_enquiry, name='save_enquiry'),
    path('success/', views.success_view, name='success'),
    # path('admin/', admin_page, name='admin'),
    path('adminpage/', admin_page, name='admin_page'),
    path('enquiry_data/', enquiry_data, name='enquiry_data'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)