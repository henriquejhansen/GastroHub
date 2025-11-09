from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def reservation_confirmation(request):
    reservas = Reservation.objects.all()
    return render(request, 'reservation_confirmation.html', {'reservas': reservas})
