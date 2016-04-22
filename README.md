# RainDataVisualizer
The program collects monthly rain data for a given number of Kenyan counties (county names are supplied via counties text file)using a form and creates a simple bar graph visualization of the data.The form only accepts data for counties that have not submited their rain data for that month. N/B the project is not fully complete. 

#NOTE
Chartit lib has some issues. Here is how to fix them
 - ~/{VIRTUAL ENV}/{ENV NAME}/local/lib/python.{VERSION}/site-packages/chartit/charts.py) and replace the line `from django.utils.datastructures import SortedDict` with `from collections import OrderedDict as SortedDict`
 - ~/{VIRTUAL ENV}/{ENV NAME}/local/lib/python.{VERSION}/site-packages/chartit/chartdata.py) and replace the line `from django.utils.datastructures import SortedDict` with `from collections import OrderedDict as SortedDict`
 - ~/{VIRTUAL ENV}/{ENV NAME}/local/lib/python.{VERSION}/site-packages/chartit/templatetags/chartit.py) and replace the line `from django.utils import simplejson` with `import simplejson`

This is possibly due to lack of support for django 1.9
