from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.db.models import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType


def ErrorResponse(code, message):
    data = {}
    data['status'] = 'ERROR'
    data['code'] = code
    data['message'] = message
    return JsonResponse(data)

def SuccessResponse(clicked_num):
    data = {}
    data['status'] = 'SUCCESS'
    data['clicked_num'] = clicked_num
    return JsonResponse(data)

def click_change(request):
    user = request.user
    content_type = request.GET.get('content_type')
    object_id = request.GET.get('object_id')

    try:
        content_type = ContentType.objects.get(model=content_type)
        model_class = content_type.model_class()
        model_obj = model_class.objects.get(pk=object_id)
    except ObjectDoesNotExist:
        return ErrorResponse(401, 'object not exist')

    click_record, created = ClickRecord.objects.get_or_create(content_type=content_type, object_id=object_id, user=user)
    if created:
        click_count, created = ClickCount.objects.get_or_create(content_type=content_type, object_id=object_id)
        click_count.click_num += 1
        click_count.save()
        return SuccessResponse(click_count.click_num)
    else:
        click_count = ClickCount.objects.get(content_type=content_type, object_id=object_id)
        return SuccessResponse(click_count.click_num)
