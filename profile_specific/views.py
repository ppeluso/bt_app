from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

@login_required
def profile(request):
	user = request.user
	return render(request, "profile_specific/profile.html", {'user': user})