from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Pic_Actions
#from whynot.whynotMain.forms import Pic_ActionsForm

def home(request):
    img_src = []
    scores = []
    images = Pic_Actions.objects.all()
    
    for i in images:
        img_src.append((i.pic_before, i.pic_after))
        scores.append(i.score)
    
    return render_to_response("index.html", )

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = Pic_ActionsForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Pic_Actions(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the Pic_Actions list after POST
            return HttpResponseRedirect(reverse('whynotMain.views.list'))
    else:
        form = Pic_ActionsForm() # A empty, unbound form

    # Load Pic_Actionss for the list page
    pic_Actionss = Pic_Actions.objects.all()

    # Render list page with the Pic_Actionss and the form
    return render_to_response(
        'whynotMain/list.html',
        {'pic_Actionss': pic_Actionss, 'form': form},
        context_instance=RequestContext(request)
    )