from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReservationForm


def restaurant_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')  # Redireciona para a página de agradecimento
    else:
        form = ReservationForm()
    
    return render(request, 'restaurant.html', {'form': form})

def salvar(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados do formulário no banco de dados
            # Redireciona para a mesma página, mantendo o contexto do formulário vazio
            return render(request, 'restaurant.html', {'form': ReservationForm(), 'success': True})
        # Se o formulário não for válido, renderiza a página novamente com os erros
        return render(request, 'restaurant.html', {'form': form})
    
    # Se o método não for POST (por exemplo, GET), cria um formulário em branco
    form = ReservationForm()
    return render(request, 'restaurant.html', {'form': form})

def reservation_confirmation(request):
    reservas = Reservation.objects.all()  # Busca todas as reservas no banco de dados
    return render(request, 'reservation_confirmation.html', {'reservas': reservas})

def thanks(request):
    return render(request, 'thanks.html')

def deletar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reservation, id=reserva_id)
    if request.method == 'POST':
        reserva.delete()
        return redirect('reservation_confirmation')
    return render(request, 'reservation_confirmation.html', {'reservas': Reservation.objects.all()})

def editar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reservation, id=reserva_id)
    
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reservation_confirmation')  # Redireciona para a confirmação de reservas após editar
    else:
        form = ReservationForm(instance=reserva)  # Inicializa o formulário com os dados da reserva
    
    return render(request, 'editar_reserva.html', {'form': form, 'reserva': reserva})

def formulario_view(request):
    success = False
    hours = list(range(11, 24))
    minutes = ["00", "15", "30", "45"]
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            success = True  # Define success como True se o formulário for válido
    else:
        form = ReservationForm()
    
    return render(request, 'formulario.html', {'form': form, 'success': success, 'hours': hours, 'minutes': minutes})
