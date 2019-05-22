import random
number = random.randint(1,100)
print('------猜数字游戏！-----')
guess = 0
sum=0
while guess != number:
    temp = input('请输入数字：\n')
    guess = int(temp)
    if guess > number:
        print('您输入的数字大了！')
    elif guess < number:
        print('您输入的数字小了！')
    else :
        print('恭喜，您猜对了！')
        print('游戏结束，再见！^_^')
    sum=sum+1
print(sum)