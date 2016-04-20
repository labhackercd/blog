from apps.website.models import MenuItem


def statics(request):
    itens_title = MenuItem.objects.filter(class_icon='')
    itens_icon = MenuItem.objects.all().exclude(class_icon='')
    return {'itens_title': itens_title, 'itens_icon': itens_icon}
