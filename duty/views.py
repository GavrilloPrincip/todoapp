from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import DutyForm
from .models import duty
# Create your views here.

@login_required
def dutydelete(request,id):
    dutty = get_object_or_404(duty.objects.filter(id = id))
    dutty.delete()
    return redirect("homepage")
def dutyactive(request,id):
    dutty = get_object_or_404(duty.objects.filter(id = id))
    if dutty.statu == "A":
        dutty.statu = "P"
    else:
        dutty.statu = "A"
    dutty.save()
    return redirect("homepage")
