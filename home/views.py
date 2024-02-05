from django.shortcuts import render
from django import views


class HomePageView(views.View):
    template_name = 'home/home_page.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass

