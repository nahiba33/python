##1.məsələ.................................
# def sqrt_test(list):
#     return [x for x in list if x >= 0 and (x**0.5).is_integer()]
# my_list = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
# print("Result:", sqrt_test(my_list))
##2.məsələ.................................
# def repeat_test(list):
#  repeat=[]
#  return[x for x in list if list.count(x)>1 and x not in repeat] 
# my_list = [-1, 1, 2, 2, 6, 7, 7, 'say', 'say']
# print("Result:", repeat_test(my_list)) 
##3.məsələ.................................
##1.üsul******
# def hasil_func():
#  x = input("Ədədləri boşluq qoyaraq daxil edin:").split()
#  hasil = 1
#  for i in x:
#     hasil *= float(i)
#  print("Girdiyiniz ədədlərin hasili:",hasil )
# hasil_func()
##2.üsul******(bu sanki daha qısa oldu)
# x = input("Ədədlər aralarında boşluq qoyaraq daxil edin: ").split()
# hasil = 1
# for i in map(int, x):
#     hasil *= i
# print("Daxil etdiyiniz ədədlərin hasili:", hasil)
##4.məsələ..................................
# ədəd = int(input("Ədədi daxil edin:"))
# bölənlər = [x for x in range(1, ədəd + 1) if ədəd % x == 0]
# print(bölənlər)
##5.məsələ..................................
# aylar = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "İyun", "İyul", "Avqust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"]
# ay_length = {ay: len(ay) for ay in aylar}
# print(ay_length)
##6.məsələ.....................................
# names_surnames = ["Rich Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# names = [name.split()[0].title().lower() for name in names_surnames ]
# print(names)
##7.məsələ.....................................
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# avarage = [(nums1[i]+nums2[i])/2 for i in range(len(nums1))]
# print("Uyğun dəyişənlərin ədədi ortası:", avarage)
