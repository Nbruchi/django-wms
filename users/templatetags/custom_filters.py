from django import template

register = template.Library()

@register.filter
def remove_email_domain(value):
    """Remove known email domains from an email string."""
    domains = ["@yahoo.com", "@gmail.com", "@outlook.com", "@icloud.com", "@protonmail.com"]
    for domain in domains:
        value = value.replace(domain, "")
    return value
