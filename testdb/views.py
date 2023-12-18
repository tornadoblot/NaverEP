from django.shortcuts import render
from .models import Product
import mimetypes
import os

from django.conf import settings
from django.http.response import HttpResponse 
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.

def post_view(request):
    results = Product.objects.all()

    return render(request, 'index.html', {"results": results})

def update_list_file(request):
    results = Product.objects.all()

    base_dir = settings.MEDIA_ROOT
    file_name = os.path.join(base_dir, "list.txt")

    f = open(file_name, 'w')

    f.write("id\ttitle\tprice_pc\tlink\timage_link\tcategory_name1\tshipping\n")

    for result in results:
        f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(result.id, result.title, result.price, result.link, result.img_link, result.category_name1, result.shipping))
        f.write('\n')

    f.close()

    return HttpResponseRedirect(reverse('post'))