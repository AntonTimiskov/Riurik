from django.core.management.base import BaseCommand, CommandError
import os

class Command(BaseCommand):
	args = '<FORK ALIAS>'
	help = 'Run specified fork.'

	def handle(self, *args, **options):
			import settings
			#for fork in args:
		        fork = args[0]
			port = args[1]
			if fork in settings.FORKS:
				fork_path = settings.FORKS.get( fork )
				settings.CURRENT_FORK_PATH = fork_path

				settings.PRODUCT_TESTS_ROOT = settings.CURRENT_FORK_PATH
				settings.STATIC_TESTS_ROOT = os.path.join(settings.PRODUCT_TESTS_ROOT, settings.PRODUCT_TEST_CASES_ROOT)

				self.stdout.write('Current fork is %s (%s)\n' % (fork, fork_path))
				from django.core.management import call_command
				call_command('runserver', '0.0.0.0:'+str(port))
			else:
				self.stdout.write('UnKnown fork "%s"\n' % fork)
			#break
