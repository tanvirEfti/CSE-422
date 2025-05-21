import random
import math

def strength(x):
    power = math.log2(x + 1) + x / 10
    return power

def utility_func(max_player_rating, min_player_rating):
    utility = strength(max_player_rating) - strength(min_player_rating) + (-1) ** random.choice([0, 1]) * (random.randrange(0, 10) / 10)
    return utility

def minimax_alpha_beta_without_magic(depth, max_rating, min_rating, alpha, beta, player):
    if depth == 0:
        return utility_func(max_rating, min_rating)

    if player: 
        max_val = float('-inf')
        for i in range(2): 
            recurr = minimax_alpha_beta_without_magic(depth - 1, max_rating, min_rating, alpha, beta, False)
            max_val = max(max_val, recurr)
            alpha = max(alpha, recurr)
            if alpha >= beta:
                break  
        return max_val
    else:  
        min_val = float('inf')
        for i in range(2):  
            recurr = minimax_alpha_beta_without_magic(depth - 1, max_rating, min_rating, alpha, beta, True)
            min_val = min(min_val, recurr)
            beta = min(beta, recurr)
            if alpha >= beta:
                break 
        return min_val
    



def minimax_alpha_beta_with_magic(depth, max_rating, min_rating, alpha, beta, player):
    if depth == 0:
        return utility_func(max_rating, min_rating)

    if player: 
        max_val = float('-inf')
        for i in range(2): 
            recurr = minimax_alpha_beta_without_magic(depth - 1, max_rating, min_rating, alpha, beta, True)
            max_val = max(max_val, recurr)
            alpha = max(alpha, recurr)
            if alpha >= beta:
                break  
        return max_val

branching = 5
starting_player = int(input(f"Enter who goes first (0 for Light, 1 for L): "))
mind_control= float(input("Enter the cost of using Mind Control:"))
base_Light= int(input("Enter base strength for Light: "))
base_L= int(input("Enter base strength for L : "))

x = minimax_alpha_beta_without_magic(branching, base_Light, base_L, float('-inf'), float('inf'), True)
y = minimax_alpha_beta_with_magic(branching, base_Light, base_L, float('-inf'), float('inf'), True)

print(f"Minimax value without Mind Control: {round(x,2)}")
print(f"Minimax value with Mind Control: {round(y,2)}")
print(f"Minimax value with Mind Control after incurring the cost: {round((y-mind_control),2)}")

if starting_player == 0:
    if x>=0:
        if y-mind_control>=0:
            print(f"Light should NOT use Mind Control as the position is already winning.")
        else:
            print("Light should NOT use Mind Control as it backfires.")
    elif x<0:
        if y-mind_control>=0:
            print(f"Light should use Mind Control as the position is losing.")
        elif (y-mind_control<x):
            print(f"Light should NOT use Mind Control as the position is losing either way.")

elif starting_player == 1:
    if x>=0:
        if y-mind_control>=0:
            print(f"L should NOT use Mind Control as the position is already winning.")
        else:
            print("L should NOT use Mind Control as it backfires.")
    elif x<0:
        if y-mind_control>=0:
            print(f"L should use Mind Control as the position is losing.")
        elif (y-mind_control<x):
            print(f"L should NOT use Mind Control as the position is losing either way.")

