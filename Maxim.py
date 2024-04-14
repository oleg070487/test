import random
from decimal import Decimal


def check_number(number):
    """Функция для добавления цифры в конец числа если число не имеет 2 цифры после запятой,
    это происходит потому что сгенерированное число может иметь только одну цифру после запятой или не имеет вовсе цифр
    после запятой """
    if len(str(number)[str(number).find('.')+1:]) < 2 or str(number).find('.') == -1:
        return Decimal(number) + Decimal(0.01)
    else:
        return Decimal(number)


def generates_numbers_is_no_trend(fr_t, to_t, num_of_nums):
    """Функция генерирует числа с двумя запятыми после запятой
    в заданном пользователем диапазоне БЕЗ какого то тренда и возвращает список этих чисел"""
    lst_of_generates_numbers = []
    for _ in range(num_of_nums):
        number_generated = round(random.uniform(fr_t, to_t), 2)
        lst_of_generates_numbers.append(check_number(number_generated))
    return lst_of_generates_numbers


def divide_into_subranges(fr_t, to_t, n_subranges):
    """ Функция делит диапазон температур на 'N' равных диапазонов(поддиапазонов) чтобы в
    последствии создать видимость тренда на снижения или повышения температур в общей картине
    и возвращает список из кортежей с поддиапазонами"""
    step = (to_t - fr_t) / n_subranges
    lst_subranges = [(fr_t + step * n, (fr_t + step * n) + step) for n in range(n_subranges)]
    return lst_subranges


def generates_numbers_is_a_trend(fr_t, to_t, num_of_nums, n_subrages):
    """Функция возвращает список рандомных чисел из температур для создания картины какого либо тренда"""
    lst_temporary = []
    lst_final_of_generates_numbers = []
    lst_sub = divide_into_subranges(fr_t, to_t, n_subrages)

    for fr, to in lst_sub:
        lst_temporary.extend(generates_numbers_is_no_trend(fr, to, num_of_nums // n_subrages))
    if (num_of_nums // n_subrages) * n_subrages == num_of_nums:
        lst_final_of_generates_numbers = lst_temporary
    else:
        for _ in range(num_of_nums - ((num_of_nums // n_subrages) * n_subrages)):
            lst_final_of_generates_numbers.append(round(random.uniform(*lst_sub[0]), 2))
        lst_final_of_generates_numbers += lst_temporary
    return lst_final_of_generates_numbers


def main(fr_t, to_t, num_of_nums, trend, n_subrages):
    """Основная функция для создания списков температур уже с учетом тренда типа тренда или без тренда вовсе
     в зависимости от ввода пользователем"""
    if trend == '+':
        return generates_numbers_is_a_trend(fr_t, to_t, num_of_nums, n_subrages)
    elif trend == '-':
        return generates_numbers_is_a_trend(fr_t, to_t, num_of_nums, n_subrages)[::-1]
    elif trend == 'no':
        return generates_numbers_is_no_trend(fr_t, to_t, num_of_nums)


if __name__ == "__main__":

    from_temp, to_temp = list(
        map(int, input('Введите диапазон температур, два числа через пробел от меньшего к большому: ').strip().split()))
    number_of_numbers_generated = int(input('Введите требуемое количество сгенерированных чисел: '))
    trend_type = input('Введите тренд, если на понижения то "-", на повышение "+", если без тренда тогда "no": ')
    number_of_subranges = None
    if trend_type != 'no':
        number_of_subranges = int(input('Введите число для регулирования качества тренда '
                                        'в зависимости от количества всех сгенерируемых чисел и '
                                        'другой необходимости например число - 4: '))
    number_of_repeat_program = int(input('Введите количество датчиков: '))

    lst_of_all_lst_generated = []
    for x in range(number_of_repeat_program):
        lst_temp = main(from_temp, to_temp, number_of_numbers_generated, trend_type, number_of_subranges)
        lst_of_all_lst_generated.append(lst_temp)

    result_of_zip = list(zip(*lst_of_all_lst_generated))

    with open('random.xls', 'w') as file:
        file.write("Случайные вещественные числа в заданном диапазоне:" + '\n\n')
        for tp in result_of_zip:
            for el in tp:
                el_str = str(el).replace('.', ',') + '\t'
                file.write(f'{el_str}')
            file.write('\n')
