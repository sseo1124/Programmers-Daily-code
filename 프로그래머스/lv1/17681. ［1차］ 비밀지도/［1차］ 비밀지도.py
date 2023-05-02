def solution(n, arr1, arr2):
    result = []
    for i, j in zip(arr1, arr2):
        bi_array1 = int(bin(i)[2:])
        bi_array2 = int(bin(j)[2:])
        path = ''
        sum_element = bi_array1 + bi_array2
        for l, c in enumerate(str(sum_element)):
            if int(c) >= 1:
                path += '#'
                
            elif int(c) == 0:
                path += ' '
      
        if (l+1) < n:
            path = ' '*(n - (l + 1)) + path
            result.append(path)
        else:
            result.append(path)
    return result