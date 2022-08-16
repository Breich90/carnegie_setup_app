from django.shortcuts import render

from .utils.setup_game import (
    BASE_SETUP,
    EXPANSION_SETUP,
    setup_game
)

def index(request):
    setup_type = ''
    num_players = 0
    if request.method == 'POST':
        setup_type = request.POST.get('game_type')
        if setup_type == 'base_setup':
            setup_type = BASE_SETUP
        elif setup_type == 'expansion_setup':
            setup_type = EXPANSION_SETUP
        num_players = int(request.POST.get('num_players'))
    if not setup_type or not num_players:
        return render(request, 'carnegie_setup/index.html', context={'error': 'Form invalid'})
    else:
        game = setup_game(setup_type, num_players)
        game['num_players'] = num_players
        return render(request, 'carnegie_setup/index.html', context=game)
