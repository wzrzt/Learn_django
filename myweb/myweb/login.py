from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    username = request.POST.get('username', None)
    if username:
        request.session['username'] = username

    username = request.session.get('username', None)

    if username:
        return render_to_response('login.html', {'username': username})
    # 试图加一个名字为空的错误提示，没有成功
    # elif username == ' ':
    #     name_empty_error = '输入为空'
    #     return render_to_response('login.html', {'name_empty_error': name_empty_error})
    else:
        return render_to_response('login.html')


@csrf_exempt
def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponseRedirect("/login/")
