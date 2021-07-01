# from django import forms
# from .models import Cat, CatToy, Player, Team

# class MyForm(forms.Form):
#     storage = {
#         'more_choices' : (1,2,3,4,5),
#         'tup': [],
#         'cats': Cat.objects.all(),
#         'cattoys': CatToy.objects.all(),
#         'cat_tuple': [],
#     }
#     product = {}

#     for num in storage.get('more_choices'):
#         storage.get('tup').append((str(num), str(num)))
#         # print('( inside )', storage.get('tup'))
#     product['x'] = tuple(storage.get('tup'))
#     print('( x )', product['x'])

#     for cat in storage.get('cats'):
#         # print('( cat )', cat)
#         storage.get('cat_tuple').append((cat.name, cat))
#         # print('( inside )', storage.get('cat_tuple'))

#     product['y'] = tuple(storage.get('cat_tuple'))
#     print('( y )', product['y'])
        
#     numbers = forms.ChoiceField(choices=product.get('x'))
#     cats = forms.ChoiceField(choices=product.get('y'))

# class PlayerForm(forms.Form):
#     storage = {
#         # 'teams' : Team.objects.all(),
#         # 'players': Player.objects.all(),
#         # 'cats': Cat.objects.all(),
#         # 'cattoys': CatToy.objects.all(),
#         # 'cat_tuple': [],
#     }
#     product = {}

#     for num in storage.get('more_choices'):
#         storage.get('tup').append((str(num), str(num)))
#         # print('( inside )', storage.get('tup'))
#     product['x'] = tuple(storage.get('tup'))
#     print('( x )', product['x'])

#     for cat in storage.get('cats'):
#         # print('( cat )', cat)
#         storage.get('cat_tuple').append((cat.name, cat))
#         # print('( inside )', storage.get('cat_tuple'))

#     product['y'] = tuple(storage.get('cat_tuple'))
#     print('( y )', product['y'])
        
#     numbers = forms.ChoiceField(choices=product.get('x'))
#     cats = forms.ChoiceField(choices=product.get('y'))