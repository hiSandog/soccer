import itertools
import random
import sys


class Player:

    def __init__(self, name, attack_ability, defense_ability):
        self.name = name
        self.attack_ability = attack_ability
        self.defense_ability = defense_ability

    def __str__(self):
        return self.name


players = [
    Player(name="A", attack_ability=8, defense_ability=3),
    Player(name="B", attack_ability=3, defense_ability=9),
    Player(name="C", attack_ability=2, defense_ability=6),
    Player(name="D", attack_ability=6, defense_ability=6),
    Player(name="E", attack_ability=3, defense_ability=7),
    Player(name="F", attack_ability=6, defense_ability=3),
    Player(name="G", attack_ability=8, defense_ability=3),
    Player(name="H", attack_ability=8, defense_ability=2),
    Player(name="J", attack_ability=6, defense_ability=3),
    Player(name="K", attack_ability=4, defense_ability=4),
]


def get_team_ability(team: []):
    attack_ability = 0
    defense_ability = 0
    for player in team:
        attack_ability += player.attack_ability
        defense_ability += player.defense_ability
    return attack_ability, defense_ability


if __name__ == "__main__":
    """
    算法思路：
        1. 给所有球星标注能力值，分为进攻能力和防守能力，满分均为10分
        2. 如果参赛球星人数为奇数，则添加一个虚拟球星凑偶数，这样做的目的是因为人多的一队没有禁区外开火权，应该给予能力值补充，否则对人多的一队不公平
        3. 分别计算参赛球星的总的进攻能力值和防守能力值，每队的理想能力值为总能力值的一半
        4. 获得本次分组的所有排列组合情况，并且打乱排列组合情况，这样做的原因是使得每一次执行，结果都不一样
        5. 先设定一个允许能力差值，该值从0开始，将所有排列组合情况进行判断,
           当队伍的进攻能力值和防守能力值都满足：理想能力值-允许能力差值 <= 当前队伍能力值 <= 理想能力值+允许能力差值，
           该队伍编为一队，余下的人编为二队，分组完成，直接返回
        6. 当所有排列组合情况均不满足步骤4中条件，允许能力差值+1，重复步骤4，直到满足步骤4条件为止
    """
    # 如果人数为奇数，则添加一个虚拟球星凑偶数
    if len(players) % 2 == 1:
        players.append(Player(name="虚拟球星", attack_ability=3, defense_ability=3))
    # 打乱参赛球星
    random.shuffle(players)
    # 获取参赛球星总进攻能力和防御能力
    sum_attack_ability, sum_defense_ability = get_team_ability(players)
    # 计算每队该有的进攻能力和防御能力，即总的进攻能力和防守能力的一半
    avg_attack_ability = int(sum_attack_ability / 2)
    avg_defense_ability = int(sum_defense_ability / 2)
    # 每队的人数
    team_size = int(len(players) / 2)
    # 获得当前每队人数的所有可能分组集合
    sub_arrays = list(itertools.combinations(players, team_size))
    # 打乱可能分组集合，这样可以使得每次分组结果不同
    random.shuffle(sub_arrays)
    # 允许每队和上面计算出的该有的进攻能力和防御能力差值，从零开始
    capacity = 0
    # 最大可允许的差值，超过这个数，分组失败，如果非要分组，就调大该值重跑
    allowable_capacity = 3
    while True:
        for sub_team in sub_arrays:
            # 获取当前队伍的进攻能力和防守能力
            curr_attack_ability, curr_defense_ability = get_team_ability(sub_team)
            # 判断当前队伍的能力是不是在可以接受的能力差值之内，如果是，剩下的人自动组成二队，分组成功，直接返回
            if (
                avg_attack_ability - capacity
                <= curr_attack_ability
                <= avg_attack_ability + capacity
                and avg_defense_ability - capacity
                <= curr_defense_ability
                <= avg_defense_ability + capacity
            ):
                if capacity == 0:
                    print("分组状态：势均力敌")
                elif capacity == 1:
                    print("分组状态：些许不平衡")
                else:
                    print("分组状态：不太平衡")
                print(f"一队：{', '.join(map(str, sub_team))}")
                team2 = [player for player in players if player not in sub_team]
                print(f"二队：{', '.join(map(str, team2))}")
                sys.exit(0)
        if capacity > allowable_capacity:
            print("当前参赛球星无法调配至一个合理的分组，若想继续，请调大最大可允许差值(allowable_capacity)")
            sys.exit(1)
        capacity += 1
