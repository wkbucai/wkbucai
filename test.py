def calculate_average(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list.")
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("All elements in the list must be numbers.")
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    return total / count


def main():
    # 示例使用
    numbers = [10, '20', 30, 40, 50]  # 包含非数字值
    average = calculate_average(numbers)
    print("The average is: ", average)


if __name__ == "__main__":
    main()
