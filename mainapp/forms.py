from django import forms
from .models import BGMI_Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = BGMI_Team
        fields = ['team_name', 'player_1', 'player_2', 'player_3', 'player_4', 'ph_no']

    def clean(self):
        cleaned_data = super().clean()
        team_name = cleaned_data.get('team_name')
        ph_no = cleaned_data.get('ph_no')

        # Check if team name already exists
        if BGMI_Team.objects.filter(team_name=team_name).exists():
            raise forms.ValidationError(f"The team name '{team_name}' already exists. Please choose another one.")

        # Check if phone number already exists
        if BGMI_Team.objects.filter(ph_no=ph_no).exists():
            raise forms.ValidationError(f"The phone number '{ph_no}' is already registered.")

        return cleaned_data
