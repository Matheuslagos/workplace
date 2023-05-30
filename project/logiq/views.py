from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.


def index(request):
    responsaveis = Responsavel_Tecnico.objects.all()
    produtores = ProdutorRural.objects.all()
    propriedades = Propriedade.objects.all()
    diagnosticos = Diagnostico.objects.all()
    return render(request, 'logiq/index.html', {'responsaveis': responsaveis, 'produtores': produtores, 'diagnosticos': diagnosticos, 'propriedades': propriedades})


def documento(request):
    responsaveis = Responsavel_Tecnico.objects.all()
    produtores = ProdutorRural.objects.all()
    propriedades = Propriedade.objects.all()
    diagnosticos = Diagnostico.objects.all()
    return render(request, 'logiq/documento.html', {'responsaveis': responsaveis, 'produtores': produtores, 'diagnosticos': diagnosticos, 'propriedades': propriedades})


def documentoCompleto(request):
    responsaveis = Responsavel_Tecnico.objects.all()
    produtores = ProdutorRural.objects.all()
    propriedades = Propriedade.objects.all()
    diagnosticos = Diagnostico.objects.all()
    return render(request, 'logiq/documentoCompleto.html', {'responsaveis': responsaveis, 'produtores': produtores, 'diagnosticos': diagnosticos, 'propriedades': propriedades})


def render_pdf_view(request):
    responsaveis = Responsavel_Tecnico.objects.all()
    produtores = ProdutorRural.objects.all()
    propriedades = Propriedade.objects.all()
    diagnosticos = Diagnostico.objects.all()

    template_path = 'logiq/documentoCompletoPDF.html'
    context = {'responsaveis': responsaveis, 'produtores': produtores,
               'diagnosticos': diagnosticos, 'propriedades': propriedades}

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename="AgroSYS.pdf"'

    # find the template and render it.

    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
