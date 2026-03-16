def jumlah(arr, n):
    if n == 0:
        return arr[0]
    return arr[n] + jumlah(arr, n-1)

def rText(s):
    if len(s) <= 1:
        return s
    return rText (s[1:]) + s[0]

if __name__ == '__main__':
    data = [5, 4, 8, 2, 9, 4, 7]
    hsl = jumlah(data, 6)
    print("Jumlah Total Nilai dalam Array: "+str(hsl) )

    dta = "Jakarta"
    hsl = rText(dta)
    print("Hasil Reverse Text: "+ hsl)