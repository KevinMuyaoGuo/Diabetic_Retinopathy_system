from django.contrib import admin

from .models import Case, Patient, Diagnosis, Photo

# 修改网页title和站点header
admin.site.site_title = "糖尿病视网膜病变识别系统"
admin.site.site_header = "糖尿病视网膜病变识别系统"



class DiagnosisInline(admin.StackedInline):
    model = Diagnosis
    extra = 0
    list_display = ('id', 'photo_id', 'photo_name', 'image_data', 'result')
    # readonly_fields = ('id', 'photo_id', 'photo_name', 'result', 'image_data')


class CaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_name', 'case_name', 'create_time')
    search_fields = ('id', 'patient_name')
    list_display_links = ['case_name']
    date_hierarchy = 'create_time'
    # readonly_fields = ('id', 'patient_name', 'case_name', 'create_time')
    inlines = [DiagnosisInline, ]


class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'sex', 'age')
    search_fields = ('id', 'name')
    list_display_links = ['name']


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo_name', 'image_data', 'photo_diagnosis')
    list_display_links = ['photo_name']


# class PhotoInline(admin.TabularInline):
#     model = Photo


admin.site.register(Case, CaseAdmin)

admin.site.register(Patient, PatientAdmin)

admin.site.register(Photo, PhotoAdmin)
