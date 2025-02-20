# main.py

def calculate_sum():
    sum = 0
    for i in range (51):
        sum = sum + i
    return sum


if __name__ == "__main__":
    result = calculate_sum()
    print(f"1+2+...+50的和是：{result}")
