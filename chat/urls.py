from django.conf.urls import patterns, include, url
from django.contrib import admin

from message.views import MessageFormView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

	url(r'^login/$',
		'django.contrib.auth.views.login',
		{'template_name' : 'common/login.html'}
	),

	url(r'^logout/$',
		'django.contrib.auth.views.logout',
		{'template_name' : 'common/logout.html'}
	),

	url(r'^message/$',
		MessageFormView.as_view()
	),
)
