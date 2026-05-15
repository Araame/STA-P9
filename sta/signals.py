from django.models.signals import post_save
from django.dispatch import receiver
from .models import Note

@receiver(post_save, sender=Note)
def new_note_signal(sender, instance, **kwargs):
    if created: # type: ignore
        title = instance.note.title
        owner = instance.note.owner
        message = f"A new note {title} is created by {owner}"
        print(message)