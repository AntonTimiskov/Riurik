import os
from django import template
import settings

register = template.Library()

@register.filter
def img_by_fstype( path, fsobject ):
	if path == '/':
		fullpath = os.path.join(settings.STATIC_TESTS_ROOT, fsobject)
	else:
		fullpath = os.path.join(settings.STATIC_TESTS_ROOT, path, fsobject)
	
	if os.path.isdir(fullpath):
		return 'fsfolder.ico'
	return 'fstest.ico'