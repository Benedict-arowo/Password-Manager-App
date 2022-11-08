from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Q
from authentication.encryption import encrpyt, decrypt, test

# Create your views here.


@login_required(login_url='auth')
def index(request):
    folders = Folder.objects.filter(
        user=request.user).all().order_by('-piority')
    items = None

    # Filtering
    if request.GET.get('type'):
        type = request.GET.get('type')

        if type == 'folder':
            uuid = request.GET.get('uuid')
            folder = Folder.objects.get(id=uuid)
            items = Item.objects.filter(folder=folder).order_by('-piority')
        elif type == 'starred':
            items = Item.objects.filter(
                user=request.user, star=True)
        elif type == 'piority':
            items = Item.objects.filter(user=request.user).order_by('-piority')

    # Searching
    elif request.GET.get('q'):
        q = request.GET.get('q')
        items = Item.objects.filter(
            Q(name__contains=q) | Q(username__contains=q) | Q(notes__contains=q) | Q(url__contains=q) & Q(user=request.user))
    else:
        items = Item.objects.filter(user=request.user).all()

    context = {
        'Folders': folders,
        'Items': items,
        'FolderForm': FolderForm,
        'ItemForm': ItemForm,
        'Type': (request.GET.get('type') or False)
    }

    return render(request, 'vault/index.html', context)


# Only accepts post request
@require_http_methods(["POST"])
@login_required(login_url='auth')
def createFolder(request):
    try:
        folder = Folder.objects.create(
            name=request.POST['name'],
            user=request.user,
            piority=(request.POST['piority'] or 0)
        )
    except:
        messages.error(
            request, 'You already have a folder named ' + request.POST['name'])

    return redirect('index')


@login_required(login_url='auth')
def deleteFolder(request):
    try:
        id = request.GET.get('id')
        folder = Folder.objects.get(id=id)
    except:
        messages.error(
            request, 'Folder does not exist!')

    if folder.user != request.user:
        messages.error(request, 'You do not own this folder!')
        return redirect('index')

    folder.delete()

    return redirect('index')


@login_required(login_url='auth')
def editFolder(request, id):
    try:
        folder = Folder.objects.get(id=id)
    except:
        messages.error(request, 'Folder does not exist!')
        return redirect('index')

    if folder.user != request.user:
        messages.error(request, 'You do not own this folder!')
        return redirect('index')

    form = FolderForm(instance=folder)

    if request.POST:
        folder.name = request.POST['name']
        folder.piority = (request.POST['piority'] or 0)
        folder.save()
        return redirect('index')

    context = {
        'form': form,
        # For displaying folders in aside
        'Folders': Folder.objects.filter(user=request.user).all().order_by('-piority')

    }
    return render(request, 'vault/editFolder.html', context)


@login_required(login_url='auth')
def item(request):
    try:
        id = request.GET.get('id')
        item = Item.objects.get(id=id)
    except:
        messages.error(request, 'Could not find item.')
        return redirect('index')

    if item.user != request.user:
        messages.error(request, 'You do not own this item!')
        return redirect('index')

    form = ItemForm(instance=item)
    try:
        password = decrypt(item.password)
        email = decrypt(item.email)
    except:
        messages.error(
            request, 'An error occured while trying to decrypt your data!')
        return redirect('index')

    if request.POST:
        form = ItemForm(request.POST, instance=item)
        if request.POST.get('star') == 'on':
            star = True
        else:
            star = False
        if form.is_valid():
            form = form.save(commit=False)
            form.password = encrpyt(form.password)
            form.email = encrpyt(form.email)
            form.star = star
            form.save()
            return redirect('index')
        else:
            messages.error(
                request, 'An error occured while trying to edit your item.')
    context = {
        'item': item,
        'form': form,
        'decryptedPassword': password,
        'decryptedEmail': email,
        # For displaying folders in aside
        'Folders': Folder.objects.filter(user=request.user).all().order_by('-piority')
    }
    return render(request, 'vault/item.html', context)


# Only accepts post requests
@require_http_methods(["POST"])
@login_required(login_url='auth')
def createItem(request):
    newItem = ItemForm(request.POST)
    password = encrpyt(request.POST['password'])
    email = encrpyt(request.POST['email'])
    if newItem.is_valid():
        item = newItem.save(commit=False)
        item.user = request.user
        item.email = email
        item.password = password
        item.piority = (request.POST['piority'] or 0)
        item.save()
    else:
        messages.error(request, 'Error creating your item. Please try again!')

    return redirect('index')


@login_required(login_url='auth')
def deleteItem(request):
    try:
        id = request.GET.get('id')
        item = Item.objects.get(id=id)
    except:
        messages.error(request, 'Could not find item.')
        return redirect('index')

    if not request.user == item.user:
        messages.error(request, 'You do not own this folder!')
        return redirect('index')

    item.delete()
    return redirect('index')
