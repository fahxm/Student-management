from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from students.forms import StudentForm,GuardianForm
from students.models import Student,Classroom
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required




@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        else:
            print("Form errors:", form.errors)
    else:
        form = StudentForm()

    classrooms = Classroom.objects.all()
    return render(request, 'add_student.html', {'form': form, 'classrooms': classrooms})

@login_required
def  student_list(request):
    classroom_id=request.GET.get('classroom')
    students=Student.objects.all()
    
    if classroom_id:
        students=students.filter(classroom_id=classroom_id)

    classrooms=Classroom.objects.all()    
    return render(request,'student_list.html',{'students':students,
                                               'classrooms':classrooms,
                                               'selected_classroom':classroom_id
                                               })
@login_required
def student_update(request,pk):
    student=  get_object_or_404(Student,pk=pk)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
            form=StudentForm(instance=student)
    return render(request,'update_student.html',{'form':form})
@login_required
def student_delete(request,pk):
    student = get_object_or_404(Student,pk=pk)
    student.delete()
    return redirect('student_list')
def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('student_list')
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})
@login_required
def add_guardian(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    
    if request.method == 'POST':
        form = GuardianForm(request.POST)
        if form.is_valid():
            guardian = form.save(commit=False)
            guardian.student = student
            guardian.save()
            return redirect('student_list')
    else:
        form = GuardianForm()

    return render(request, 'add_guardian.html', {'form': form, 'student': student})

@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_detail.html', {'student': student})
