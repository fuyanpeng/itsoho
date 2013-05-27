# -*- coding: utf-8 -*-
from django import forms
from itsoho.core.charge.models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content',]
