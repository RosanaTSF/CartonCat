# your_app/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    """
    Adiciona uma classe CSS ao campo do formulário.
    
    Args:
        field: O campo do formulário.
        css_class: A classe CSS a ser adicionada.
    
    Returns:
        O campo do formulário com a classe CSS adicionada.
    """
    return field.as_widget(attrs={"class": css_class})

@register.filter(name='field_icon')
def field_icon(field_name):
    """
    Retorna o ícone FontAwesome correspondente ao nome do campo do formulário.
    
    Args:
        field_name: O nome do campo do formulário.
    
    Returns:
        O ícone FontAwesome correspondente ao nome do campo.
    """
    icons = {
        'username': 'fa-user',      # Ícone para campo de usuário
        'password1': 'fa-lock',     # Ícone para campo de senha
        'password2': 'fa-lock',     # Ícone para campo de confirmação de senha
        'email': 'fa-envelope',     # Ícone para campo de email
    }
    return icons.get(field_name, 'fa-question')  # Ícone padrão para campos desconhecidos