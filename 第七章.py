import turtle as t
t.title("自动会之轨迹")
t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)

# 数据读取
datasets = []
f = open("data.txt")
for line in f:
    line = line.replace("\n", "")
    datasets.append(list(map(eval, line.split(","))))
# map函数的功能将第一个参数的功能作用于每一个元素 eval评估函数将字符串两边冒号去掉
f.close()
# 自动绘制
for i in range(len(datasets)):
    t.pencolor(datasets[i][3], datasets[i][4], datasets[i][5])
    t.fd(datasets[i][0])
    if datasets[i][0]:
        t.right(datasets[i][2])
    else:
        t.left(datasets[i][2])
