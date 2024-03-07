from django.contrib import admin
from .models import db_Profile, db_Profile_detail

# Register your models here.


admin.site.register(db_Profile)
admin.site.register(db_Profile_detail)
