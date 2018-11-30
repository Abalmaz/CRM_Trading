from django import template

register = template.Library()


@register.simple_tag(name='has_perm', takes_context=True)
def has_perm(context, *args):
    company = context['company']
    user = context['user']
    user_perms = user.get_current_permissions(company)
    perm = []
    for arg in args:
        perm.append(arg)
    if len(set(user_perms).intersection(perm)) <= 0:
        return False
    return True
