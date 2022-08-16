from django.shortcuts import render

from .utils.setup_game import (
    BASE_SETUP,
    EXPANSION_SETUP,
    setup_game
)

def index(request):
    num_players = 3
    setup_type = EXPANSION_SETUP
    game = setup_game(setup_type, num_players)
    return render(request, 'carnegie_setup/index.html', context=game)
