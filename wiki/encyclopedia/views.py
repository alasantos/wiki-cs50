from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
import random

from . import util

class NewArticleForm( forms.Form ):
    title = forms.CharField(label='Title ', max_length=80)
   # article = forms.CharField(label='Article text ')

def addTitle( request):
    context = {
        "NewArticle": NewArticleForm()
    }
    return(render, "encyclopedia/add.html", context )

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_title(request, TITLE):
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
    msg = None
    query = request.POST.get("q")
    article = util.search_in_titles ( query )
    if ( article ) == None:
        msg = f"Article {query.upper()} not avaliable"

    return render( request, "encyclopedia/index.html",
                            {
                                "article": article,
                                "title": query,
                                "message": msg
                            }
                )

def random_title (request):
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