"""
This is a gambling simulator that aim at analyse different strategy while doing gamble.
"""

import random as r
"""
winningProbability: Winning probability in a game.
gamblingTimes: How many rounds should it play.
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

def play(rounds, winProbability, strategy, initBet, balance):
    i = 0
    lost = 0
    bet = strategy(initBet, True, 0, balance)
    balances = [balance]
    assert bet <= balance , "Cannot bet more than your balance"
    while([i < rounds, True][rounds == 0] and balance > 0):
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

def getMean(list):
    return sum(list)/len(list)

def getVariance(list):
    mean = getMean(list)
    v = []
    for i in list:
        v += [pow(i - mean, 2)]
    return sum(v)/len(list)

def getNominalDistribution(list):
    dis = {}
    for i in list:
        if(i not in dis):
            dis[i] = 1
        else:
            dis[i] += 1
    return dis

def getLoseRounds(rounds, winProbability, strategy, initBet, balance):
    ltime = []
    for i in range(rounds):
        ltime += [play(0, winProbability, strategy, initBet, balance)[0]]
    return ltime

def getAverageLoseRound(rounds, winProbability, strategy, initBet, balance):
    return getLoseRounds(rounds, winProbability, strategy, initBet, balance) / rounds

def getMaximumBalances(rounds, winProbability, strategy, initBet, balance):
    maxBalances = []
    for i in range(rounds):
        maxBalances += [getMaximumBalance(play(rounds, winProbability, strategy, initBet, balance)[2])]
    return maxBalances

def getAverageMaximumBalance(rounds, winProbability, strategy, initBet, balance):
    return getMaximumBalances(rounds, winProbability, strategy, initBet, balance) / rounds

def getMaximumBalance(balances):
    return max(balances)

def getMaximumRatio(balances, initBalance):
    return max(balances) / initBalance
    
def analyseRatioAndBalance(winProbability, strategy, begin, stepping, numberOfSteps, rounds = 100000):
    ratios = {}
    balance = begin
    for i in range(numberOfSteps):
        ratios[balance] = getAverageMaximumBalance(rounds, winProbability, strategy, 100, balance) / balance
        balance *= stepping
    return ratios

def writeListToCsv(data, path, x = "Time", y = "Balance"):
    fp = open(path, "w+")
    fp.write(x + "," + y + "\n")
    for i in range(len(data)):
        fp.write(str(i + 1) + "," + str(data[i]) + "\n")
    fp.close()

def writeDictionaryToCsv(data, path, x = "Round", y = "Time"):
    fp = open(path, "w+")
    fp.write(x + "," + y + "\n")
    for i in data:
        fp.write(str(i) + "," + str(str(data[i])) + "\n")
    fp.close()
