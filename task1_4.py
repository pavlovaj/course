S = input("Введите строку:")


def IsPalindrome(S):
    if len(S) <= 1:
        return True
    else:
        return S[0] == S[-1] and IsPalindrome(S[1:-1])


print(IsPalindrome(S))