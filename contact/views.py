from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseForm
from cart.models import Fruit




def course_detail_view(request, pk):
    course = Fruit.objects.get(pk=pk)
    return render(request, 'shop_detail.html', {'fruits': course})


def course_create_view(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course-list')
        else:
            return render(request, 'course_create.html', {'form': form, "message_error": "Qayerdadur xatolik mavjud!"})

    form = CourseForm()
    return render(request, 'course_create.html', {'form': form})

def course_update_view(request,pk):
    course=get_object_or_404(Fruit,pk=pk)
    if request.method == "POST":
        form=CourseForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return redirect('course-detail',pk=course.pk)
        else:
            form=CourseForm(instance=course)
    course = Fruit.objects.get(pk=pk)
    return render(request,'shop.html',{"course":course})
def course_delete_view(request, id):
    course = Fruit.objects.get(id=id)
    course.delete()
    return redirect('course-list')
    return render(request, 'shop.html', {'form': form})
