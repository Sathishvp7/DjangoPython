from django.contrib import admin
from accounts.models import UserProfile
from .models import Blogs
#from simple_history.admin import SimpleHistoryAdmin
#
# Register your models here.
admin.site.register(UserProfile)
admin.site.site_header = 'Administration'


admin.site.register(Blogs)
