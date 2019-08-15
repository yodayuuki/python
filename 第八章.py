import random


def printIntro():
    print("这个程序模拟两个选手AB的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")


def getInputs():
    a = eval(input("请输入选手A的能力值：(0-1)"))
    b = eval(input("请输入选手B的能力值：(0-1)"))
    n = eval(input("模拟比赛场次"))
    return a, b, n


def printSummary(winsA, winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:.2%}".format(winsA, winsA/n))
    print("选手B获胜{}场比赛，占比{:.2%}".format(winsB, winsB/n))

def gameOver(a, b):
    return  a==15 or b ==15

def simOneGame(probA, proB):
    scoreA , scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random.random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random.random() < proB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB


def simNgames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNgames(n, probA, probB)
    printSummary(winsA, winsB)
main()




