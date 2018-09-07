import random
import sys
import os


print("hello")
name = "Huy"
print(name)
name = 15
print("5+2 =",5+2)
quote = "\"Huy "
multi_line = '''leader team 4 '''
new_string = quote + multi_line
#print(new_string)
print("%s %s %s" % ('  ',quote,multi_line))
# output:
# hello
# Huy
# 5+2 = 7
#    "Huy  leader team 4
# -----------------------------------------------------------
# H_List = ['Huy','Đức','Quân','Hà']
# print('Tên', H_List[0])
# H_List[0]= "dev"
# print("job: ", H_List[0])
# print(H_List[1] + H_List[2])
# list_numer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_name = ['number', 'last number', 'first numer']
# total_list = [list_numer, list_name]
# print( total_list)
# print((total_list[1][2]))
# list_name.append('Huy')# thêm vào vị trí cuối
# list_name.insert(1, "Dz")
# list_name.remove("Huy")#
# list_name.sort()#Ssắp xếp
# list_name.reverse()# đảo ngược
# print(list_name)
# print(len(list_name))
# print(max(list_name))
# print(min(list_name))
# print(max(list_numer))
# print(min(list_numer))
# print(list_name)
# output:
# Tên Huy
# job:  dev
# ĐứcQuân
# [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['number', 'last number', 'first numer']]
# first numer
# ['number', 'last number', 'first numer', 'Dz']
# 4
# number
# Dz
# 10
# 0
# -----------------------------------------------------------------------------
# đếm chuỗi
# pi_tuple = (1, 5, 4, 8, 6, 9, 7, 10)
# new_tuple = list(pi_tuple)
# new_list = tuple(new_tuple)
# a = len(tuple(new_tuple))
# b = max(tuple(new_tuple))
# c = min(tuple(new_tuple))
# print(a, b, c)
# print(new_tuple)
# print(new_list)

# #--------------------------------------------------------------
# the_opposite_number = {1: -1, 2: -2, 3: -3, 4: -4}
# print(the_opposite_number[1])
# del the_opposite_number[1]
# the_opposite_number[5] = -5
# print(the_opposite_number)
# print(len(the_opposite_number))
# print(the_opposite_number.get(5))
# print(the_opposite_number.keys())
# print(the_opposite_number.values())

# # out put:
# #  -1
# # {2: -2, 3: -3, 4: -4, 5: -5}
# # 4
# # -5
# # dict_keys([2, 3, 4, 5])
# # dict_values([-2, -3, -4, -5])

# ----------------------------------------------------------------
# for x in range(0, 10):
#     print(x, '', end="")

# # out put:  0 1 2 3 4 5 6 7 8 9

# print('\n')
# string_list = ['Huy', 'Dz', 'Vãi','Lìn']
# for y in string_list:
# 	 print(y,'', end="")
# # output: Huy Dz Vãi Lìn

# num_list = [[1,2,3],[10,20,30],[100,200,300]]
# for x in range(0,3):
# 	for y in range(0,3):
# 		print(num_list[x][y],'',end = "")
# #output: 1 2 3 10 20 30 100 200 300

# ------------------------------------------------
# random_num = random.randrange(0, 100)
# while(random_num != 9):
#     print(random_num, '', end="")
#     random_num = random.randrange(0, 100)  # important
# out put: 28 80 72 91 54 62 76 78 43 90 20 88 52 11 46 46 52 51 35 5 85 61 98 64 66 2 80 62 72
# 27 73 55 74 92 8 55 34 67 89 55 27 26 99 20 34 34 72 32 42 49 86 53 91 37 54 58 73 63 1 6 85 56 80 27 59 56 60 64 53 93 0 8 70 3 69 60 55 15 37 75 3 57 41 60 38 37 45 54
# 14 83 89 57 83 75 64 79 84 36 50 23 61 81 37 81 29 69 14 58 3 20 39 40 81 77 36 89 86 36 58 99 50 92 23 36 30 42 11 17 36 45 6 53 97 84 4 84 8 86 74 8 67 50 1 7 10 89 50
# 63 19 25 7 4 12 11 47 3 32 74 92 49 6 18 84 75 47 19 27 84 3 11 4 39 21 41 43 79 10 40

