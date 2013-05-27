#! -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from itsoho.core.charge.models import Category, Entry, Comment, Tag
from itsoho.core.charge.forms import CommentForm
from itsoho.core.sponsor.models import Sponsor


def charge_index(request):
    categories = Category.objects.all()
    entries = Entry.objects.all()[:30]

    return render(request, 'charge/charge_entry_list.html', {
        'categories': categories,
        'entries':entries,
    })

def charge_entry_list(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, pk=category_id)
    entries = category.entry_set.all()

    return render(request, 'charge/charge_entry_list.html',{
        'categories': categories,
        'entries': entries,
    })


def charge_entry_detail(request, category_id, entry_id, entry_slug=None):
    categories = Category.objects.all()

    entry = get_object_or_404(Entry, pk=entry_id)
    entry.click_count += 1
    entry.save()

    comments = Comment.objects.filter(entry=entry)

    sponsors = Sponsor.objects.all()[:4]

    tags = Tag.objects.all().order_by('?')

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.entry = entry
            comment.save()
            redirect_url = ur"%s#comment-%s" % (request.path, comment.pk)
            return redirect(redirect_url)
    else:
        form = CommentForm(initial=None)

    return render(request, 'charge/charge_entry_detail.html',{
        'categories': categories,
        'entry': entry,
        'comments': comments,
        'sponsors': sponsors,
        'tags': tags,
        'form': form,
    })
