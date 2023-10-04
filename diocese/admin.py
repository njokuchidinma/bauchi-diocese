from django.contrib import admin
from .models import CustomUser, Diocese, Bishop, Project, Parish, Priest, Chapel, MassSchedule, YouthGroup, YouthEvent, Diocese_Event, Blog


admin.site.register(CustomUser)
admin.site.register(Diocese)
admin.site.register(Bishop)
admin.site.register(Project)
admin.site.register(Parish)
admin.site.register(Priest)
admin.site.register(Chapel)
admin.site.register(MassSchedule)
admin.site.register(YouthGroup)
admin.site.register(YouthEvent)
admin.site.register(Diocese_Event)
admin.site.register(Blog)