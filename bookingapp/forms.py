from django import forms

class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES = (
        ('Unterrichtsraum', 'Unterrichtsraum'),
        ('Hörsaal', 'Hörsaal'),
        ('PC-Raum', 'PC-Raum'),
        ('Selbstlernecke', 'Selbstlernecke'),
    )
    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])