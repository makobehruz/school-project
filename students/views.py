from django.shortcuts import render, redirect, get_object_or_404

from .models import Post


def home(request):
    return render(request, 'index.html')


def person_list(request):
    students = Post.objects.all()
    ctx = {'students': students}
    return render(request, 'students/list.html', ctx)


def person_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        if (first_name and last_name and
                age and email):
            Post.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                email=email
            )
            return redirect('students:list')
    return render(request, 'students/form.html')

def person_detail(request, pk):
    students = get_object_or_404(Post, pk=pk)
    ctx = {'students': students }
    return render(request, 'students/detail.html', ctx)

def person_delete(request, pk):
    person = get_object_or_404(Post, pk=pk)
    person.delete()
    return redirect('students:list')