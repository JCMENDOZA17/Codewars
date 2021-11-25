def duplicate_encode(word):
    palabra = word.lower() # convierte el valor de la entrada en minusculas y lo guarda en una nueva variable
    encoder = {} # crea un diccionario vacío

    for chacter in palabra:
        if chacter in encoder: # si el caracter esta dentro del diccionario  
            encoder[chacter] = ')' # el valor de cada key será ')'
        else:
            encoder[chacter] = '(' # si no el valor será '('
    return ''.join([encoder[chacter] for chacter in palabra]) 
 
        




if __name__ == '__main__':
    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())","should ignore case"
    assert duplicate_encode("(( @") == "))(("