satuan = ['', 'satu', 'dua', 'tiga', 'empat','lima', 'enam', 'tujuh', 'delapan', 'sembilan']


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
            return terbilang(depan) + ' koma ' + terbilang(belakang)
    elif n < 10:
        # satuan
        return satuan[n]
    elif n >= 1_000_000_000:
        # milyar
        return terbilang(n // 1_000_000_000) + ' milyar ' + terbilang(n % 1_000_000_000) 
    elif n >= 1_000_000:
        # juta
        return terbilang(n // 1_000_000) + ' juta ' + terbilang(n % 1_000_000) 
    elif n >= 1000:
        #ribuan
        if n // 1000 == 1:
            return " seribu " + terbilang(n % 1000) 
        else:
            return terbilang(n // 1000) + ' ribu ' + terbilang(n % 1000)         
    elif n >= 100:
        # ratusan
        if n // 100 == 1:
            return " seratus " + terbilang(n % 100) 
        else:
            return terbilang(n // 100) + ' ratus ' + terbilang(n % 100) 
    elif n >= 20:
        # puluhan
        return terbilang(n // 10) + ' puluh ' + terbilang(n % 10) 
    else:
        # belasan
        if n == 10:
            return ' sepuluh'
        elif n == 11:
            return ' sebelas'
        else:
            return terbilang(n % 10) + ' belas'

    
    
# test
n = 11000
print(f'{n:,} = {terbilang(n)}')