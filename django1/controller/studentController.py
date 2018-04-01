import json
import logging
import traceback
from django.http import HttpResponse
from service import studentService
from dto.commonResult import CommonResult
from utils import jsonp
from entity.student import Student

logger = logging.getLogger(__name__)

def get(request):
    param_dict = request.GET
    if request.method == "POST":
        param_dict = request.POST
    commonResult = CommonResult()
    idStr = param_dict.get('id')
    callback = request.GET.get('callback')
    if (idStr is None) or (not idStr.isdigit()) or (int(idStr) < 1):
        commonResult.code = 430
        commonResult.message = "id参数错误"
    else:
        id = int(idStr)
        student = studentService.get(id)
        commonResult.data = student

    return HttpResponse(jsonp.doJsonP(commonResult, callback), content_type='application/json')


def getall(request):
    commonResult = CommonResult()
    callback = request.GET.get('callback')
    students = studentService.getAll()
    commonResult.data = students
    return HttpResponse(jsonp.doJsonP(commonResult, callback), content_type='application/json')


def getallpage(request):
    param_dict = request.GET
    if request.method == "POST":
        param_dict = request.POST
    commonResult = CommonResult()
    callback = request.GET.get('callback')
    pageNo = param_dict.get("page")
    pageSize = param_dict.get("size")

    if (pageNo is None) or (not pageNo.isdigit()) or (int(pageNo) < 0):
        pageNo = 0
    if (pageSize is None) or (not pageSize.isdigit()) or (int(pageSize) < 1):
        pageSize = 10

    pageResult = studentService.getAllPage(int(pageNo), int(pageSize))
    commonResult.data = pageResult
    return HttpResponse(jsonp.doJsonP(commonResult, callback), content_type='application/json')


def add(request):
    param_dict = request.GET
    if request.method == "POST":
        param_dict = request.POST
    commonResult = CommonResult()
    callback = request.GET.get('callback')
    number = param_dict.get('number')
    if (number is None) or (number == ""):
        commonResult.code = 430
        commonResult.message = "参数错误"
    else:
        name = param_dict.get('name')
        if (name is None) or (name == ""):
            commonResult.code = 430
            commonResult.message = "参数错误"
        else:
            age = param_dict.get('age')
            if (age is None) or (age.isdigit() and int(age) >= 0):
                note = param_dict.get('note')
                student = Student(note=note, age=age, name=name, number=number)
                entity = studentService.add(student)
                commonResult.data = entity
            else:
                commonResult.code = 430
                commonResult.message = "参数错误"

    return HttpResponse(jsonp.doJsonP(commonResult, callback), content_type='application/json')


def update(request):
    param_dict = request.GET
    if request.method == "POST":
        param_dict = request.POST
    commonResult = CommonResult()
    idStr = param_dict.get('id')
    callback = request.GET.get('callback')
    if (idStr is None) or (not idStr.isdigit()) or (int(idStr) < 1):
        commonResult.code = 430
        commonResult.message = "id参数错误"
    else:
        updatedParams = param_dict.get('updatedParams')
        if (updatedParams is None) or (len(updatedParams) < 7):  # 表示更新信息的json字符串怎么也不会少于七个字
            commonResult.code = 430
            commonResult.message = "updatedParams参数错误"
        else:
            id = int(idStr)
            student = studentService.get(id)
            if student is None:
                commonResult.code = 500
                commonResult.message = "要更新的对象不存在"
            else:
                #  把updatedParams转化为dict
                try:
                    dict1 = json.loads(s=updatedParams)
                    if dict1 is None:
                        commonResult.code = 500
                        commonResult.message = "解析json失败"
                    else:
                        if dict1.__contains__('id'):
                            del dict1['id']
                        if dict1.__contains__('create_time'):
                            del dict1['create_time']
                        if dict1.__contains__('update_time'):
                            del dict1['update_time']
                        if not dict1:
                            commonResult.code = 430
                            commonResult.message = "缺少更新参数"
                        else:
                            #  更新student
                            for k in dict1:
                                student[k] = dict1[k]
                            entity = studentService.update(id, dict1, student)
                            commonResult.data = entity
                except Exception as e:
                    logger.error(traceback.format_exc())
                    commonResult.code = 500
                    commonResult.message = "解析json失败"

    return HttpResponse(jsonp.doJsonP(commonResult, callback), content_type='application/json')


def delete(request):
    param_dict = request.GET
    if request.method == "POST":
        param_dict = request.POST
    commonResult = CommonResult()
    idStr = param_dict.get('id')
    callback = request.GET.get('callback')
    if (idStr is None) or (not idStr.isdigit()) or (int(idStr) < 1):
        commonResult.code = 430
        commonResult.message = "id参数错误"
    else:
        id = int(idStr)
        studentService.delete(id)

    return HttpResponse(jsonp.doJsonP(commonResult, callback), content_type='application/json')
