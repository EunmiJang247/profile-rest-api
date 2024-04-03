from django.contrib import admin

from profiles_api import models


admin.site.register(models.UserProfile) # UsrProfile모델에 접근가능하게함.
