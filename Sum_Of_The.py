def SumOfThe(N,data):
    x = 0
    for i in range(N):
        data2 = []
        summ = 0
        for j in range(N):
            data2.append(data[j])
        data2.remove(data[i])
        for k in range(len(data2)):
            summ += data2[k]
        if data[i] == summ:
            x = data[i]
    return x
        
        

N = 5
data = [10, -25, -45, -35, 5]
print(SumOfThe(N,data))
