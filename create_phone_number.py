def create_phone(number):
    assert isinstance(number, list) # comprobar que es una lista
    nums = ''.join(map(str, number)) # transforma   
    telf = "({}) {}-{}".format(nums[0:3],nums[3:6],nums[6:]) # reemplaza lo que se ponga dentro del format en las {} por orden
    return telf # devuelve la variable




if __name__ == '__main__':
    assert create_phone([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890" 
    assert create_phone([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111"   
    