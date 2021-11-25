def duplicate_count(text):
    low_text = text.lower()
    sumador = {} # diccionario vacio
    for cont in low_text:
        if sumador.get(cont) is None: #si el valor del caracter en la lista es "ninguno o no existe"
            sumador[cont] = 0 # le agregamos un 0 al valor del caracter
        else:
            sumador[cont] = 1 # si no es así, es decir si ya tiene un valor asignado le agregamos 1
    return sum(sumador.values()) # devolvemos la suma total de los valores del diccionario

# solución codewars:
    
def duplicate_count(text):
    s = text.lower()
    case = ''
    count = 0
    for letter in s:
        if s.count(letter) > 1 and (not(letter in case)):
            count += 1
            case += letter
    return count




if __name__ == '__main__':
    assert duplicate_count("abcdeaa") == 1
    assert duplicate_count("abcde") == 0
    assert duplicate_count("abcdeaB") == 2
    assert duplicate_count("Indivisibilities") == 2
    assert duplicate_count("") == 0