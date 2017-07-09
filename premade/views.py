from django.shortcuts import render
from .forms import StrategyForm

# Create your views here.
def index(request):
	if request.method == "POST":
		form = StrategyForm(request.POST)

		if form.is_valid():
			pass
	else:
	    form = StrategyForm()
	return render(request,"premade/index.html",{'form': form})