import itertools
import random
import sys

from player import all_players, virtual_player

players = [
    player
    for player in all_players
    if player.name
    in (
        "陈家名",
        # "倪恺隆",
        "杨帅",
        "吕哥",
        "煦坤",
        "宇轩",
        "晓俊",
        "霄哥",
        "乾泰",
        "业总",
        "修然",
        "子龙",
    )
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
           当队伍的进攻能力值和防守能力值满足：
               理想进攻能力值 = 队伍进攻能力值 且 理想防守能力值 = 队伍防守能力值 (势均力敌)
           或  理想进攻能力值 - 允许能力差值 = 队伍进攻能力值 且 理想防守能力值 + 允许能力差值 = 队伍防守能力值 (攻弱守强)
           或  理想进攻能力值 + 允许能力差值 = 队伍进攻能力值 且 理想防守能力值 - 允许能力差值 = 队伍防守能力值 (攻强守弱)
           该队伍编为一队，余下的人编为二队，分组完成，直接返回
        6. 当所有排列组合情况均不满足步骤4中条件，允许能力差值+1，重复步骤4，直到满足步骤4条件为止
    """
    # 如果人数为奇数，则添加一个虚拟球星凑偶数
    if len(players) % 2 == 1:
        players.append(virtual_player)
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
    while True:
        for sub_team in sub_arrays:
            # 获取当前队伍的进攻能力和防守能力
            curr_attack_ability, curr_defense_ability = get_team_ability(sub_team)
            group_success = False
            if (
                avg_attack_ability - capacity == curr_attack_ability
                and avg_defense_ability + capacity == curr_defense_ability
            ):
                group_success = True
            elif (
                avg_attack_ability + capacity == curr_attack_ability
                and avg_defense_ability - capacity == curr_defense_ability
            ):
                group_success = True
            elif (
                capacity >= 2
                and avg_attack_ability - capacity + 1
                <= curr_attack_ability
                <= avg_attack_ability + capacity - 1
                and avg_defense_ability - capacity + 1
                <= curr_defense_ability
                <= avg_defense_ability + capacity - 1
            ):
                group_success = True
            if group_success:
                team1 = [player for player in players if player in sub_team]
                team1_attack_ability, team1_defense_ability = get_team_ability(team1)
                print(
                    f"一队：{', '.join(map(str, team1))}。 进攻能力:{team1_attack_ability}, 防守能力:{team1_defense_ability}"
                )
                team2 = [player for player in players if player not in sub_team]
                team2_attack_ability, team2_defense_ability = get_team_ability(team2)
                print(
                    f"二队：{', '.join(map(str, team2))}。 进攻能力:{team2_attack_ability}, 防守能力:{team2_defense_ability}"
                )
                sys.exit(0)
        capacity += 1
