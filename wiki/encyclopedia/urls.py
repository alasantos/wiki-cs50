from django.urls import path

from . import views

app_name = "wiki"

urlpatterns = [
      path( ""                  , views.index,          name="index"        )
    , path( "search/"           , views.search_title,   name='search'       ) 
    , path( "<str:TITLE>"       , views.get_title,      name="get_title"    )
    , path( "random_title/"     , views.random_title,   name="random_title" )
]
