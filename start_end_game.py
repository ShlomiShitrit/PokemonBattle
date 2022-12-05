import os
from time import sleep
from random import choice
from logistics import check_input, sprint
from progress_func import save_progress


def start_game(pokemon_tup, index_tup, choice_str):
    """
    Start the game by letting the player decide what pokemon they want to fight with.
    Also choose randomly a pokemon for the rival
    :param pokemon_tup: tuple
        A tuple of the pokemon options to choose from
    :param index_tup: tuple
        A tuple with the indexes of the pokemon tuple
    :param choice_str: str
        The index of the pokemon that the player chooses
    :return: class Pokemon, class Pokemon
        The pokemon that the player chose and the randomly selected pokemon for the rival
    """
    os.system('CLS')
    sprint(choice_str)
    choose = input('enter choice: ')
    final_choose = check_input(choose, index_tup)
    player_pok = pokemon_tup[int(final_choose) - 1]
    rival_pok = choice(pokemon_tup)
    return player_pok, rival_pok


def end_game(pokemon_tup):
    """
    Checks if the player want to save the game, and saving it for him.
    Also checks if the player want to continue playing.
    :param pokemon_tup: tuple
        The tuple with all the pokemons of the player
    :return: bool
        Boolean value that's indicates if the player wants to keep playing
    """
    flag = True
    save_the_game = input('Do you want to save your progress? y/n ')
    save_game_check = check_input(save_the_game, ('y', 'n'))
    if save_game_check == 'y':
        slot_pick = input('At what slot you want to save your progress? 1/2/3 ')
        slot_check = check_input(slot_pick, ('1', '2', '3'))
        save_progress(slot_check, pokemon_tup)
        sprint('Progress saved!')
        sleep(2)
    elif save_game_check == 'n':
        sleep(2)
    keep_play = input('Do you want to keep playing? y/n ')
    keep_play_check = check_input(keep_play, ('y', 'n'))
    if keep_play_check == 'n':
        sprint('Goodbye!')
        flag = False
    elif keep_play_check == 'y':
        sprint('Please Wait...')
        sleep(3)
    return flag
