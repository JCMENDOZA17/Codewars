def permute_a_palindrome(word): # definimos la función y le asignamos un input llamado "word"
    odd_char_count = 0 # creamos una variable y le asignamos un valor
    
    for chara in word: # para "chara" en el input word del inicio
        if word.count(chara) % 2 == 0: # si al contar el input de "chara" dividido entre 2 nos da 0
            continue # continuamos el algoritmo
        elif word.count(chara) % 2 != 0 and word.count(chara) == 1: # si al contar el input de "chara" entre 2 nos es igual a 0 y es 1
            odd_char_count += 1 # la varible es mayor o igual a 1
            if odd_char_count == 1: # si la variable es igual a 1
                continue # continuamos el algoritmo
            else: #sino
                return False #devuelve falso
        else: #sino
            return False #devuelve falso
    return True #devuelve verdadero

print(permute_a_palindrome("aba"))