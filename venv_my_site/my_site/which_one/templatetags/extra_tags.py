from django import template

register = template.Library()

@register.filter
def calc(vote_A,vote_B):
    if vote_A ==1 and vote_B == 0:
        return '100%'
    try:
        result = '{:.0%}'.format(vote_A / (vote_A + vote_B))
        return result
    except ZeroDivisionError:
        return "0%" 