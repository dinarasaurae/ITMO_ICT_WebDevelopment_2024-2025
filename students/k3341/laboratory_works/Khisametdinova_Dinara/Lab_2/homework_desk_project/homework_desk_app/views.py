from django.shortcuts import render
from .forms import UserRegistrationForm, SubmissionForm, SubjectForm, CustomAuthenticationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import *
from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView

class RegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = CustomAuthenticationForm

    def get_success_url(self):
        return reverse_lazy('dashboard')

class UserDashboardView(LoginRequiredMixin, ListView):
    template_name = 'dashboard.html'
    context_object_name = 'submissions'
    
    def get_queryset(self): 
        user = self.request.user

        # Если студент, показываем только его домашние задания
        if user.role == 'student':
            return Submission.objects.filter(student=user).select_related('homework')
        
        # Если учитель или админ, показываем все домашние задания
        return Submission.objects.filter(homework__subject__teachers=user).select_related('homework', 'student')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['is_student'] = user.role == 'student'
        context['subjects'] = Subject.objects.filter(teachers=user) if user.role == 'teacher' else Subject.objects.all()
        return context
    
class SubmissionCreateView(LoginRequiredMixin, CreateView):
    model = Submission
    form_class = SubmissionForm
    template_name = 'submission.html'

    def form_valid(self, form):
        homework_id = self.kwargs['homework_id']
        homework = get_object_or_404(Homework, pk=homework_id)
        form.instance.student = self.request.user
        form.instance.homework = homework
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dashboard')

class HomeworkListView(ListView):
    model = Homework
    template_name = 'homework_list.html'
    context_object_name = 'homeworks'

class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subject_form.html'
    success_url = '/homeworks/'

class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subject_form.html'
    success_url = '/homeworks/'

class SubmissionCreateView(CreateView):
    model = Submission
    form_class = SubmissionForm
    template_name = 'submission.html'

    def form_valid(self, form):
        homework_id = self.kwargs['homework_id']
        homework = get_object_or_404(Homework, pk=homework_id)
        form.instance.student = self.request.user
        form.instance.homework = homework
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('homeworks')
    
def is_admin_or_teacher(user):
    return user.is_superuser or user.role == 'teacher'

@method_decorator(user_passes_test(is_admin_or_teacher), name='dispatch')
class AdminGradeTableView(ListView):
    model = Submission
    template_name = 'grade_table.html'
    context_object_name = 'submissions'
    paginate_by = 10

    def get_queryset(self):
        queryset = Submission.objects.select_related('student', 'homework')
        class_id = self.request.GET.get('class_id')

        if class_id:
            queryset = queryset.filter(student__student_class_id=class_id)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = Class.objects.all()
        context['is_admin'] = True  # Администратор видит больше данных
        return context

class StudentGradeTableView(LoginRequiredMixin, ListView):
    model = Submission
    template_name = 'grade_table.html'
    context_object_name = 'submissions'
    paginate_by = 10

    def get_queryset(self):
        # Фильтруем только по записям текущего пользователя
        return Submission.objects.filter(student=self.request.user).select_related('homework', 'student')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_admin'] = False  # Студенты не видят фильтра по классам
        return context