from django.shortcuts import render
from django.contrib.postgres.search import *
from django.contrib.postgres.operations import  *
from .models import *
from .forms import *
from .populatedata import *

# Create your views here.
def BookSearch(request): 
    form = SearchField()
    # start = Books.objects.filter(acc_no = 0)
    if request.method == "POST":
        form = SearchField(request.POST)
        if form.is_valid():
            # populating()
            query = form.cleaned_data.get('searchinput')
            start = Books()

            vector = SearchVector('book_name', weight = 'B', config = 'english') + SearchVector('authorname', weight = 'A', config = 'english')
            mango = Books.objects.annotate(search = vector).filter(search = SearchQuery(query))
            
            if mango:
                
                return render(request, "BookSearch.html", {'form': form, 'bookdata' : mango})


            else:
                apple = Books.objects.annotate(similarity=TrigramSimilarity('authorname', query) + TrigramSimilarity('book_name', query),).filter(similarity__gt=0.1) .order_by('-similarity')
                
                if apple.count() > 1:
                    
                    return render(request, "BookSearch.html", {'form': form, 'bookdata' : apple})

                elif apple.count() < 3:
                    apple = Books.objects.annotate(similarity=TrigramSimilarity('authorname', query) + TrigramSimilarity('book_name', query),).filter(similarity__gt=0.1) .order_by('-similarity')
                    
                    return render(request, "BookSearch.html", {'form': form, 'bookdata' : apple})

                elif apple.count() < 3:
                    apple = Books.objects.annotate(similarity=TrigramSimilarity('authorname', query) + TrigramSimilarity('book_name', query),).filter(similarity__gt=0.1) .order_by('-similarity')
                    
                    return render(request, "BookSearch.html", {'form': form, 'bookdata' : apple})

                else:
                   apple = Books.objects.annotate(similarity=TrigramSimilarity('authorname', query) + TrigramSimilarity('book_name', query),).filter(similarity__gt=0.1) .order_by('-similarity')
                   
                   return render(request, "BookSearch.html", {'form': form, 'bookdata' : apple})

                    
                # print("\nResults From Trigram\n")
                # 
            
            # print("Search Vector Results \n")
            # print(mango)
            # print("\n\nTrigram Results \n")
            # 

            

    return render(request, "BookSearch.html", {'form': form})



