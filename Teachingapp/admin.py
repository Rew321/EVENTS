from django.contrib import admin
from.models import  Event,User, Tag
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class EventAdmin(SummernoteModelAdmin):
    list_display = ('title', 'Venue', 'image', 'notes', 'starting_time', 'end_time', 'id', 'snumber','Origin','created_at')
    search_fields = ['title', 'Venue']
    list_filter = ['Venue', 'title', 'Origin']
    list_per_page = 8
    summary_fields = ['notes']
    
admin.site.register(Event, EventAdmin)    




admin.site.register(User)    
admin.site.register(Tag)    