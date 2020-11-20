satuan = ['', 'one', 'two', 'three', 'four','five', 'six', 'seven', 'eight', 'nine']


def terbilang(n):
    # mencari koma
    if n % 1 > 0 :
        angka = str(n)
        koma = angka.find('.')
        depan = int(angka[:koma])
        belakang = int(angka[koma+1:])
        if '.' not in angka :
            return terbilang(depan)
        elif '.' in angka :
            return terbilang(depan) + ' coma ' + terbilang(belakang)
    elif n < 10:
        # satuan
        return satuan[n]
    elif n >= 1_000_000_000:
        # milyar
        return terbilang(n // 1_000_000_000) + ' billion ' + 'and ' + terbilang(n % 1_000_000_000) 
    elif n >= 1_000_000:
        # juta
        return terbilang(n // 1_000_000) + ' million' + ' and ' + terbilang(n % 1_000_000) 
    elif n >= 1_000:
        #ribuan
        return terbilang(n // 1000) + ' thousand ' + 'and ' + terbilang(n % 1000)         
    elif n >= 100:
        # ratusan
        return terbilang(n // 100) + ' hundred ' + terbilang(n % 100) 
    elif n >= 20:
        # puluhan
        if n // 10 == 2 :
            return "twenty " + terbilang(n%10)
        elif n // 10 == 3 :
            return "thirty " + terbilang(n%10)
        elif n // 10 == 4 :
            return "forty " + terbilang(n%10)
        elif n // 10 == 5 :
            return "fifty " + terbilang(n%10)
        else :
            return terbilang(n//10) + 'ty ' + terbilang(n%10) 
    else:
        # belasan
        if n == 10:
            return ' ten'
        elif n == 11:
            return ' eleven'
        elif n == 12:
            return ' twelve'
        elif n == 13:
            return ' thirteen'
        elif n == 14:
            return ' forteen'
        elif n == 15:
            return ' fifteen'
        else:
            return terbilang(n % 10) + 'teen' 
    
    
# test
n = 18
print(f'{n:,} = {terbilang(n)}')