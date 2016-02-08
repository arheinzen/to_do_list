from django.conf.urls import url
from django.views.generic import TemplateView
from .views import TodoListView

urlpatterns = [
    
    url(r'^todolist/$', TodoListView.as_view()),
    url(r'^todoform/$', 'main.views.Todo'),
    
    
]