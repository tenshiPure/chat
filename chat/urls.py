from django.conf.urls import patterns, include, url
from django.contrib.auth.forms import UserCreationForm
from django.contrib import admin
from django.views.generic import CreateView, FormView

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

	url(r'^user/form/$',
		FormView.as_view(
			form_class = UserCreationForm,
			template_name = 'user/form.html'
		)
	),

	url(r'^user/create/$',
		CreateView.as_view(
			form_class = UserCreationForm,
			template_name = 'user/form.html',
			success_url = '/user/form'
		)
	),

	url(r'^message/(\d+)/(\w*)$',
		MessageFormView.as_view()
	),

	url(r'^message/create/$',
		MessageCreateView.as_view()
	),
)
