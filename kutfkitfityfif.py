def stubbornness(*data):

    res = []
    for i in data:
        if len(i) >= 2:
            q1 = int(i[0])
            m = list(map(lambda x: int(x), i[1::]))
            q2 = max(m)
            q3 = min(m)
            if 0 == q2 or 0 == q3:
                raise ZeroDivisionError('Cannot be divided by zero')
            else:
                if (q1 % q2 == 0) and (q1 % q2 == 0):
                    res.append(q1)
        else:
            raise NotEnoughError('Not enough values')
    if res:
        res.sort()
        return res
    raise IndexError('Empty Return Error')


class NotEnoughError(Exception):
    pass
