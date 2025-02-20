# main.py

def left_side(x, num_terms):
    """
    计算方程左侧前 num_terms 项的和。
    """
    result = 0.0


    for i in range(num_terms):
        result += float((2**i * x**(2 ** i - 1) - 2**(i+1) * x**(2 ** (i + 1) - 1)) / (1 - x ** (2 ** i) + x ** (2 ** (i + 1))))

    return result

def right_side(x):
    """
    计算方程右侧的固定值。
    """


    result = float((1+2*x)/(1+x+x**2))

    return result

def find_num_terms(x, tolerance=1e-6):
    """
    寻找满足左侧与右侧差异小于容差的最小项数。
    """
    
    num_terms = 1
    while(abs(left_side(x,num_terms) - right_side(x)) > tolerance):
        print(left_side(x,num_terms))
        num_terms += 1
    


    return num_terms

if __name__ == "__main__":
    x = 0.25  # 题目给定的 x 值
    num_terms = find_num_terms(x)
    print(f"所需最小项数: {num_terms}")
