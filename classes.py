from random import choice


class Pokemon:
    """
    A class to represents a pokemon

    Attributes
    __________
    name: str
        The name of the pokemon
    atk_pwr: int
        The attack power of the pokemon
    hp: int
        The life points of the pokemon
    defense: int
        The defense power of the pokemon
    move1: class Move
        The first attack move of the pokemon
    move2: class Move
        The second attack move of the pokemon
    move3: class Move
        The third attack move of the pokemon
    move4: class Move
        The fourth attack move of the pokemon
    type1: str
        The first element of the pokemon
    speed: int
        The speed of the pokemon
    lvl: int
        The level of the pokemon
    xp: int
        The experience points of the pokemon
    type2: str
        The second element of the pokemon

    Methods
    _______

    get_type():
        Return the types of the pokemon
    add_xp(n):
        Add experience points to the pokemon
    add_lvl():
        Add level to the pokemon and more attributes

    """
    def __init__(self, name, atk_pwr, hp, defense, move1, move2, move3, move4, type1, speed, lvl=100, xp=0, type2=None):
        """
        Constructs all the necessary attributes for the pokemon object.
        :param name: str
            The name of the pokemon
        :param atk_pwr: int
            The attack power of the pokemon
        :param hp: int
            The life points of the pokemon
        :param defense: int
            The defense power of the pokemon
        :param move1: class Move
            The first attack move of the pokemon
        :param move2: class Move
            The second attack move of the pokemon
        :param move3: class Move
            The third attack move of the pokemon
        :param move4: class Move
            The fourth attack move of the pokemon
        :param type1: str
            The first element of the pokemon
        :param speed: int
            The speed of the pokemon
        :param lvl: int
            The level of the pokemon
        :param xp: int
            The experience points of the pokemon
        :param type2: str
            The second element of the pokemon
        """
        self.name = name
        self.atk_pwr = atk_pwr
        self.hp = hp
        self.defense = defense
        self.type1 = type1
        self.type2 = type2
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
        self.lvl = lvl
        self.xp = xp
        self.speed = speed

    def get_type(self):
        """
        Create a string with the pokemon's elements
        :return: str
            The pokemon's elements
        """
        if self.type2 is None:
            return f'{self.type1} pokemon'
        return f'{self.type1}-{self.type2} pokemon'

    def add_xp(self, n):
        """
        Add experience points to the pokemon xp attribute
        :param n: int
            The amount of the experience points to add
        :return: None
        """
        self.xp += n

    def add_lvl(self):
        """
        Add level to the pokemon lvl attribute
        :return: None
        """
        self.lvl += 1
        self.hp += choice([1, 2, 3])
        self.atk_pwr += choice([1, 2, 3])
        self.defense += choice([1, 2, 3])
        self.speed += choice([1, 2, 3])
        self.xp = 0


class Move:
    """
     A class to represents an attack move

    Attributes
    __________
    name: str
        The name of the move
    power: int
        The power of the move
    acc: int
        The accuracy of the move
    move_type: str
        The element of the attack
    """

    def __init__(self, name, power, acc, move_type):
        """
        Constructs all the necessary attributes for the move object.

        :param name: str
            The name of the move
        :param power: int
             The power of the move
        :param acc: int
            The accuracy of the move
        :param move_type: str
            The element of the attack
        """
        self.name = name
        self.power = power
        self.acc = acc
        self.move_type = move_type



