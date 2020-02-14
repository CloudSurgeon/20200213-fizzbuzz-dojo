def fizzbuzz(x, foo={3: 'fizz', 5: 'buzz'}):
    result = ''.join(
        word
        for divisor, word in foo.items()
        if x % divisor == 0
    )
    return result or x
