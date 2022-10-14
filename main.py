def _min(array):
    min_val = array[0]
    for i in range(1, len(array)):
        if array[i] < min_val:
            min_val = array[i]
    return min_val


def _mult(array):
    _mult = array[0]
    for i in range(1, len(array)):
        _mult = _mult * array[i]
    return _mult


if __name__ == '__main__':
    with open(input('Напишите название файла: '), 'r', encoding='utf-8') as file:
        array = list(map(int, file.readline().split()))

    # Альтернативный вариант чтения файла
    # array = [int(i) for i in open('file.txt').readline().split()]

    print('Результат работы _min', _min(array))
    print('Результат работы _mult', _mult(array))



