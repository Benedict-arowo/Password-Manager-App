from django import forms
from .models import *


class FolderForm(forms.ModelForm):

    class Meta:
        model = Folder
        fields = '__all__'
        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'bg-slate-200 border-blue-300 lg:w-full font-normal',
                'minlength': '4'
            }),
            "piority": forms.TextInput(attrs={
                'class': 'bg-slate-200 border-blue-300 lg:w-full font-normal',
                'max': '5',
                'min': '0',
                'type': 'number'
            })
        }


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['id', 'user']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'bg-slate-200 border-blue-300 lg:w-full font-normal'
            }),
            'username': forms.TextInput(attrs={
                'class': 'bg-slate-200 border-blue-300 lg:w-full font-normal'
            }),
            'email': forms.TextInput(attrs={
                'class': 'bg-slate-200 border-blue-300 lg:w-full font-normal',
                'type': 'email',
            }),
            'url': forms.TextInput(attrs={
                'class': 'bg-slate-200 border-blue-300 lg:w-full font-normal'
            }),
            'folder': forms.Select(attrs={
                'class': 'bg-slate-200 border-blue-300 lg:w-full font-normal'
            }),
            'password': forms.TextInput(attrs={
                'class': 'bg-slate-200 border-blue-300 lg:w-full font-normal',
                'type': 'password',
            }),
            'notes': forms.Textarea(attrs={
                'class': 'bg-slate-200 border-blue-300 lg:w-full font-normal max-h-36',
                'cols': '30',
                'rows': '10'
            }),
            'piority': forms.TextInput(attrs={
                'class': 'bg-slate-200 border-blue-300 lg:w-full font-normal',
                'type': 'number',
                'min': '0',
                'max': '5'
            }),
            'star': forms.CheckboxInput(attrs={
                'style': 'border-radius: 50%; color:lightgreen'
            })

        }
