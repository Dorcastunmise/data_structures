def romanToInt(s):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    i = 0

    while i < len(s):
        current_value = values[s[i]]

        if i + 1 < len(s):
            next_value = values[s[i + 1]]

            if current_value < next_value:
                total = total - current_value
            else:
                total = total + current_value
        else:
            total = total + current_value

        i = i + 1

    return total
