from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/home.html', {'notes': notes})
@login_required
def add_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Note.objects.create(user=request.user, title=title, content=content)
        return redirect('home')
    return render(request, 'notes/add_notes.html')  # ✅ use this name


@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        return redirect('home')
    return render(request, 'notes/add_notes.html', {'note': note}) 

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            # show errors on form
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


