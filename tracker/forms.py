# tracker/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import Link, Campaign

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Campaign Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Campaign Description', 'rows': 3}),
        }

class LinkForm(forms.ModelForm):
    campaign = forms.ModelChoiceField(
        queryset=None,
        required=False,
        empty_label="No Campaign (Optional)",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Link
        fields = ['original_url', 'name', 'campaign']
        widgets = {
            'original_url': forms.URLInput(attrs={'placeholder': 'https://example.com?var={variable_name}'}),
            'name': forms.TextInput(attrs={'placeholder': 'My Link'})
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['campaign'].queryset = Campaign.objects.filter(user=user)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
