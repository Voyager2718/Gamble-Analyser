"""
This is a gambling simulator that aim at analyse different strategy while doing gamble.
"""

import random as r
"""
winningProbability: Winning probability in a game.
gamblingTimes: How many times should it play.
"""
winningProbability = 0.49
gamblingTimes = 0

def strategy1(initBet, won, numberOfLosing, balance):
    assert type(initBet) == int , "variable initBet should be int"
    assert type(won) == bool , "variable won should be bool"
    assert type(numberOfLosing) == int , "variable numberOfLosing should be int"
    assert type(balance) == int , "variable balance should be int"
    if(not won):
        return [int(initBet * pow(2, numberOfLosing)), balance][int(initBet * pow(2, numberOfLosing)) > balance]
    return [balance, initBet][balance>initBet]


def roll(winProbability):
    return winProbability > r.random()

def play(times, winProbability, strategy, initBet, balance):
    i = 0
    lost = 0
    bet = strategy(initBet, True, 0, balance)
    balances = [balance]
    assert bet <= balance , "Cannot bet more than your balance"
    while([i < times, True][times == 0] and balance > 0):
        i += 1
        result = roll(winProbability)
        if(not result):
            balance -= bet
            lost += 1
            bet = strategy(initBet, False, lost, balance)
        else:
            balance += bet
            lost = 0
            bet = strategy(initBet, True, lost, balance)
        balances += [balance]
    return (i, balance, balances)

def multiPlay(times, winProbability, strategy, initBet, balance):
    loseAt = 0
    for i in range(times):
        loseAt += play(times, winProbability, strategy, initBet, balance)
    return loseAt / times

def getMaximumBalance(balances):
    return max(balances)

def getMaximumRatio(balances, initBalance):
    return max(balances) / initBalance
    
def analyseRatioAndBalance(winProbability, strategy, begin, stepping, numberOfSteps, numberOfSamples = 100000):
    bal = begin
    ratios = []
    r = 0.0
    for i in range(numberOfSteps):
        for j in range(numberOfSamples):
            r += getMaximumRatio(play(0, winProbability, strategy, 100, bal)[2], bal)
        ratios += [r / bal]
        bal *= stepping
    ret = []
    bal = begin
    for i in range(len(ratios)):
        ret += [[bal, ratios[i]]]
        bal *= stepping
    return ret

def outputOnePlayToCSV(data, path, x = "time", y = "balance"):
    fp = open(path, "w+")
    fp.write(x + "," + y + "\n")
    for i in range(len(data)):
        fp.write(str(i + 1) + "," + str(data[i]) + "\n")
    fp.close()