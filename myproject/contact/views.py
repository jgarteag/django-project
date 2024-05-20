from django.shortcuts import render
from django.views import View

# Create your views here.
class IndexView(View):
    """
    Clase para renderizar la página de inicio
    """
    def get(self, request):
        return render(request, 'index.html', {})