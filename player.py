class Player:

    def __init__(self, name, attack_ability, defense_ability):
        self.name = name
        self.attack_ability = attack_ability
        self.defense_ability = defense_ability

    def __str__(self):
        return self.name


all_players = []

# 如果参赛球星人数为奇数，则添加一个虚拟球星凑偶数，这样做的目的是因为人多的一队没有禁区外开火权，应该给予能力值补充，否则对人多的一队不公平
virtual_player = Player(name="虚拟球星", attack_ability=4, defense_ability=4)
