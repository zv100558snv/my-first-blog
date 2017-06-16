from django.views.generic.edit import FormView      
from django.contrib.auth.forms import UserCreationForm 


class RegisterFormView(FormView):
    form_class = UserCreationForm     
    success_url = "/" 
    template_name = "register.html" 

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)
