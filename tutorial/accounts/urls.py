from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import (
    login,logout,password_reset,password_reset_done,password_reset_confirm,password_reset_complete
)
from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^Home$', views.home),
    url(r'^EnterTask$', login, {'template_name': 'accounts/Enter Task.html'}, name='EnterTask'),
    url(r'^login$', login, {'template_name': 'accounts/login.html'},name='login'),
    url(r'^logout$', logout, {'template_name': 'accounts/logout.html'}),
    url(r'^Signuplogin$', login, {'template_name': 'accounts/Signuplogin.html'}),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^register/$', views.register, name='register'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^Changepassword_profile/$', views.changepassword_profile, name='changepassword_profile'),

    url(r'^reset-password/$', password_reset,{'template_name': 'accounts/reset-password.html',
                                              'post_reset_redirect':'accounts:password_reset_done','email_template_name':'accounts/reset_password_email.html'}, name='password_reset'),

    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'accounts/reset_password_done.html'},
        name='password_reset_done'),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm,{'template_name': 'accounts/reset_password_confirm.html','post_reset_redirect':'accounts:reset_password_complete'}, name='password_reset_confirm'),


    url(r'^reset-password/complete/$',password_reset_complete,{'template_name':'accounts/reset_password_complete.html'},name='reset_password_complete'),
    url(r'^add/task/$', views.add_blog),
    url(r'^add/userprofile/$', views.add_userprofile),
    url(r'^all/$', views.BlogAll),
    url(r'^get/(?P<blog_id>\d+)$', views.BlogGet),
    url(r'^alls/$', views.BlogAlls),
    url(r'^all_edit/$', views.BlogAlls),
    url(r'^edit/blog/(?P<id>\d+)$', views.BlogEdit),

]