from random import choice, randint
import os
from time import sleep
from logistics import check_input, sprint, types_effect


def battle(pok1, pok2, atk_move):
    """
    Calculate the damage done by the attacker and the conditions: immune, resist and super effective.
    Also calculate if the damage is critical
    :param pok1: class Pokemon
        The attacker
    :param pok2: class Pokemon
        the defender
    :param atk_move: class classes.Move
        The attack move of the attacker
    :return: int, str, bool
        The damage, the condition and if the attack is critical.
    """
    lvl = pok1.lvl
    power = atk_move.power
    rand = randint(85,  100)
    atk_type = atk_move.move_type
    stab = 1.5 if pok1.type1 == atk_type or pok1.type2 == atk_type else 1
    crit_tup = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.5)
    critical = choice(crit_tup)
    is_crit = critical == 1.5
    types_dict = types_effect()
    pok2_types = (pok2.type1, pok2.type2)
    is_resist = any(item in types_dict[atk_type]['resist'] for item in pok2_types)
    is_effective = any(item in types_dict[atk_type]['effective'] for item in pok2_types)
    is_immune = any(item in types_dict[atk_type]['immune'] for item in pok2_types)
    if is_resist:
        target_type = 0.5
        display_eff = "It's not very effective..."
    elif is_effective:
        target_type = 2
        display_eff = "It's super effective!"
    elif is_immune:
        target_type = 0
        display_eff = 'The attack has no effect'
    else:
        target_type = 1
        display_eff = ''
    damage = (((((((2 * lvl)/5) + 2) * power * (pok1.atk_pwr / pok2.defense))/50) + 2) * (rand / 100)
              * critical * stab * target_type)
    return damage, display_eff, is_crit


def attack(attacker, defender, defender_hp, attacker_move, rival_turn=False):
    """
    Display the combat turns and reduce the damage done by the attack from the defender life points
    :param attacker: class Pokemon
        The attacker
    :param defender: class Pokemon
        The defender
    :param defender_hp: int
        The defender life points
    :param attacker_move: class Move
        The attack move of the attacker
    :param rival_turn: bool
        Indicates if it's the rival turn or the player turn
    :return: int
        The defender hp after reducing the damage done by the attacker
    """
    hp_reduce, disp_eff, is_crit = battle(attacker, defender, attacker_move)
    defender_hp -= hp_reduce
    if rival_turn and attacker.name == defender.name:
        attacker_name = 'rival' + attacker.name
    else:
        attacker_name = attacker.name
    sprint(f'{attacker_name} used {attacker_move.name}!')
    if is_crit:
        sprint('A critical hit!')
        sleep(1)
    sprint(disp_eff)
    sleep(1)
    return defender_hp


def the_game(pok1, pok2):
    """
    The course of the game
    :param pok1: class Pokemon
        The player's pokemon
    :param pok2: class Pokemon
        The rival pokemon
    :return: None
    """
    rival_name = 'rival ' + pok2.name if pok1.name == pok2.name else pok2.name
    sprint(f'{pok1.name} I choose you!')
    sprint(f'Rival chose {rival_name}')
    sleep(4)
    os.system('CLS')
    sprint('Rival challenge you for a battle!')
    player_hp = pok1.hp
    rival_hp = pok2.hp
    player_win = False
    flag = True
    while flag:
        pok1_moves = (pok1.move1, pok1.move2, pok1.move3, pok1.move4)
        pok2_moves = (pok2.move1, pok2.move2, pok2.move3, pok2.move4)
        sprint(f'What should {pok1.name} do?')
        sprint(f'[1] {pok1.move1.name}    [2] {pok1.move2.name}')
        sprint(f'[3] {pok1.move3.name}    [4] {pok1.move4.name}')
        choose_atk = input('Enter your choice: ')
        final_choose_atk = check_input(choose_atk, ['1', '2', '3', '4'])
        pok1_atk = pok1_moves[int(final_choose_atk) - 1]
        rival_atk = choice((1, 2, 3, 4))
        pok2_atk = pok2_moves[rival_atk - 1]
        os.system('CLS')
        if pok1_atk.name == 'Quick Attack' or (pok1.speed > pok2.speed and pok2_atk.name != 'Quick Attack'):
            rival_hp = attack(pok1, pok2, rival_hp, pok1_atk)
            if rival_hp <= 0:
                flag = False
                player_win = True
                continue
            sprint(f'{rival_name} have {round(rival_hp)} hp left')
            player_hp = attack(pok2, pok1, player_hp, pok2_atk, rival_turn=True)
            if player_hp <= 0:
                flag = False
                continue
            sprint(f'{pok1.name} have {round(player_hp)} hp left')
        else:
            player_hp = attack(pok2, pok1, player_hp, pok2_atk, rival_turn=True)
            if player_hp <= 0:
                flag = False
                continue
            sprint(f'{pok1.name} have {round(player_hp)} hp left')
            rival_hp = attack(pok1, pok2, rival_hp, pok1_atk)
            if rival_hp <= 0:
                flag = False
                player_win = True
                continue
            sprint(f'{rival_name} have {round(rival_hp)} hp left')
        sleep(4)
        os.system('CLS')
    if player_win:
        sprint(f'{rival_name} fainted')
        exp = pok2.atk_pwr + pok2.hp
        sprint(f'{pok1.name} gained {exp} EXP points')
        pok1.add_xp(exp)
        if pok1.xp >= 200:
            pok1.add_lvl()
            sprint(f'{pok1.name} leveled up to level {pok1.lvl}!')
        sprint('You win!')
    else:
        sprint(f'{pok1.name} fainted')
        sprint('You lose...')
    sleep(3)
    os.system('CLS')
