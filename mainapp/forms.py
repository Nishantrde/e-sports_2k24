from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import BGMI_Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = BGMI_Team
        fields = ['team_name', 'player_1', 'player_2', 'player_3', 'player_4', 'ph_no', 'e_mail']

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        self.fields['ph_no'].required = False
        self.fields['e_mail'].required = False

    def clean(self):
        cleaned_data = super().clean()
        team_name = cleaned_data.get('team_name')
        ph_no = cleaned_data.get('ph_no')
        e_mail = cleaned_data.get('e_mail')

        # Check if team name already exists
        if BGMI_Team.objects.filter(team_name=team_name).exists():
            raise ValidationError(f"The team name '{team_name}' already exists. Please choose another one.")

        # Validate email if provided
        if e_mail:
            try:
                validate_email(e_mail)
            except ValidationError:
                raise ValidationError("The email address provided is not valid.")
        
        # Check if phone number is exactly 10 digits long and numeric
        if ph_no:
            if not ph_no.isdigit() or len(ph_no) != 10:
                raise ValidationError("The phone number must be 10 digits long and contain only numeric values.")
            
            # Check if phone number already exists
            if BGMI_Team.objects.filter(ph_no=ph_no).exists():
                raise ValidationError(f"The phone number '{ph_no}' is already registered.")

        # Ensure at least one of phone number or email is provided
        if not ph_no and not e_mail:
            raise ValidationError("You must provide either a phone number or an email address.")

        return cleaned_data
