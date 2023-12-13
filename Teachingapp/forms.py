from django import forms
from Teachingapp.models import Event
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget




class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title','image','Venue', 'notes','starting_time', 'end_time', 'Origin']
        
       
  