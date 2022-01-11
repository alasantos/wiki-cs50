from django import forms
from django.http.response import HttpResponseRedirect
from django.core.files.storage import default_storage

from django.shortcuts import render
from django.urls import reverse
import random

from . import util


class NewArticleForm( forms.Form ):
    title = forms.CharField(label='Title ', required="true")
    description = forms.CharField( label='Description ', required="true", widget=forms.Textarea( attrs= { 'rows': 5, 'cols': 20 } ) )

def addTitle( request, Title = None ):
    ''' addTitle view '''
    context = {
        "NewArticle": NewArticleForm(),
        "Message": None
    }

    if request.method == "POST":
        form = NewArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data['description']
            util.save_entry( title, description )
            return HttpResponseRedirect( reverse( "wiki:index" ) )
    elif request.method == "GET":
        print( Title)
        print("to aqui" )

    return render( request, "encyclopedia/addTitle.html", context ) 
    #return HttpResponseRedirect( reverse( "encyclopedia:addTitle", args=context))

def edit_title(request, TITLE = None ):
 
    if TITLE != None and request.method == "GET":
        form = NewArticleForm()
        article = util.get_entry( TITLE )
        #form.description = article
        form.initial["description"] = article
        form.initial["Title"] = TITLE
        #form.title= TITLE
        
    return render( request, "encyclopedia/editTitle.html", 
                    {
                        "NewArticle": form,
                        "Message": "hhwhwhwhwhwhw"
                    }  
                 )


def index(request):
    ''' Home view '''
    return render(request, "encyclopedia/index.html", {
                    "entries": util.list_entries()
    })

def get_title(request, TITLE):
    ''' Retrieves a requested title '''
    result = message = None
    result = util.get_entry( TITLE )
    if result == None:
        message = f"Article not found for {TITLE}"

    return render( request, "encyclopedia/title.html", 
                    {
                        "article": result, 
                        "title": TITLE,
                        "message": message
                    } 
                  )
def search_title( request ):
    ''' Search solution entry point '''
    msg = None
    query = request.POST.get("q")
    articles = util.search_in_titles( query )
    qtty = len( articles )
    if( len(articles) == 0 ):
        msg = f'Search for "{query.upper()}" found no results'

    if( len( articles ) == 1):
        return HttpResponseRedirect( reverse( "wiki:get_title", args=articles))
    else:
        msg = f'Search for "{query.upper()}" found {qtty} results'
        return render( request, "encyclopedia/index.html",
                            {
                                "entries": articles,
                                "message": msg
                            }
                )

def random_title (request):
    ''' Random article entry point '''
    article = message = None
    selected_title = random.choice( util.list_entries() )
    if selected_title == None:
        message = f"Surprise article not available {selected_title}"

    article = util.get_entry( selected_title )
    
    return render( request, "encyclopedia/title.html", 
                    {
                        "article": article, 
                        "title": selected_title,
                        "message": message
                    } 
                  )