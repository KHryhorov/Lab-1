def list_elements(numb):
    list_tot = []
    for i in range(numb):
        list_tot.append(i+1)
    return list_tot
def sort(amount):
    a = list_elements(amount)
    for i in range(0, len(a)-1):
        for j in range(0, len(a)-1-i):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
sort()