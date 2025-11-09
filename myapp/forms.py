from django import forms
from .models import Reservation
from datetime import datetime

class ReservationForm(forms.ModelForm):
    time_hour = forms.ChoiceField(choices=[(str(x).zfill(2), str(x).zfill(2)) for x in range(11, 24)], required=True)
    time_minute = forms.ChoiceField(choices=[(str(x).zfill(2), str(x).zfill(2)) for x in [0, 15, 30, 45]], required=True)
    
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'date', 'people', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            # Verifique se self.instance.time não é None antes de acessar hour e minute
            if self.instance.time:
                self.fields['time_hour'].initial = self.instance.time.hour
                self.fields['time_minute'].initial = self.instance.time.minute
    
    def save(self, commit=True):
        instance = super(ReservationForm, self).save(commit=False)
        time_hour = self.cleaned_data.get('time_hour')
        time_minute = self.cleaned_data.get('time_minute')
        time_str = f"{time_hour}:{time_minute}"
        instance.time = datetime.strptime(time_str, '%H:%M').time()
        if commit:
            instance.save()
        return instance
