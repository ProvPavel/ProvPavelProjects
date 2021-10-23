from yandex_testing_lesson import is_palindrome


f = 1
if is_palindrome('jkgfvkv') is True:
    f = 0
if is_palindrome('qwertrewq') is False:
    f = 0
if is_palindrome('') is False:
    f = 0
if is_palindrome('a') is False:
    f = 0
if is_palindrome('aaaaaa') is False:
    f = 0
if f:
    print('YES')
else:
    print('NO')
