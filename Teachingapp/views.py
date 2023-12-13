from django.contrib import messages
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404

from Teachingapp.forms import EventForm
from . models import Event, Tag,User
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Q
# Create your views here.
#home page

def landing_page(request):
    events_list = Event.objects.all()
    tags = Tag.objects.all()
    display = "none"
    context={"events":events_list, "tags":tags, "display":display}
    def get_ip(request):
        adress= request.META.get('HTTP_X_FORWARDED_FOR')
        if adress:
            ip = adress.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    ip = get_ip(request)
    u = User(user=ip)
    print(ip)
    results = User.objects.filter(Q(user__icontains = ip))
    if len(results) ==1:
        print("user exists")
    elif len(results)>1:
        print("user exizta")    
    else:
        u.save()
        print("user is unique")  
    count = User.objects.all().count()
    print("total user is", count)          

    return render(request, 'landing_page.html', context)



#Add event
def add_event(request):
    if request.method == "POST":
        if request.POST.get('title') \
            and request.POST.get('Venue') \
            and request.POST.get('image') \
            and request.POST.get('notes') \
            and request.POST.get('starting_time') \
            and request.POST.get('end_time') \
            or request.POST.get('Origin'):
            event = Event()
            event.title = request.POST.get('title')
            event.Venue = request.POST.get('Venue')
            event.image = request.POST.get('image')
            event.notes = request.POST.get('notes')
            event.starting_time = request.POST.get('starting_time')
            event.end_time = request.POST.get('end_time')
            event.Origin = request.POST.get('Origin')
            event.save()
            messages.success(request, 'Event added successfully')
            return HttpResponseRedirect('/')
    else:
        return render(request, 'add.html')
    
#Function to view event data individually
def event(request, event_id):
    event = Event.objects.get(id=event_id)
    if event != None:
        return render(request, 'edit.html',  {"event":event})
    else:
        return render(request, '404.html')    

#Function to edit event
def edit_event(request):
    if request.method == "POST":
        event = Event.objects.get(id = request.POST.get('id'))
        if event != None:
            event.title = request.POST.get('title')
            event.Venue = request.POST.get('Venue')
            event.image = request.POST.get('image')
            event.notes = request.POST.get('notes')
            event.starting_time = request.POST.get('starting_time')
            event.end_time = request.POST.get('end_time')
            event.Origin = request.POST.get('Origin')
            event.save()
            messages.success(request, 'Event updated successfully')
            return HttpResponseRedirect('/')
    else:
        return render(request, '404.html')


#Function to delete event
def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if event != None:
        event.delete()
        messages.success(request, 'Event deleted successfully')
        return HttpResponseRedirect('/')
    else:
        return render(request, '404.html')
    
  
def Event_details(request, event_id):
    event = Event.objects.get(id=event_id) 
    if event != None:
        return render(request, 'detail.html',  {"event":event})
    else:
        return render(request, '404.html')
    
def event_listajax(request):
    events = Event.objects.filter(status=0).values_list('title', flat=True)
    eventlist = list(events)
    
    return JsonResponse(eventlist, safe=False)

def searchevents(request):
    if request.method =='POST':
        searchterm = request.POST.get('eventsearch')
        if searchterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            event = Event.objects.filter(title__contains=searchterm).first()
            if event:
                return render(request,"detail.html", {"event":event})
            else:
                messages.info(request, "No search term found")
                request.redirect(request.MEATA.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))    