
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage


def get_paginated_data(data,url,request):

    paginator=Paginator(data,10)
    page = request.GET.get('page', 1)

    try:
        result = paginator.page(page)

    except PageNotAnInteger:

        result = paginator.page(1)    

    except EmptyPage:

        result = paginator.page(paginator.num_pages)

    if result.has_next():
        next_link = "{0}&page={1}".format(url,result.next_page_number())
    else:
        next_link = None

    if result.has_previous():
        prev_link = "{0}&page={1}".format(url,result.previous_page_number())
    else:
        prev_link = None

        
    res = {
        'log_result': result.object_list,
        'total_records': paginator.count,
        'total_pages': paginator.num_pages,
        'current_page': result.number,
        "per_page":len(result.object_list),
        'next_link': next_link,
        'prev_link': prev_link}
    return res      