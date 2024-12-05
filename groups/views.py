from django.shortcuts import render, redirect, get_object_or_404

from .models import Post


def home(request):
    return render(request, 'index.html')


def person_list(request):
    groups = Post.objects.all()
    ctx = {'groups': groups}
    return render(request, 'groups/list.html', ctx)


def person_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if (first_name and last_name
                ):
            Post.objects.create(
                first_name=first_name,
                last_name=last_name,

            )
            return redirect('groups:list')
    return render(request, 'groups/form.html')

def person_detail(request, pk):
    groups = get_object_or_404(Post, pk=pk)
    ctx = {'groups': groups }
    return render(request, 'groups/detail.html', ctx)

def person_delete(request, pk):
    person = get_object_or_404(Post, pk=pk)
    person.delete()
    return redirect('groups:list')