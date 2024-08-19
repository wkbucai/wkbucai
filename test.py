def calculate_average(numbers):
    if not numbers:  # 检查列表是否为空
        return 0
    return sum(numbers) / len(numbers)


def main():
    # 示例使用
    numbers = [10, '20', 30, 40, 50]  # 包含非数字值
    average = calculate_average(numbers)
    print("The average is: ", average)


if __name__ == "__main__":
    main()
