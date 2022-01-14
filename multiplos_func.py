def cinco_sete(num):
    """[Descobre múltiplos de 5 e de 7]

    Args:
        num ([int]): [numero a ser testado]

    Returns:
        [string]: [FIZZ, FIZZBUZ, BUZZ, MISS]
    """

    if (num % 5 == 0) and (num % 7 == 0):

        res = 'FIZZBUZZ'

    elif num % 5 == 0:
        res = 'FIZZ'

    elif num % 7 == 0:

        res = 'BUZZ'

    else:
        res = 'MISS'
    return res
