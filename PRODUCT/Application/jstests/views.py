from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.cache import never_cache
from logger import log
from django.conf import settings
from django.utils.translation import ugettext as _
import os

try:
    from django.contrib import messages
    _USE_MESSAGES = True
except ImportError: 
    _USE_MESSAGES = False

@never_cache
def index(request):
    tests = []
    vars = {}
    if 'path' in request.REQUEST:
        path = request.REQUEST['path']
    else:
        if _USE_MESSAGES:
            messages.add_message(request, messages.INFO, _('No tests loaded. Please, check path parameter'))
        else:
            vars = {'error': _('No tests loaded. Please, check path parameter')}
        return render_to_response('static/tests/testLoader.html', vars)
        
    for tpl_dir in settings.TEMPLATE_DIRS:
        abs_path_tpl_dir = os.path.abspath(tpl_dir)
        tests_dir = os.path.join(abs_path_tpl_dir, 'static/tests')
        if not os.path.exists(tests_dir):
            continue
        test_cases_dir = os.path.join(tests_dir, path)
        if os.path.exists(test_cases_dir):
            if os.path.isdir(test_cases_dir):
                for root, dirs, files in os.walk(test_cases_dir):
                    for in_file in files:
                        abs_file_path = os.path.join(root, in_file)
                        tests += [ 
                            abs_file_path.replace(abs_path_tpl_dir,'').replace(abs_path_tpl_dir,'').replace('\\','/'), 
                        ]
            else:
                tests += [ test_cases_dir.replace(abs_path_tpl_dir,'').replace(abs_path_tpl_dir,'').replace('\\','/'), ]
            break
        else:
            if _USE_MESSAGES:
                messages.add_message(request, messages.ERROR, _('No tests loaded. "%s" does not exists').__unicode__() % (test_cases_dir))
            else:
                vars =  {'error': _('No tests loaded. "%s" does not exists').__unicode__() % (test_cases_dir)}
            return render_to_response('static/tests/testLoader.html', vars)
    vars = { 'js': tests }
    return render_to_response('static/tests/testLoader.html', vars)
