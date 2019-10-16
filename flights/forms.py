from django import forms

# run "pip install django-bootstrap-datepicker-plus" for this to work
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput

from . models import Flight


class CreateFlightForm(forms.ModelForm):

    # departure_time = date = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'
    #     })
    # )

    # make specific field required
    # departure_location = forms.CharField(required=True)
    # departure_time = forms.DateField(required=True)

    # Make all fields required
    def __init__(self, *args, **kwargs):
        super(CreateFlightForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True

    class Meta:
        model = Flight

        # show all fields
        # fields = '__all__'

        # Show specific fields
        fields = ('departure_location', 'departure_date', 'departure_time', 'arrival_location', 'arrival_date', 'arrival_time', 'cost', 'status')

        # add class attributes to form fields
        # widgets = {
        #     'departure_time': forms.DateTimeInput(format=('%d/%m/%Y %H:%M'),
        #                                           attrs={
        #                                               'class': 'form-control',
        #                                                  'placeholder': 'Select a date',
        #                                                  'type': 'date',
        #                                                  'required': True
        #                                       }),
        #                                     }

        widgets = {
            'departure_date': DatePickerInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select a date',
                'required': True
            }),

            'departure_time': TimePickerInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select a date',
                'required': True
            }),
        }
