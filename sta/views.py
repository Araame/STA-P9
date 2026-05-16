from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Note
from django.urls import reverse_lazy
from .forms import NoteUpdateForm
import ollama
from django.shortcuts import render
from django.db.models import Count
from datetime import datetime, timedelta

# Create your views here.
class AllNotesListView(LoginRequiredMixin,ListView):
    model = Note
    template_name = 'all_notes.html'
    context_object_name = 'notes'

class NoteDetailView(DetailView):
    model = Note
    template_name = 'detail.html'
    context_object_name = 'note'

class HomeView(LoginRequiredMixin,ListView):
    model = Note
    template_name = 'home.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(owner = self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actual_date = datetime.now().date
        #date_limit = actual_date - timedelta(days=7)
        context['total_notes'] = Note.objects.aggregate(Count("id"))
        #context['weekly_notes_num'] = Note.objects.filter(date__gte = date_limit).aggregate(Count("id"))
        context['recent_notes'] = Note.objects.order_by('date')[:5]
        return context




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
    template_name = 'update_note.html'
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
        notes = Note.objects.filter(owner=request.user)
        notes_text = "\n".join([f"{note.title}: {note.description}" for note in notes])

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
        return render(request, "reports.html", {"resume": resume})

    return render(request, "reports.html")