from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from SSH import views

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^patient_portal/', views.patient_portal, name="patient_portal"),
                  url(r'^doctor_portal/', views.doctor_portal, name="doctor_portal"),
                  url(r'^patient_reg/', views.patient_reg, name="patient_reg"),
                  url(r'^doctor_reg/', views.doctor_reg, name="doctor_reg"),
                  url(r'^doc_login/', views.doc_login, name="doc_login"),
                  url(r'^pat_login/', views.pat_login, name="pat_login"),
                  url(r'^pat_logout/', views.pat_logout, name="pat_logout"),
                  url(r'^doc_logout/', views.doc_logout, name="doc_logout"),
                  url(r'^pat_upload/(?P<pat_id>[0-9]+)/$', views.pat_upload, name='pat_upload'),
                  url(r'^book/(?P<doc_id>[0-9]+)/$', views.book, name='book'),
                  url(r'^confirm/(?P<con_id>[0-9]+)/$', views.confirm, name='confirm'),
                  url(r'^del_app/(?P<del_id>[0-9]+)/$', views.del_app, name='del_app'),
                  url(r'^forget_pass/', views.forget_pass, name="forget_pass"),
                  url(r'^change_pass/', views.change_pass, name="change_pass"),
                  url(r'^success/', views.success, name="success"),
                  url(r'^user_profile/', views.user_profile, name="user_profile"),
                  url(r'^doc_profile/', views.doc_profile, name="doc_profile"),
                  url(r'^new_appointment/', views.new_appointment, name="new_appointment"),
                  url(r'^view_appointment/', views.view_appointment, name="view_appointment"),
                  url(r'^doc_view/', views.doc_view, name="doc_view"),
                  url(r'^doc_upload/', views.doc_upload, name="doc_upload"),
                  url(r'^doc_status/', views.doc_status, name="doc_status"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
