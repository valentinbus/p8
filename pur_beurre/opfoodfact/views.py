from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from .api_op.api_op import OpenFoodFacts
from .forms import NameForm


op = OpenFoodFacts()

def search(request):
    """
    search process
    """
    if request.method == 'POST':
        form = NameForm(request.POST)


        if form.is_valid():

            query = form.data['query']
            result = op.search(query)
            return JsonResponse(result, safe=False)

    else:
        form = NameForm()

    return render(request, "openfoodfacts_search.html", {'form': form})
    
def replace(request):
    """
    replace process
    """
    category = request.GET['category']
    nutriscore = request.GET['nutriscore']

    data = op.purpose_replace(category, nutriscore)

    return JsonResponse(data, safe=False)