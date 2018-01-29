from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(BasefileUpload, BasefileUploadAdmin)
admin.site.register(BaseDataFile, BaseDataFileAdmin)

admin.site.register(StandardfileUpload, StandardfileUploadAdmin)
admin.site.register(StandardDataFile, StandardDataFileAdmin)

admin.site.register(InnerSensorfileUpload, InnerSensorfileUploadAdmin)
admin.site.register(InnerSensorData, InnerSensorDataFileAdmin)

admin.site.register(OutSensorfileUpload, OutSensorfileUploadAdmin)
admin.site.register(OutSensorData, OutSensorDataFileAdmin)

admin.site.register(InvestigationfileUpload, InvestigationfileUploadAdmin)
admin.site.register(InvestigationData, InvestigationDataFileAdmin)