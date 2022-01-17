from django.urls import path

from . import views

app_name = "wiki"

urlpatterns = [
      path( ""                     , views.index,          name="index"        )
    , path( "addTitle/"            , views.addTitle,       name="addTitle"     )
    , path( "search/"              , views.search_title,   name='search'       ) 
    , path( "<str:TITLE>/edit"     , views.edit_title,     name="edit_title"   )
    , path( "<str:TITLE>"          , views.get_title,      name="get_title"    )   
    , path( "random_title/"        , views.random_title,   name="random_title" )
]