from yandex_testing_lesson import is_prime


f = 1
if is_prime(1) is True:
    f = 0
if is_prime(19) is False:
    f = 0
if is_prime(0) is True:
    f = 0
if is_prime(13) is False:
    f = 0
if is_prime(100) is True:
    f = 0
if f:
    print('YES')
else:
    print('NO')
