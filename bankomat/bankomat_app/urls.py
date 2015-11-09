from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	# Validations
	url(r'^$', 'bankomat_app.views.validations.cardnumber', name='home'),
	url(r'^pin_code/(?P<pk>\d+)/$', 'bankomat_app.views.validations.pin_code', name='pin_code'),
	url(r'^error/$', 'bankomat_app.views.validations.error', name='error'),

	# Operations
	url(r'^pin_code/(?P<pk>\d+)/operations/$', 'bankomat_app.views.operations.operations', name='operations'),
	url(r'^pin_code/(?P<pk>\d+)/operations/balance/$', 'bankomat_app.views.operations.balance', name='balance'),
	url(r'^pin_code/(?P<pk>\d+)/operations/get_cash/$', 'bankomat_app.views.operations.get_cash', name='get_cash'),
	url(r'^pin_code/(?P<pk>\d+)/operations/get_cash/report/$', 'bankomat_app.views.operations.report', name='report'),
)

