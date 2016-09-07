from django.shortcuts import render
from django.http import HttpResponse

from django.template.loader import render_to_string

import data
import threading
import time

def puller():
    while True:
        print "polling"
        data.get_data()
        time.sleep(1)

t = threading.Thread(target=puller)
t.setDaemon(True)
t.start()

def table(request):
    rendered = render_to_string('table.html', {'prices': reversed(data.prices)})
    return HttpResponse(rendered)
