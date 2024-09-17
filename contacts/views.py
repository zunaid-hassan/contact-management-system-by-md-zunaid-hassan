from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm


def contact_list(request):
    contacts = Contact.objects.all()
    query = request.GET.get("q")
    if query:
        contacts = contacts.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(email__icontains=query)
        )
    return render(request, "contacts/contact_list.html", {"contacts": contacts})


def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, "contacts/contact_detail.html", {"contact": contact})


@login_required
def contact_create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else:
        form = ContactForm()
    return render(request, "contacts/contact_form.html", {"form": form})


@login_required
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else:
        form = ContactForm(instance=contact)
    return render(request, "contacts/contact_form.html", {"form": form})


@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("contact_list")
    return render(request, "contacts/contact_confirm_delete.html", {"contact": contact})
