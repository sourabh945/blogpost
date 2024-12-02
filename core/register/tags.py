from django import template

reg = template.Library() 

@reg.filter
def has_tag(message_tag,*args):
    for i in args:
        if i not in message_tag:
            return False       
    return True