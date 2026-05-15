from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.base import TemplateView
from .models import Note
from django.urls import reverse_lazy
from .forms import NoteUpdateForm
import ollama
from django.shortcuts import render

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html', context = {})

class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'home.html'


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'list_notes.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'description', 'image', 'category']
    template_name = 'creation_form.html'
    success_url = reverse_lazy('list_notes')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteUpdateForm
    template_name = 'creation_form.html'
    success_url = reverse_lazy('list_notes')

    def test_func(self):
        note = self.get_object()
        return note.owner == self.request.user


class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    template_name = 'delete.html'
    success_url = reverse_lazy('list_notes')

    def test_func(self):
        note = self.get_object()
        return note.owner == self.request.user







def week_summarize(request):

    if request.method == "POST":
        notes = Note.objects.filter(owner =request.user)
        notes_text = "\n".join([f"- {note.title}: {note.description}" for note in notes])

        response = ollama.chat(
            model="llama3.2",
            messages=[{
                "role": "user",
                "content": f"""
                You are a productivity assistant.
                Analyze the following notes and produce:
                Weekly overview, Main issues, Key insights,
                Positive achievements, Action plan for next week
                {notes_text}
                """
            }]
        )

        resume = response['message']['content']
        return render(request, "home.html", {"resume": resume})