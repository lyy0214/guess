import random    #导入random模块
i = int(input('请输入1个两位整数:'))
j = random.randint(10, 99)
k = 1
while i != j:
    if i < j:
        print('你输入的数字小了，继续加油！')
    else:
        print('你输入的数字大了，继续努力！')
    i = int(input('请输入两位整数:'))
    k = k + 1
else:
    print('你输入的数字正确，你好聪明！')
    print('你一共猜了',k,'次！')
