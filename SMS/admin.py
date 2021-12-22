from django.contrib import admin

# Register your models here.


from .models import UserInfo, Owns, Balance, Ticket


admin.site.register(UserInfo)
admin.site.register(Owns)
admin.site.register(Balance)
admin.site.register(Ticket)
