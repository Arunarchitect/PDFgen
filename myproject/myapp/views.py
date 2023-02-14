from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
def home(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name')
        age = int(request.POST.get('age'))
        marks = int(request.POST.get('marks'))

        # Calculate product of marks and age
        product = age * marks

        # Generate the PDF report
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        # Create the PDF object, using the response object as its "file."
        p = canvas.Canvas(response)

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        p.drawString(100, 800, "Name: {}".format(name))
        p.drawString(100, 780, "Age: {}".format(age))
        p.drawString(100, 760, "Marks: {}".format(marks))
        p.drawString(100, 740, "Product: {}".format(product))

        # Close the PDF object cleanly, and we're done.
        p.showPage()
        p.save()

        return response

    return render(request, 'home.html')
