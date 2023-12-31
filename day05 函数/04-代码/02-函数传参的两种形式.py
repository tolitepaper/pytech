def func(a, b, c):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")


# 位置传参, 按照形参的位置顺序将实参的值传递给形参
func(1, 2, 3)
# func(3, 1, 2)
# 关键字传参,指定实参给到哪个形参, 注意点: 关键字必须是函数的形参名
func(a=10, b=20, c=30)
# func(c=10, a=20, b=30)
# 混合使用, 先写位置传参,再写关键字传参
# func(10, b=20, c=30)
# func(a=10, 20, 30)  # 代码会报错
# func(10, a=30, b=20)  # 代码会报错


