def first_missing_positive_intiger_sorted(integers):
    size = len(arr)
    sumofSize = (size * (size + 1))/2
    sumofArr = sum(arr)
    print(int(sumofSize - sumofArr))