import os, shlex, subprocess
import dir_index_tools

COFFEESCRIPT_EXECUTABLE = r'C:\\CoffeeScript\\coffee.bat'
ext = '.coffee'

def coffee2js(path):
	#file_name = path.rsplit('/', 1)[1]
	file_name = os.path.basename(path)
	return (file_name, '.%s' % file_name.replace(ext, '.js'))

def compile(source, path, full_path):

	args = shlex.split("%s -c -b -s -p" % COFFEESCRIPT_EXECUTABLE)
	if not source:
		source = dir_index_tools.gettest(full_path)
	else:
		source = source.encode('utf-8')

	p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	out, errors = p.communicate(source)

	coffee_name, js_name = coffee2js(full_path)
	full_path = full_path.replace(coffee_name, js_name)
	if os.path.exists(full_path):
		os.remove(full_path)

	if out:
		dir_index_tools.savetest(out.decode("utf-8"), full_path)

	#return errors
	return path.replace(coffee_name, js_name) if path else None
