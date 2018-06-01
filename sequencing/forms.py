from .models import *
from django.views.generic import ListView, DetailView, UpdateView
from django import forms

class SampleEditForm(UpdateView):
    model = Sample
    fields = '__all__'

    def get_form(self, form_class = None):
        form = super(SampleEditForm, self).get_form(form_class)
        # limit lanes to lanes on the run
        form.fields['lane'].queryset = Lane.objects.filter(run=self.get_object().run)
        form.fields['lane'].empty_label = None
        # limit run to only this run so they can't change it
        form.fields['run'].queryset = Run.objects.filter(id=self.get_object().run.id)
        form.fields['run'].empty_label = None
        return form
