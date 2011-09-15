from django.core.management.base import BaseCommand, CommandError
import os

class Command(BaseCommand):
	args = '<FORK ALIAS>'
	help = 'Run specified fork.'

	def handle(self, *args, **options):
			import settings
			fork = args[0]
			port = args[1]
			if fork in settings.FORKS:
				settings.CURRENT_FORK_PATH = settings.FORKS.get( fork )
				settings.VIRTUAL_PATHS[settings.info_portal_tests] = os.path.join(settings.CURRENT_FORK_PATH, settings.info_portal_path)
				self.stdout.write('Current fork is %s (%s)\n' % (fork, settings.CURRENT_FORK_PATH))
				from django.core.management import call_command
				call_command('runserver', '0.0.0.0:'+str(port))
			else:
				self.stdout.write('UnKnown fork "%s"\n' % fork)
