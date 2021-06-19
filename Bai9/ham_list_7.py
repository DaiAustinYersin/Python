# Tạo list số và in ra list các số vừa nhập
def in_list(lst):
    print(lst)


# Tính tổng các phần tử trong list
def sum_list(lst):
    return sum(lst)


# Tìm và in ra tất cả các số nguyên tố có trong list
def prime_list(lst):
    prime_lst = []
    for i in lst:
        if i > 1:
            for j in range(2,i+1):
                if i % j == 0:
                    break
                else:
                    prime_lst.append(i)
    return prime_lst


# Tính trung bình cộng của các phần tử dương trong list
def SumAvg_Positive_list(lst):
    tong = 0
    dem = 0
    for i in lst:
        if i > 0:
            tong += i
            dem += 1
    return tong/dem




# Tính trung bình cộng của các phần tử âm trong list
def SumAvg_Negative_list(lst):
    tong = 0
    dem = 0
    for i in lst:
        if i < 0:
            tong += i
            dem += 1
    return tong/dem




# Tìm giá trị chẵn lớn nhất trong list
def max_even_list(lst):
    Max = 0
    for i in lst:
        if i % 2 == 0:
            Max = max(i,Max)
    return Max



# Tìm giá trị lẻ nhỏ nhất trong list
def min_odd_list(lst):
    Min = 100
    for i in lst:
        if i % 2 != 0:
            Min = min(i,Min)
    return Min
