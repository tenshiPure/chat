from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import CreateView, FormView

from message.models import UserForm
from message.views import MessageFormView, MessageCreateView, TagListView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/',
		include(admin.site.urls)
	),

	url(r'^login/$',
		'django.contrib.auth.views.login',
		{'template_name' : 'common/login.html'}
	),

	url(r'^logout/$',
		'django.contrib.auth.views.logout',
		{'template_name' : 'common/logout.html'}
	),

	url(r'^dev/delete/$',
		'message.views.dev_delete'
	),

	url(r'^user/form/$',
		FormView.as_view(
			form_class = UserForm,
			template_name = 'user/form.html'
		)
	),

	url(r'^user/create/$',
		CreateView.as_view(
			form_class = UserForm,
			template_name = 'user/form.html',
			success_url = '/user/form'
		)
	),

	url(r'^message/(\d+)/(\w*)$',
		MessageFormView.as_view()
	),

	url(r'^message/create/(\d+)$',
		MessageCreateView.as_view()
	),

	url(r'^tag/(\d+)$',
		TagListView.as_view()
	),
)
