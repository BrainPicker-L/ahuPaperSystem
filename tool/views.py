from django.shortcuts import render, get_object_or_404
from .models import *
from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Count
from .forms import SearchForm

def get_paper_list_common_data(request, paper_all_list):
    paginator = Paginator(paper_all_list, settings.EACH_PAGE_PAPERS_NUMBER)
    page_num = request.GET.get('page', 1)  # 获取url的页面参数（GET请求）
    page_of_papers = paginator.get_page(page_num)
    currentr_page_num = page_of_papers.number  # 获取当前页码
    # 获取当前页码前后各2页的页码范围
    page_range = list(range(max(currentr_page_num - 2, 1), currentr_page_num)) + \
                 list(range(currentr_page_num, min(currentr_page_num + 2, paginator.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)


    context = {}
    searlch_form = SearchForm()
    context['search_form'] = searlch_form
    context['papers'] = page_of_papers.object_list
    context['page_of_papers'] = page_of_papers
    context['page_range'] = page_range
    context['paper_types'] = PaperType.objects.annotate(paper_count=Count('paper'))
    return context


def paper_list(request):
    if request.method == 'POST':
        text = SearchForm(request.POST)
        if text.is_valid():
            text_to_search = text.cleaned_data['text']
            paper_all_list = Paper.objects.filter(chinese_title__icontains=text_to_search)
            if paper_all_list.count() == 0:
                paper_all_list = Paper.objects.filter(author__icontains=text_to_search)
                if paper_all_list.count() == 0:
                    paper_all_list = Paper.objects.filter(publish_year__icontains=text_to_search)
        context = get_paper_list_common_data(request, paper_all_list)
    else:
        paper_all_list = Paper.objects.get_queryset().order_by('id')
        context = get_paper_list_common_data(request, paper_all_list)
    return render(request, 'paper/paper_list.html', context)

def papers_with_type(request, paper_type_pk):
    paper_type = get_object_or_404(PaperType, pk=paper_type_pk)
    papers_all_list = Paper.objects.filter(paper_type=paper_type)
    context = get_paper_list_common_data(request, papers_all_list)
    context['paper_type'] = paper_type
    return render(request, 'paper/papers_with_type.html', context)