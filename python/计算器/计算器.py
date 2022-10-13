def mo(x,y,m):
    # 数学运算处理函数（mo 是 Mathematical operations 的缩写）
    if m == 1:
        return x + y
    elif m == 2:
        return x - y
    elif m == 3:
        return x * y
    elif m == 4:
        return x / y
    elif m == 5:
        return x ** y

def go(x,y,m):
    # 图形运算处理函数（go 是 Graphical calculations 的缩写）
    if 1 == 1:
        pass

mode = int(input("选择模式\n1：加法计算\n2：减法计算\n3：乘法计算\n4：除法计算\n5：幂运算\n6：图形运算\n请输入序号："))
if mode == 1:
    num_1 = input("请输入加数 1：")
    num_2 = input("请输入加数 2：")
    da = mo(eval(num_1),eval(num_2),mode)
    print(num_1,"+",num_2,"=",da)
elif mode == 2:
    num_1 = input("请输入被减数：")
    num_2 = input("请输入减数：")
    da = mo(eval(num_1),eval(num_2),mode)
    print(num_1,"-",num_2,"=",da)
elif mode == 3:
    num_1 = input("请输入乘数 1：")
    num_2 = input("请输入乘数 2：")
    da = mo(eval(num_1),eval(num_2),mode)
    print(num_1,"×",num_2,"=",da)
elif mode == 4:
    num_1 = input("请输入被除数：")
    num_2 = input("请输入除数：")
    da = mo(eval(num_1),eval(num_2),mode)
    print(num_1,"÷",num_2,"=",da)
elif mode == 5:
    num_1 = input("请输入一个数字：")
    num_2 = input("请输入你要求出上面数字的几次幂：")
    da = mo(eval(num_1),eval(num_2),mode)
    print(num_1,"的",num_2,"次幂是：",da)
elif mode == 6:
    print("已进入图形运算模式。")
    gmode = int(input("请选择计算类型：\n1：长方形计算\n2：正方形计算\n3：梯形计算\n4：长方体计算\n5：正方体计算\n6：圆计算\n请输入序号："))
    if 1 == 1:
        print("我才不会告诉你我没写完呢")
