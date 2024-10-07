from django.shortcuts import render, redirect
from .forms import TeamForm



def index(request):
    # user_email = request.user.email  # Get the logged-in user's email
    user_email = ""

    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)  # Save form without committing
            team.e_mail = user_email  # Assign the user's email to the e_mail field
            team.save()  # Now save the team
            return redirect('/')
    else:
        form = TeamForm()

    return render(request, 'index.html', {'form': form, 'user_email': user_email})

def log_in(request):
    return render(request, "login.html")

