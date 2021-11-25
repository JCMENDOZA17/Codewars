def tower_builder(n_floors):
    caja = []
    for i in range(1, n_floors + 1):
        caja.append(' '*(n_floors - i) + '*' * (2 * i - 1) + ' '*(n_floors - i))
    return caja





if __name__ == '__main__':
    assert tower_builder(1) == ['*', ]
    assert tower_builder(3) == ['  *  ', ' *** ', '*****']
    assert tower_builder(2) == [' * ', '***']
    
44 = 0, 1, 1, 2, 3, 5, 8 , 13, 21, 34
5 = 0, 1, 1, 2, 5