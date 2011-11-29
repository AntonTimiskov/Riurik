import os, sys

info_portal_tests = 'info-portal-tests'
info_portal_path = os.path.join('sharepoint information portal', 'application', 'tests', 'cases')
riurik_tests_path = os.path.join('tests', 'riurik', 'cases')
VIRTUAL_PATHS = {
  'info-portal-tests': os.path.join('c:\\hunter', riurik_tests_path),
  'warrior': os.path.join('c:\\warrior', info_portal_path),
  'wizard': os.path.join('c:\\wizard', info_portal_path),
  'blade': os.path.join('c:\\blade', info_portal_path),
  'ford': os.path.join('c:\\ford', info_portal_path),
  'olegshevnin': os.path.join('c:\\olegshevnin', info_portal_path),
}

sys.path.append('C:\\hunter\\tests')
tests_loader_path = 'riurik.urls'
