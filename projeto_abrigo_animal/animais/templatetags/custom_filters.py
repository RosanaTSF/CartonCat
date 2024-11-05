from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})
# your_app/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})

@register.filter(name='field_icon')
def field_icon(field_name):
    icons = {
        'username': 'fa-user',      # Ícone para campo de usuário
        'password1': 'fa-lock',     # Ícone para campo de senha
        'password2': 'fa-lock',     # Ícone para campo de confirmação de senha
        'email': 'fa-envelope',     # Ícone para campo de email
    }
    return icons.get(field_name, 'fa-question')  # Ícone padrão para campos desconhecidos
