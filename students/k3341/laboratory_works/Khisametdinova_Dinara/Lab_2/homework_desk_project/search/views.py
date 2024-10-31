from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View
from homework_desk_app.models import Homework, Submission
from django.db import models 

class AdminSearchView(View):
    template_name = 'search_results.html'

    def get(self, request, *args, **kwargs):
        context = {}
        query = request.GET.get('q')
        
        if query:
            # Поиск по Submission (поиск студентов)
            submission_results = Submission.objects.filter(
                student__username__icontains=query
            )
            
            # Поиск по Homework (поиск по описанию и предмету)
            homework_results = Homework.objects.filter(
                models.Q(description__icontains=query) |
                models.Q(subject__name__icontains=query)
            )

            # Настройка пагинации
            submission_paginator = Paginator(submission_results, 10)
            homework_paginator = Paginator(homework_results, 10)
            submission_page_number = request.GET.get('submission_page')
            homework_page_number = request.GET.get('homework_page')

            # Получение страниц результатов
            try:
                context['submission_page_obj'] = submission_paginator.page(submission_page_number)
            except PageNotAnInteger:
                context['submission_page_obj'] = submission_paginator.page(1)
            except EmptyPage:
                context['submission_page_obj'] = submission_paginator.page(submission_paginator.num_pages)

            try:
                context['homework_page_obj'] = homework_paginator.page(homework_page_number)
            except PageNotAnInteger:
                context['homework_page_obj'] = homework_paginator.page(1)
            except EmptyPage:
                context['homework_page_obj'] = homework_paginator.page(homework_paginator.num_pages)

            # Сохранение последнего запроса для пагинации
            context['last_question'] = f'?q={query}'

        return render(request, self.template_name, context)