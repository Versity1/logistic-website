from django import forms

class TrackingForm(forms.Form):
    tracking_id = forms.UUIDField(
         
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your tracking code. e.g. 987733733-GT'}),
    )