# -----------------------------------------------------------------------------------------
# def addnum(a,b):
# 	total = a+b
# 	return total

# print(addnum(1,5))
# #output: 6
# print("Input any num: ")
# num = sys.stdin.readline()
# print(num)

# long_string = " hey fuck your life again"


# print(long_string[0:10])
# print(long_string[0:-5])
# print(long_string[-5:0])

# print(long_string[:-5])
# print(long_string[-5:])

# print(long_string.capitalize())
# print(long_string.isalpha())  # kiểm tra các kỹ tự
# print(long_string.find("hey"))
# print(long_string.replace("hey", ""))
# print(long_string)
# print(long_string.strip())
# quote_list = long_string.split("hey ")
# print(quote_list)
# #output:
# # hey fuck
# #  hey fuck your life

# #  hey fuck your life
# # again
# #  hey fuck your life again
# # False
# # 1
# #   fuck your life again
# #  hey fuck your life again
# # hey fuck your life again
# # [' ', 'fuck your life again']

# ---------------------------------------------------------------
test_file = open("test.txt", "wb")
print("input name: ")
name = sys.stdin.readline()
print(test_file.mode)
print(test_file.name)
test_file.write(bytes(name, 'UTF-8'))
test_file.close()





test_file = open("test.txt", "r+")
text_in_file = test_file.read()
print(text_in_file)
# output
# input name:
# fuck
# wb
# test.txt
# fuck
# -----------------------------------------------------
# Toán tử trong python
# cộng : +
# trừ : -
# nhân: *
# chia: /
# +=: vd: x += y nó sẽ tương đương với phép toán x = x + y
# *=
# /=
# -=
# **: bình phương
# //:Phân chia tầng - Phân chia các toán hạng trong đó kết quả là thương số trong đó các chữ số sau dấu thập phân được loại bỏ.
# Nhưng nếu một trong các toán hạng là số âm, kết quả sẽ được làm tròn, nghĩa là, được làm tròn từ 0 (theo hướng vô cùng âm) -
# vd : 9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0
# Chia toán hạng bên trái bằng toán hạng tay phải và trả về phần còn lại, chia hết
# vd: a % b nếu a chia hết cho b trả về 0 nếu a k chia hết cho b trả về 1
# >: dấu lớn hơn
# <: dấu nhỏ hơn
# >=: lớn hơn hoặc bằng
# <=: nhỏ hơn hoặc bằng
# int : số trong R gồm tất cả các số âm và dương có số 0
# str : chuỗi gồm tất cả các số và chữ và ký tự đặc biệt trong dấu ngoặc đơn hoặc kép
# float : là dãy số gồm cả số thaajp phan trong tap
# print(5 + 2)
# print(5 - 2)
# print(5 * 2)
# print(5 / 2)
# print(5 // 2 )
# print(5 ** 2)
# print(5 == 2)
# print( 5 % 2)
# num = 0.1
# num1 = 1
# num2 = '2'

# print(type(num1))
# print(type(num))
# print(type(num2))
# function type: ép kiểu output: <class 'int'> int là kiểu
# --------------------------------------------------------------

# for  x  in range(0,5):
#     num = int(input("Nhập 1 số : "))
#     if num > 0 :
#         print(" số bạn vừa nhập lớn hơn không và số đó là {}".format(num))
#     elif num < 0 :
#         print(" số bạn vừa nhập nhỏ hơn không và số đó là {}".format(num))
#     elif num == 10 :
#         print(" số bạn vừa nhập là 10")
#     else:
#         print("số bạn vừa nhập là số 0 ")

# print("chương trình kết thúc")
# num = 0
# while(True):
#     num = int(input("Nhập 1 số : "))
#     if num >= 0:
#         print(" số bạn vừa nhập lớn hơn không và số đó là {}".format(num))
#         continue
#     else:
#         break

# print("chương trình kết thúc")

