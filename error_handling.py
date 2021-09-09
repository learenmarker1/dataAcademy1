try:
    10/0

except TypeError:
    print('fel typ')

except ZeroDivisionError:
    print('dela inte med 0')

finally:
    print('skriver alltid detta oavsett')