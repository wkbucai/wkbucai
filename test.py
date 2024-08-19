def calculate_average(numbers):
    # 忽略了输入类型检查
    total = sum(numbers)  # 没有处理可能的非数字值
    count = len(numbers)

    # 忽略了除以零的情况
    return total / count


def main():
    # 示例使用
    numbers = [10, '20', 30, 40, 50]  # 包含非数字值
    average = calculate_average(numbers)
    print("The average is: ", average)


if __name__ == "__main__":
    main()
