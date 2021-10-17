import src.constants as const


def add_expressions(first, second, k):
    result = [-1] * k

    for i in range(len(first)):
        if first[i] == second[i] == -1:  # оба -1 -> -1
            pass
        elif first[i] == -1:  # только один = -1 -> берем второй
            result[i] = second[i]
        elif second[i] == -1:
            result[i] = first[i]
        else:  # иначе берем минимум из двух
            result[i] = min(first[i], second[i])
    return result


def concat_expressions(first, second, k):
    new_lengths = set()  # храним возможные длины после конкатенации
    maximum = max(first) + max(second) + 2  # наим точно не достигаемая величина
    result = [maximum] * k

    for i in range(k):
        for j in range(k):  # n = first[i] * k + second[j] * k + i + j  и делим на k
            if first[i] + second[j] + (i + j) // k <= result[(i + j) % k]:  # нашли возможно что-то меньше
                if first[i] == -1 or second[j] == -1:  # одно из двух не оределено
                    continue
                else:
                    index = (i + j) % k
                    result[index] = first[i] + second[j] + (i + j) // k
                    new_lengths.add(index)

    for i in range(k):
        if i not in new_lengths:
            result[i] = -1  # не существующая длина
    return result


def klini_star(expression, k):
    result = expression.copy()
    result[0] = expression[0] = 0  # не забываем про пустое слово

    for i in range(1, k):  # добавление пустого слова уже учтено,
        # нет смысла делать больше чем k конкатенаций, ибо длины слов берём по модулю k
        result = concat_expressions(result, expression, k)

    return result


def get_min_n_to_be_in_expr(expression, k, l):
    stack = []

    for symbol in expression:

        if symbol in const.ALPHABET:
            letter_array = [-1] * k
            if symbol == const.EPSILON:
                letter_array[0] = 0
            else:
                letter_array[1] = 0
            stack.append(letter_array)

        elif symbol in const.OPERATIONS:

            if symbol == const.OR:
                if len(stack) < 2:
                    raise RuntimeError("not enough arguments")

                second = stack.pop()
                first = stack.pop()
                result = add_expressions(first, second, k)
                stack.append(result)

            elif symbol == const.CONCAT:
                if len(stack) < 2:
                    raise RuntimeError("not enough arguments")

                second = stack.pop()
                first = stack.pop()
                result = concat_expressions(first, second, k)
                stack.append(result)
            else:
                if len(stack) == 0:
                    raise RuntimeError("not enough arguments")

                expression = stack.pop()
                result = klini_star(expression, k)
                stack.append(result)

        else:
            raise SyntaxError("invalid syntax")

    if len(stack) != 1:
        raise SyntaxError("incorrect expression form")

    answer_array = stack.pop()
    answer = answer_array[l]
    if answer == -1:
        answer = const.INF
    else:
        answer *= k
        answer += l
    return answer
