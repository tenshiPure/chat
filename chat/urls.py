from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import CreateView

from message.models import MessageForm
from message.views import MessageFormView, MessageCreateView

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

	url(r'^message/create/$',
		MessageCreateView.as_view()
	),

#	url(r'^message/create/$',
#		CreateView.as_view(
#			form_class = MessageForm,
#			template_name = 'message/form.html',
#			success_url = '/message/',
#		)
#	),
)
