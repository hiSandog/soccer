class Player:

    def __init__(self, name, attack_ability, defense_ability):
        self.name = name
        self.attack_ability = attack_ability
        self.defense_ability = defense_ability

    def __str__(self):
        return self.name


all_players = [
    # 版本T0 20分
    Player(name="A", attack_ability=18, defense_ability=2),
    # 版本T1 18分
    Player(name="B", attack_ability=14, defense_ability=4),
    Player(name="C", attack_ability=4, defense_ability=14),
    Player(name="D", attack_ability=9, defense_ability=9),
    # 版本T3 16分
    Player(name="E", attack_ability=12, defense_ability=4),
    Player(name="F", attack_ability=10, defense_ability=6),
    Player(name="G", attack_ability=12, defense_ability=4),
    # 版本T4 14分
    Player(name="H", attack_ability=4, defense_ability=10),
    Player(name="I", attack_ability=7, defense_ability=7),
    Player(name="J", attack_ability=7, defense_ability=7),
    Player(name="K", attack_ability=10, defense_ability=4),
    Player(name="L", attack_ability=8, defense_ability=6),
    # 版本T5 12分
    Player(name="M", attack_ability=3, defense_ability=9),
    Player(name="N", attack_ability=6, defense_ability=6),
    Player(name="O", attack_ability=9, defense_ability=3),
    Player(name="P", attack_ability=3, defense_ability=9),
    # 版本T6 10分
    Player(name="Q", attack_ability=5, defense_ability=5),
    Player(name="R", attack_ability=3, defense_ability=7),
    Player(name="S", attack_ability=5, defense_ability=5),
    Player(name="T", attack_ability=5, defense_ability=5),
]

# 如果参赛球星人数为奇数，则添加一个虚拟球星凑偶数，这样做的目的是因为人多的一队没有禁区外开火权，应该给予能力值补充，否则对人多的一队不公平
virtual_player = Player(name="虚拟球星", attack_ability=4, defense_ability=4)
