from django.urls import path
from . import views
urlpatterns=[
        path('map/',views.map,name='map'),
        path('sightings/',views.sightings,name='sightings'),
        path('sightings/stats',views.stats),
        path('sightings/add',views.add),
]  
