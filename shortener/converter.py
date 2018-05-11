class Converter:
    """
    Use bijective numeration to convert positive integer to short strings
    and vice versa
    """
    def __init__(self, alphabet):
        self._alphabet = alphabet
        self._base = len(self._alphabet)

    def shorten(self, num):
        # basic type check since python is dynamically typed
        if not isinstance(num, int):
            raise TypeError('attribute must be positive integer')
        string = ''
        while num > 0:
            string = self._alphabet[num % self._base] + string
            num //= self._base
        return string

    def decipher(self, short_string):
        # basic type check since python is dynamically typed
        if not isinstance(short_string, str):
            raise TypeError('attribute must be string')
        num = 0
        for character in short_string:
            num = num * self._base + self._alphabet.index(character)
        return num
