def list_elements(numb):
    list_tot = []
    for i in range(numb):
        list_tot.append(i+1)
    return list_tot
def sort(amount):
    a = list_elements(amount)
    for i in range(0, len(a) - 1):
        m = max(a[i:])
        ind = a.index(m)
        a[i], a[ind] = a[ind], a[i]
    print(a)
