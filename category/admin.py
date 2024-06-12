from django.contrib import admin
from .models import District,Subdictrict,Gender,Living_Con,Level_of_Education,Career,Filed,AgeRange

# Register your models here.
admin.site.register(District)
admin.site.register(Subdictrict)
admin.site.register(Gender)
admin.site.register(Living_Con)
admin.site.register(Level_of_Education)
admin.site.register(Career)
admin.site.register(Filed)
admin.site.register(AgeRange)
