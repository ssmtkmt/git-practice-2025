def calculate_average(numbers: list) -> float:
    if not numbers:
        return 0.0

    # 合計値を初期化
    total = 0.0

    # リストの各数値を合計値に加算
    for number in numbers:
        total += number

    # 合計値をリストの長さで割って平均値を計算
    return total / len(numbers)
