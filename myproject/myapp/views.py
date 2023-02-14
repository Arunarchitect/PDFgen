import os
import pdfkit
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

def home(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name')
        age = int(request.POST.get('age'))
        marks = int(request.POST.get('marks'))

        # Calculate product of marks and age
        product = age * marks

        # Render the HTML template
        context = {'name': name, 'age': age, 'marks': marks, 'product': product}
        html = render(request, 'report.html', context).content.decode('utf-8')

        # Write the HTML to a file
        with open('report.html', 'w') as f:
            f.write(html)

        # Redirect to the PDF preview page
        return redirect(reverse('preview'))

    return render(request, 'home.html')

def preview(request):
    # Generate the PDF report
    pdfkit.from_file('report.html', 'report.pdf')

    # Read the PDF file into a byte array
    with open('report.pdf', 'rb') as f:
        pdf_data = f.read()

    # Delete the PDF file from disk
    os.remove('report.pdf')

    # Return the PDF data as a response
    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'
    return response
