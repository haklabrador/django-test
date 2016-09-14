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

def graph(request):
    import matplotlib
    #matplotlib.use('Cairo')
    import matplotlib.pyplot as plt
    import StringIO
    import urllib, base64

    import dateutil.parser
    l = []
    for e in data.prices[-20:]:
        l.append((dateutil.parser.parse(e[0]), float(e[2])))

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot([e[0] for e in l], [e[1] for e in l], '*:b')

    labels = ax.get_xticklabels()
    for l in labels:
        l.set_rotation(-45)

    imgdata = StringIO.StringIO()
    fig.savefig(imgdata, format='png')
    imgdata.seek(0)  # rewind the data

    uri = 'data:image/png;base64,' + urllib.quote(base64.b64encode(imgdata.buf))
    return HttpResponse('''
    <html>
    <head>
    <meta http-equiv="refresh" content="1">
    </head>
    <body>
    <img src = "%s"/>
    </body>
    </html>
    ''' % uri)
