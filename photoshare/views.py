from django.shortcuts import render, redirect
from photoshare.models import Category, Photo

# Create your views here.


def gallery(request):

    categoryByUrl = request.GET.get('category')
 
    if categoryByUrl == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name = categoryByUrl)

    categories = Category.objects.all()
 
    contextData = {
        'categories': categories,
        'photos': photos
    }
    return render(request, 'gallery.html', contextData)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'viewphoto.html', {'photo': photo})


def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        formData = request.POST
        image = request.FILES.get('image')
       # print(formData)

        if formData['category'] != 'none':
            # To check if the category exists or not
            category = Category.objects.get(id=formData['category'])
        elif formData['category_new'] != '':
            # to create a new category add it to the category table 
            category = Category.objects.create(name=formData['category_new'])
        else:
            category = None

        # add photo to the photo table.
        photo = Photo.objects.create(
            category=category,
            image=image,
            description=formData['description']
        )

        return redirect('gallery')
    return render(request, 'addphoto.html', {'categories': categories})
