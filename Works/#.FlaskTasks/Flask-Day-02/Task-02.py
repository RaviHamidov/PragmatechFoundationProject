from tkinter import *

#     - Əsas menu (ready)
#         - Qeydiyyatdan keç (ready)
#             - Ad (doldurulması zəruridir)
#             - Soyad (doldurulması zəruridir)
#             - Email (doldurulması zəruridir)
#                 - Email olub olmaması yoxlanılmalıdır. Əks halda error mesajı çıxmalıdır ekrana
#             - Telefon (doldurulması zəruri deyil) (ready)
#                 - Sadəcə rəqəmlər daxil edilə bilməlidir. Əks halda error mesajı verilməlidir.
#                 - +994 ifadəsi aftamatik olaraq yazılmalıdır telefon nömrəsinin önünə. 
#                 - Telefon nömrəsi sadəcə Azərbaycan GSM şirkətlərinin prefixləri ilə daxil edilməlidir (55,50 və s)
#                 - Daxil edilən rəqəm sayı 7-dən yuxarı ola bilməz
#             - Password (ready)
#                 - Minimum 8 xarakterdən ibarət olmalıdır
#                 - Daxilində mütləq minium 2 kiçik və 1 böyük hərf olmalıdır
#                 - Minimum 1 ədəd rəqəm olmalıdır
#             - Qisa məlumat (ready)
#         - Daxil ol (ready)
#             - istifadəçi email və passwordunu daxil edir (ready)
#                 - üç dəfə səhv məlumat daxil edildiyi zaman qeydiyyat bölməsinə yönləndirmə edilməlidir
#             - Bu məlumatlara uyğun istifadəçi varsa (ready)
#                 - istifadəçi haqqında olan bütün məlumatlar ekranda görünməlidir
#                 - ESC düyməsinə basanda profildən çıxın əsas menuye qayıtmalıdır
#         - ESC düyməsinə basılanda proqramdan çıxmalıdır (ready)