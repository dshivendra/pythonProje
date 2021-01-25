from django.urls import path
from .views import home, login, signup, add_todo, signout, delete_todo,change_todo


urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', signout, name='signout'),
    path('delete-todo/<int:id>', delete_todo),
    path('change-status/<int:id>/<str:status>', change_todo),
    path('add-todo/', add_todo),
]