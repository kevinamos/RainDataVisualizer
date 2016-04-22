from django.shortcuts import render_to_response
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render

from chartit import PivotDataPool, PivotChart
from chartit import DataPool, Chart
from chartit import DataPool, Chart

from highcharts.views import HighChartsBarView

from .forms import RainfallDataForm,ViewCountiesForm, ViewmMonthsForm
from .models import RainDataStore


class Home(FormView):
	template_name='index.html'
        form_class = RainfallDataForm
        success_url = '/success/'

	def post(self, request, *args, **kwargs):		
    		form_class = self.get_form_class()
    		form = self.get_form(form_class)
    		if form.is_valid():
			form.save()			
        		return self.form_valid(form)
    		else:
        		return self.form_invalid(form)

class Choose_county_View(FormView):
	template_name='view_rain_data.html'
	form_class = ViewCountiesForm
	
	def post(self, request, *args, **kwargs):
		
    		form_class = self.get_form_class()
    		form = self.get_form(form_class)
    		if form.is_valid():

			form.save()
			
        		return self.form_valid(form)
    		else:
        		return self.form_invalid(form)

class Choose_Rainfall_Month_View(Choose_county_View):
	template_name='view_county_rain_for_month.html'
	form_class = ViewmMonthsForm

class success(TemplateView):
	template_name = "index.html"
	succesful_entry='Data succefully saved'
	
	def get(self, request, *args, **kwargs):
        	context = locals()
        	context['succesful_entry'] = self.succesful_entry        	
        	return render_to_response(self.template_name, context, context_instance=RequestContext(request))

def weather_chart_view(request):    
    county_name='Nairobi'
    if request.method == 'POST': # If the form has been submitted...
        	form = ViewCountiesForm(request.POST) # A form bound to the POST data
    if form.is_valid(): # All validation rules pass

            # Process the data in form.cleaned_data

        county_name=form.cleaned_data['County']

    heading_text='{} County Monthly Rainfall graph'.format(county_name)
    #Step 1: Create a DataPool with the data we want to retrieve.
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': RainDataStore.objects.filter(County=county_name)},
              'terms': [
                'Month',
                'Rainfall_Amount',
                ]}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'Month': [
                    'Rainfall_Amount',

                    ]

                  }}],
            chart_options =
              {'title': {
                   'text':heading_text },
               'xAxis': {
                    'title': {
                       'text': 'Month of year'}}})

    #Step 3: Send the chart object to the template.
    return render_to_response('Visualized_rain_data.html',{'weatherchart': cht})


def  Rainfall_per_month_chart_view(request):
    
    month_name='January'
    if request.method == 'POST': # If the form has been submitted...
        	form = ViewmMonthsForm(request.POST) # A form bound to the POST data
    if form.is_valid(): # All validation rules pass

            # Process the data in form.cleaned_data

        month_name=form.cleaned_data['Month']

    heading_text='County  Rainfall During the month of {} '.format(month_name)
    #Step 1: Create a DataPool with the data we want to retrieve.
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': RainDataStore.objects.filter(Month=month_name)},
              'terms': [
                'County',
                'Rainfall_Amount',
                ]}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'County': [
                    'Rainfall_Amount',

                    ]

                  }}],
            chart_options =
              {'title': {
                   'text':heading_text },
               'xAxis': {
                    'title': {
                       'text': 'Month of year'}}})

    #Step 3: Send the chart object to the template.
    return render_to_response('Visualized_rain_data.html',{'weatherchart': cht})







