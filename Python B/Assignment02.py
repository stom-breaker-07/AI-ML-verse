
def Batting(run:int,fo:int,six:int,ball:int,fld:int):
    strike_rate=run/ball
    points=0
    if run>=100:
        points+=10
    elif run>=50:
        points+=5
    points+=(run/2)+(fo*1)+(six*2)+(fld*10)
    if strike_rate>100:
        points+=4
    elif 100>strike_rate>80:
        points+=2
    return points

def Bowling(wkts:int,over:int,runs:int,fld:int):
    economy=float(runs/over)
    points=0
    if wkts>=5:
        points+=10
    elif wkts>=3:
        points+=5
    points+=(wkts*10)+(fld*10)
    if 4.5>=economy>3.5:
        points+=4
    elif 3.5>=economy>2:
        points+=7
    else:
        points+=10
    return points


def compute(p1:dict,p2:dict,p3:dict,p4:dict,p5:dict,):
    p1_s=Batting(p1.get("runs"),p1.get("4"),p1.get("6"),p1.get("balls"),p1.get('field'))
    p2_s = Batting(p2.get("runs"), p2.get("4"), p2.get("6"), p2.get("balls"), p2.get('field'))
    p3_s= Bowling(p3.get("wkts"),p3.get("overs"),p3.get("runs"),p3.get('field'))
    p4_s = Bowling(p4.get("wkts"), p4.get("overs"), p4.get("runs"), p4.get('field'))
    p5_s = Bowling(p5.get("wkts"), p5.get("overs"), p5.get("runs"), p5.get('field'))
    Max=max(p1_s,p2_s,p3_s,p4_s,p5_s)
    print(f"MAX Score is {Max}")


if __name__ == '__main__':
    p1 = {'name': 'Virat Kohli', 'role': 'bat', 'runs': 112, '4': 10, '6': 0, 'balls': 119, 'field': 0}
    p2 = {'name': 'du Plessis', 'role': 'bat', 'runs': 120, '4':11, '6':2, 'balls':112, 'field':0}
    p3 = {'name': 'Bhuvneshwar Kumar', 'role': 'bowl', 'wkts': 1, 'overs': 10, 'runs': 71, 'field': 1}
    p4 = {'name': 'Yuzvendra Chahal', 'role': 'bowl', 'wkts': 2, 'overs': 10, 'runs': 45, 'field': 0}
    p5 = {'name': 'Kuldeep Yadav', 'role': 'bowl', 'wkts': 3, 'overs': 10, 'runs': 34, 'field': 0}
    compute(p1,p2,p3,p4,p5)


# Introduction: For this assignment, read the scenario below and then respond to the problem statement described.
# Scenario: The 'Man of the Match' award of a 50-over cricket match is decided by computing points earned by players.
# The points are calculated on the basis of the following rules:
#
# Batting:
# 1 point for 2 runs scored
# Additional 5 points for a half-century
# Additional 10 points for a century
# 2 points for strike rate (runs/balls faced) of 80-100
# Additional 4 points for strike rate>100
# 1 point for hitting a boundary (four) and 2 points for over boundary (six)
# Bowling:
# 10 points for each wicket
# Additional 5 points for three wickets in innings
# Additional 10 points for 5 wickets or more in innings
# 4 points for economy rate (runs given per over) between 3.5 and 4.5
# 7 points for an economic rate between 2 and 3.5
# 10 points for an economy rate less than 2
# Fielding:
#
# 10 points each for catch/stumping/run out

# Problem Statement:
#
# Assuming that these are the top 5 performers,
# write a Python program to decide the player with the highest points.
# \Develop separate functions to compute batting and bowling points and save them in a module.
# These functions should be imported into the main code.
