from django.shortcuts import render, redirect, get_object_or_404

from .models import Post


def home(request):
    return render(request, 'index.html')


def person_list(request):
    teachers = Post.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'teachers/list.html', ctx)


def person_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        if (first_name and last_name and
              email):
            Post.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            return redirect('teachers:list')
    return render(request, 'teachers/form.html')

def person_detail(request, pk):
    teachers = get_object_or_404(Post, pk=pk)
    ctx = {'teachers': teachers }
    return render(request, 'teachers/detail.html', ctx)

def person_delete(request, pk):
    person = get_object_or_404(Post, pk=pk)
    person.delete()
    return redirect('teachers:list')