from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView
import telegram
from .models import *
from .forms import *


class Home(ListView):
    model = Skills
    template_name = 'my_portfolio/index.html'
    context_object_name = 'skills'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['title'] = 'Kanin Nikita`s Portfolio'
        context['projects'] = Projects.objects.all()
        context['form'] = ContactForm()
        context['about_me'] = AboutMe.objects.all()
        return context


def contact_me(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            bot = telegram.Bot(token='')
            message = f'Name: {form.cleaned_data["name"]}\nE-mail: {form.cleaned_data["user_email"]}\n' \
                      f'Subject: {form.cleaned_data["subject"]}\n{form.cleaned_data["message"]}'
            bot.send_message(586551552, message)
            messages.success(request, 'Письмо отправлено, я скоро свяжусь с вами.')
            return redirect('home')
        else:
            messages.error(request, 'Поле e-mail заполнено не корректно.')
    return redirect('home')
