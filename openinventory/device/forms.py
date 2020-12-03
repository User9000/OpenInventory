from django import forms

from .models import Device


class DeviceForm(forms.ModelForm):
    class Meta:

        model = Device
        fields = ['hostname', 'content', 'ipaddress']

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if len(content) > 240:
            raise forms.ValidationError("Content is too long")
        return content

    def clean(self, *args, **kwargs):

        data = self.cleaned_data
        content = data.get('content', None)

        if content == "":
            content = None

        if content is None:
            raise forms.ValidationError('Content  is required')

        return super().clean(*args, **kwargs)