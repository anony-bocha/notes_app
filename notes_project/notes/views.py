from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from .models import Note
from .forms import NoteForm  # Your Note form

class LogoutGetView(LogoutView):
    http_method_names = ['get', 'post']

@login_required
def home(request):
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notes/home.html', {'notes': notes})

@login_required
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('notes:home')
    else:
        form = NoteForm()
    return render(request, 'notes/add_notes.html', {'form': form})

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes:home')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/add_notes.html', {'form': form, 'note': note})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('notes:home')
    return render(request, 'notes/delete_note_confirm.html', {'note': note})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log user in immediately after signup
            return redirect('notes:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            return redirect('notes:home')
    else:
        form = UserCreationForm()
    # Use registration/signup.html since your template is there
    return render(request, 'registration/signup.html', {'form': form})
