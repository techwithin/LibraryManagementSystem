from django.shortcuts import render
from django.contrib.postgres.search import *
from django.contrib.postgres.operations import  *
from .models import *
from .forms import *
from .populatedata import *

# Create your views here.
def BookSearch(request): 
    form = SearchField()
    # start = Title.objects.filter(acc_no = 0)
    if request.method == "POST":
        form = SearchField(request.POST)
        if form.is_valid():
            # populating()
            # print("Populated")
            query = form.cleaned_data.get('searchinput')
            start = Title()

            vector = SearchVector('title', weight = 'B', config = 'english') + SearchVector('author', weight = 'A', config = 'english')
            mango = Title.objects.annotate(search = vector).filter(search = SearchQuery(query))
            
            if mango:
                
                c = mango.count()
                return render(request, "BookSearch.html", {'form': form, 'bookdata' : mango, 'count' : c, 'result' : "searchvector"})
                

            else:
                apple = Title.objects.annotate(similarity=TrigramSimilarity('author', query) + TrigramSimilarity('title', query),).filter(similarity__gt=0.12) .order_by('-similarity')
                c = apple.count()
                return render(request, "BookSearch.html", {'form': form, 'bookdata' : apple, 'count' : c, 'result' : "trigram"})

                # elif apple.count() < 3:
                #     apple = Title.objects.annotate(similarity=TrigramSimilarity('author', query) + TrigramSimilarity('title', query),).filter(similarity__gt=0.1) .order_by('-similarity')
                    
                #     return render(request, "BookSearch.html", {'form': form, 'bookdata' : apple})

                # elif apple.count() < 3:
                #     apple = Title.objects.annotate(similarity=TrigramSimilarity('author', query) + TrigramSimilarity('title', query),).filter(similarity__gt=0.1) .order_by('-similarity')
                    
                #     return render(request, "BookSearch.html", {'form': form, 'bookdata' : apple})

                # else:
                #    apple = Title.objects.annotate(similarity=TrigramSimilarity('author', query) + TrigramSimilarity('title', query),).filter(similarity__gt=0.1) .order_by('-similarity')
                   
                #    return render(request, "BookSearch.html", {'form': form, 'bookdata' : apple})
            

    return render(request, "BookSearch.html", {'form': form})



