from django import template

register = template.Library()

@register.filter
def add_class(value, arg):
    """
    Adds CSS classes to a form field's widget.
    Usage: {{ form.field|add_class:"class1 class2" }}
    """
    return value.as_widget(attrs={'class': arg})
