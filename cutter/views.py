from django.contrib import messages
from django.http import Http404
from django.views.generic.edit import FormMixin
from django.views.generic import ListView
from django.shortcuts import redirect

from random import choice
from string import ascii_letters

from .forms import LinkForm
from .models import Link


class IndexView(FormMixin, ListView):
    model = Link
    template_name = 'index.html'
    context_object_name = 'page'
    extra_context = {
        'title': 'Сократить ссылку',
        'button': 'Сократить',
    }
    form_class = LinkForm

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = LinkForm()
        user = self.request.user
        if user != 'AnonymousUser':
            context['links'] = Link.objects.filter(author__username=user)
        else:
            context['links'] = []

        return context

    def post(self, request, *args, **kwargs):
        LinkForm({
            'author': request.user,
            'url': request.POST['url'],
            'short_url': self.create_short_url()
        }).save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            f'Ссылка успешно создана',
            extra_tags='success'
        )
        return self.get(request, *args, **kwargs)

    @staticmethod
    def create_short_url():
        len = 5
        letnum = ascii_letters + '0123456789'
        short_url = ''.join([choice(letnum) for _ in range(len)])
        return short_url


def redirect_url(request, slug):
    try:
        link = Link.objects.filter(short_url=slug).first()
    except Link.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    return redirect(link.url)



