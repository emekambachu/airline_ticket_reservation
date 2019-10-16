from django import forms
from . models import Flight


class CreateFlightForm(forms.ModelForm):

    # make specific field required
    # departure_location = forms.CharField(required=True)

    # Make all fields required
    def __init__(self, *args, **kwargs):
        super(CreateFlightForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True

    class Meta:
        model = Flight
        fields = ('departure_location', 'departure_time', 'arrival_location', 'arrival_time', 'cost', 'status')

        # add class attributes to form fields
        widgets = {
            'departure_location': forms.TextInput(attrs={'class': 'form-control'}),
        }