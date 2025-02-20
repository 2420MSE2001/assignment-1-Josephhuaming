def horner_method(coefficients, x):
    #输入区

    result = 0.0
    n = len(coefficients)
    for i in range(n):
        result += coefficients[i] * (x ** (n-1-i))

    return result

if __name__ == "__main__":
    # 读取输入：第一行为 x0，第二行为多项式系数（从高次到低次排列）
    x0 = float(input().strip())
    coefficients = list(map(float, input().split()))
    
    # 计算并输出结果
    print(horner_method(coefficients, x0))
