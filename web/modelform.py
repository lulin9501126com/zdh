#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : linlin
# @Software: PyCharm

from django import forms
from web import models
class Register(forms.ModelForm):
    class Meta:
        model = models.Userinfo
        fields = '__all__'

    def __init__(self, *args, **kwargs,):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })
