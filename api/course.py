from flask import Blueprint, request
from utils.cookie import get_token
from internal.core.zjooc import ZJOOC
from decorator.auth import login_required
from dto.response import make_json_success, make_json_fail

courseApi = Blueprint('course', __name__)


@courseApi.get('/list')
@login_required
def get_course_list():
    try:
        zj = ZJOOC(cookie=get_token())
        publishStatus = request.args.get('publishStatus')
        return make_json_success(zj.getMyCourseList(publishStatus))
    except:
        return make_json_fail('fail')

@courseApi.get('/info/<course_id>')
@login_required
def get_course_info(course_id):
    # try:
        zj = ZJOOC(cookie=get_token())
        return make_json_success(zj.getCourseInfoBrief(course_id))
    # except:
        # return make_json_fail('fail')
    



@courseApi.get('/homework')
@login_required
def get_course_homework():
    try:
        zj = ZJOOC(cookie=get_token())
        courseId = request.args.get('courseId')
        return make_json_success(zj.getMyHomework(courseId))
    except:
        return make_json_fail('fail')
    


@courseApi.get('/exam')
@login_required
def get_course_exam():
    try:
        zj = ZJOOC(cookie=get_token())
        courseId = request.args.get('courseId')
        return make_json_success(zj.getMyExam(courseId))
    except:
        return make_json_fail('fail')


@courseApi.get('/test')
@login_required
def get_course_test():
    try:
        zj = ZJOOC(cookie=get_token())
        courseId = request.args.get('courseId')
        return make_json_success(zj.getMyTest(courseId))
    except:
        return make_json_fail('fail')



@courseApi.get('/chapters/<course_id>')
@login_required
def get_course_chapters(course_id):
    try:
        zj = ZJOOC(cookie=get_token())
        return make_json_success(zj.getCourseChapters(course_id))
    except:
        return make_json_fail('fail')

@courseApi.get('/resource/<course_id>')
@login_required
def get_course_resource(course_id):
    try:
        zj = ZJOOC(cookie=get_token())
        return make_json_success(zj.getCourseResource(course_id))
    except:
        return make_json_fail('fail')

@courseApi.get('/notices/<course_id>')
@login_required
def get_course_notices(course_id):
    try:
        zj = ZJOOC(cookie=get_token())
        return make_json_success(zj.getCourseNotices(course_id))
    except:
        return make_json_fail('fail')