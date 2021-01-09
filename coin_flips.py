# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"

def coin_flips(n):
    # Write code here
    if n < 1:
        return ('Coin must be flipped at least 1 time')
    elif n == 1:
        outcomes = ['H', 'T']
        return outcomes
    else:
        possible_outcomes = ['H', 'T']
        outcomes = []
        for i in possible_outcomes:
            for outcome in coin_flips(n - 1):
                outcomes.append(i + outcome)
        return outcomes

print(coin_flips(2)) 
# => ["HH", "HT", "TH", "TT"]

print(coin_flips(3)) 