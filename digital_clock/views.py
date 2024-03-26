

# Create your views here.
from django.shortcuts import render
import datetime

def index(request):
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    return render(request, 'digital_clock/index.html', {'current_time': current_time})
