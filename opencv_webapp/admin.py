from django.contrib import admin
from .models import ImageUploadModel
#
# Register your models here.

class Image_upload_Admin(admin.ModelAdmin):
    list_display = ('description', 'document', 'uploaded_at')
    list_filter = ['uploaded_at']
    search_fields = ['document']

admin.site.register(ImageUploadModel, Image_upload_Admin)
