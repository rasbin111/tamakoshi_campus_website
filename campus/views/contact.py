from django.shortcuts import render
from django.views import View
from campus.forms import ParticipantForm
from campus.models import Participant

class ContactView(View):
    def get(self, request):
        form = ParticipantForm()
        return render(request, 'contact.html', {'form': form})

    def post(self, request):
        form = ParticipantForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            full_name = form.cleaned_data['full_name']
            user_message = form.cleaned_data['message']
            try:
                participant = Participant.objects.get(email=email)
            except Exception as e:
                participant = Participant.objects.create(email=email,
                                                         phone_number=phone_number,
                                                         full_name=full_name)
            participant.message.create(message=user_message)
            form = ParticipantForm()
            return render(request, 'contact.html', {'form': form, "success": True})

        return render(request, "contact.html", {
            'form': form
        })

def message_success_view(request):
    return render(request, 'message_success.html')