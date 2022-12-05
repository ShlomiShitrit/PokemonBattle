from classes import Pokemon, Move
from game_func import the_game
from progress_func import is_save
from start_end_game import start_game, end_game


def main():
    vine_whip = Move('Vine Whip', 45, 100, 'Grass')
    razor_leaf = Move('Razor Leaf', 55, 95, 'Grass')
    double_edge = Move('Double Edge', 120, 100, 'Normal')
    solar_beam = Move('Solar Beam', 120, 100, 'Grass')
    water_gun = Move('Water Gun', 40, 100, 'Water')
    water_pulse = Move('Water Pulse', 60, 100, 'Water')
    hydro_pump = Move('Hydro Pump', 110, 80, 'Water')
    skull_bash = Move('Skull Bash', 130, 100, 'Normal')
    dragon_breath = Move('Dragon Breath', 60, 100, 'Dragon')
    flame_thrower = Move('FlameThrower', 90, 100, 'Fire')
    inferno = Move('Inferno', 100, 50, 'Fire')
    flare_blitz = Move('Flare Blitz', 120, 100, 'Fire')
    swift = Move('Swift', 60, None, 'Normal')
    quick_attack = Move('Quick Attack', 40, 100, 'Normal')
    tackle = Move('Tackle', 50, 100, 'Normal')
    bug_buzz = Move('Bug Buzz', 90, 100, 'Bug')
    air_slash = Move('Air Slash', 75, 95, 'Flying')
    psybeam = Move('Psybeam', 65, 100, 'Psychic')
    confusion = Move('Confusion', 50, 100, 'Psychic')
    wing_attack = Move('Wing Attack', 60, 100, 'Flying')
    aerial_ace = Move('Aerial Ace', 60, None, 'Flying')
    hurricane = Move('Hurricane', 110, 70, 'Flying')
    thunder = Move('Thunder', 110, 70, 'Electric')
    iron_tail = Move('Iron Tail', 100, 75, 'Steel')
    thunderbolt = Move('Thunderbolt', 90, 100, 'Electric')
    spark = Move('Spark', 65, 100, 'Electric')
    slash = Move('Slash', 70, 100, 'Normal')
    dig = Move('Dig', 80, 100, 'Ground')
    earthquake = Move('Earthquake', 100, 100, 'Ground')

    table = is_save()

    bulbasaur = Pokemon(name=table['A2'].value, atk_pwr=int(table['B2'].value), hp=int(table['C2'].value),
                        defense=int(table['D2'].value), move1=vine_whip, move2=razor_leaf,
                        move3=double_edge, move4=solar_beam, type1='Grass', type2='Poison',
                        speed=int(table['E2'].value), lvl=int(table['F2'].value), xp=int(table['G2'].value))

    squirtle = Pokemon(name=table['A3'].value, atk_pwr=int(table['B3'].value), hp=int(table['C3'].value),
                       defense=int(table['D3'].value), move1=water_gun, move2=water_pulse,
                       move3=hydro_pump, move4=skull_bash, type1='Water', speed=int(table['E3'].value),
                       lvl=int(table['F3'].value), xp=int(table['G3'].value))

    charmander = Pokemon(name=table['A4'].value, atk_pwr=int(table['B4'].value), hp=int(table['C4'].value),
                         defense=int(table['D4'].value), move1=dragon_breath, move2=flame_thrower, move3=inferno,
                         move4=flare_blitz, type1='Fire', speed=int(table['E4'].value),
                         lvl=int(table['F4'].value), xp=int(table['G4'].value))

    eevee = Pokemon(name=table['A5'].value, atk_pwr=int(table['B5'].value), hp=int(table['C5'].value),
                    defense=int(table['D5'].value), move1=tackle, move2=quick_attack, move3=swift, move4=double_edge,
                    type1='Normal', speed=int(table['E5'].value), lvl=int(table['F5'].value), xp=int(table['G5'].value))

    butterfree = Pokemon(name=table['A6'].value, atk_pwr=int(table['B6'].value), hp=int(table['C6'].value),
                         defense=int(table['D6'].value), move1=confusion, move2=psybeam, move3=air_slash,
                         move4=bug_buzz, type1='Flying', type2='Bug', speed=int(table['E6'].value),
                         lvl=int(table['F6'].value), xp=int(table['G6'].value))

    pidgey = Pokemon(name=table['A7'].value, atk_pwr=int(table['B7'].value), hp=int(table['C7'].value),
                     defense=int(table['D7'].value), move1=wing_attack, move2=aerial_ace, move3=air_slash,
                     move4=hurricane, type1='Flying', type2='Normal', speed=int(table['E7'].value),
                     lvl=int(table['F7'].value), xp=int(table['G7'].value))

    pikachu = Pokemon(name=table['A8'].value, atk_pwr=int(table['B8'].value), hp=int(table['C8'].value),
                      defense=int(table['D8'].value), move1=spark, move2=thunderbolt, move3=iron_tail, move4=thunder,
                      type1='Electric', speed=int(table['E8'].value), lvl=int(table['F8'].value),
                      xp=int(table['G8'].value))

    sandshrew = Pokemon(name=table['A9'].value, atk_pwr=int(table['B9'].value), hp=int(table['C9'].value),
                        defense=int(table['D9'].value), move1=swift, move2=slash, move3=dig, move4=earthquake,
                        type1='Ground', speed=int(table['E9'].value), lvl=int(table['F9'].value),
                        xp=int(table['G9'].value))

    pok_tup = (bulbasaur, squirtle, charmander, eevee, butterfree, pidgey, pikachu, sandshrew)
    ind_tup = tuple([str(ind) for ind in range(1, len(pok_tup) + 1)])
    pokemon_choose = ('choose your pokemon:\n'
                      f'[1] {bulbasaur.name}  [2] {squirtle.name}    [3] {charmander.name}\n'
                      f'[4] {eevee.name}      [5] {butterfree.name}  [6] {pidgey.name}\n'
                      f'[7] {pikachu.name}    [8] {sandshrew.name}')
    flag = True
    while flag:
        player_pok, rival_pok = start_game(pok_tup, ind_tup, pokemon_choose)
        the_game(player_pok, rival_pok)
        flag = end_game(pok_tup)


if __name__ == '__main__':
    main()
