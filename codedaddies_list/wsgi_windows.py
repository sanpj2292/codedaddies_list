activate_this = 'C:/Users/sanpj/.virtualenvs/codedaddies_list-XfvD6hkC/Scripts/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))

import os
import sys
import site

site.addsitedir('C:/Users/sanpj/.virtualenvs/codedaddies_list-XfvD6hkC/Lib/site-packages')

sys.path.append('F:/django-sites/codedaddies_list')
sys.path.append('F:/django-sites/codedaddies_list/codedaddies_list')

os.environ['DJANGO_SETTINGS_MODULE'] = 'codedaddies_list.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codedaddies_list.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
