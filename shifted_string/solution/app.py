def is_shifted(a, b):
    b = list(b)
    for i in a:
        try:
            position = b.index(i)
        except:
            return False
        b.pop(position)
    return True

  
print(is_shifted('abcde', 'cdeab'))
# True