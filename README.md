# RainDataVisualizer
The program collects monthly rain data for a given number of Kenyan counties (county names are supplied via counties text file)using a form and creates a simple bar graph visualization of the data.The form only accepts data for counties that have not submited their rain data for that month. N/B the project is not fully complete. 

Requirements
Django==1.9.5
django-braces==1.8.1
django-chartit==0.1
django-highcharts==0.1.7
django-jquery==1.12.2
simplejson==3.8.2
six==1.10.0
 for chartit to work on this project navigate to (/site-packages/chartit/charts.py) and replace the line "from django.utils.datastructures import SortedDict" with "from collections import OrderedDict as SortedDictwith" 
