from .models import *
from django.views.generic import ListView, DetailView, UpdateView
from django import forms

'''class SampleEditModelForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = '__all__'
    #run = forms.CharField(disabled = True)
    #lane = forms.CharField(disabled = True)
    def __init__(self, sam, *args, **kwargs):
        super(SampleEditModelForm, self).__init__(*args, **kwargs)
        self.fields['lane'].queryset = Lane.objects.filter(run=sam.run)'''

class SampleEditForm(UpdateView):
    model = Sample
    fields = '__all__'

    def get_form(self, form_class = None):
        form = super(SampleEditForm, self).get_form(form_class)
        form.fields['lane'].queryset = Lane.objects.filter(run=self.get_object().run)
        form.fields['lane'].empty_label = None
        form.fields['run'].queryset = Run.objects.filter(id=self.get_object().run.id)
        form.fields['run'].empty_label = None
        return form
