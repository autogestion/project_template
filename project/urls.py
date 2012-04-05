from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
                    {'template_name': 'login.html'}, name='login_auth'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                    dict(next_page='/accounts/login/'), name='logout'),
    url(r'^auth/', include('social_auth.urls')),
    url(r'^profile/details/$',
                    'project.apps.profile.views.profile_details'),
    url(r'^profiles/$', 'profiles.views.profile_list',
                    {'public_profile_field': 'public_profile_field'}),
    (r'^profiles/', include('profiles.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
