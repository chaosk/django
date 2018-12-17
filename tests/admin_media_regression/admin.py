from django import forms
from django.contrib import admin
from django.db import models

from .models import Holder5, Inner5

site = admin.AdminSite(name="admin")


class TestMediaWidget(forms.NumberInput):
    class Media:
        js = ('test.js', )


class Inner5Inline(admin.TabularInline):
    model = Inner5
    formfield_overrides = {models.IntegerField: {"widget": TestMediaWidget}}


class Holder5Admin(admin.ModelAdmin):
    inlines = [Inner5Inline]
    fieldsets = (("Fieldset", {"classes": ("collapse",), "fields": ("dummy",)}),)
    formfield_overrides = {models.IntegerField: {"widget": TestMediaWidget}}

site.register(Holder5, Holder5Admin)
