def quicksort(data):
    index = len(data)

    if index <=1:
        return data
    else:
        pivot = data.pop()

    data_kiri = []
    data_kanan = []

    for i in data :
        if i < pivot :
            data_kiri.append(i)
        else :
            data_kanan.append(i)
    
    return quicksort(data_kiri) + [pivot] + quicksort(data_kanan)

data = [9,-3,5,2,6,8,-6,1,3]
print("Data Awal (Urutan Acak):",data)

data_hasil = quicksort(data)
print("Data Urut Secara Quicksort :",data_hasil)