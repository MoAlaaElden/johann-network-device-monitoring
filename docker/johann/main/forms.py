from django import forms

class AddSingleDevice(forms.Form):
    device_ip = forms.CharField(label="Device IP Address",max_length=50)
    device_username = forms.CharField(label="Device Username", max_length=200)
    device_password = forms.CharField(label="Device Password", widget=forms.PasswordInput)
    #request_verify = forms.ChoiceField(label='Request Verify', choices=[('F','False')], widget=forms.RadioSelect)

class ImportMultipleDevices(forms.Form):
    csv_file = forms.FileField(label="CSV-File: ")

class AddSingleVLAN(forms.Form):
    device_ip = forms.CharField(label="Device IP Address",max_length=50)
    device_username = forms.CharField(label="Device Username", max_length=200)
    device_password = forms.CharField(label="Device Password", widget=forms.PasswordInput)
    vlan_id = forms.CharField(label="VLAN ID", max_length=200)
    vlan_name = forms.CharField(label="VLAN Name", max_length=200)
