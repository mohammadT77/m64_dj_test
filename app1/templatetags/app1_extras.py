from django import template

register = template.Library()


# {{ value | akbar:arg }}
# {{ value | akbar   }}

@register.filter
def akbar(value, arg):
    return value + arg


@register.simple_tag
def asqar(*args):
    return ('***'.join(args)).upper()
