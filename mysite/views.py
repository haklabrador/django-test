from django.shortcuts import render
from django.http import HttpResponse

def table(request):
    table_html = ""
    #for e in reversed(data.prices):
    for e in reversed([('2016-11-11', 'YHOO', 33.3)]):
        table_html += '''
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
        </tr>
        ''' % e
    tabela = '''
<html>
<head>
    <meta http-equiv="refresh" content="5">
</head>
<body>
    <TABLE  BORDER="5"; WIDTH=50%%>
    <TR>
        <TH COLSPAN="3">
            <H3><BR>Podatci s burza</H3>
        </TH>
    </TR>
        <TH>Date</TH>
        <TH>Symbol</TH>
        <TH>Price</TH>
    <TR>
    %s
    </TR>
</TABLE>
</body>
</html>
    '''
    return HttpResponse(tabela % table_html)
