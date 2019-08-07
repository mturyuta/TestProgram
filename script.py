from testclass import Menu_dis
import datetime
today1 = datetime.date.today()
today2 = "{0:%Y%m%d}".format(today1)

menu0 = Menu_dis("カロリータンパク質入力")
menu1 = Menu_dis("カロリータンパク質確認")
menu2 = Menu_dis("必要なカロリー、タンパク質計算(リーンバルク)")
menu3 = Menu_dis("一日に必要なカロリータンパク質の設定")

menus = [menu0, menu1, menu2, menu3]
index = 0
print("---------------------------------")
for menu in menus:
    print(str(index) + "." + menu.info())
    index += 1
print("---------------------------------")




first_dis = int(input ("選んでください 0~4:"))


if first_dis == 0:
    second_dis_0 = int(input("0.当日 1. 別日 :"))

    while second_dis_0 == 0:
        today_cal = input("摂取カロリーを入力してください")
        today_pro = input("摂取タンパク質を入力してください")
        file = open(str(today2),"a")
        string_list = [today_cal, " ", today_pro,"\n"]
        file.writelines(string_list)
        second_dis_0 = int(input("追加書き込みしますか？Y/0 N/2:"))
        if second_dis_0 != 0:
            file.close()
            print (str(today2) + "の書き込みを終了します")


    if second_dis_0 == 1:
        second_dis_0 = 0
        while second_dis_0 == 0:
            the_day = int(input("日付を入力してください　(例20191102):"))
            the_day_cal = input("摂取カロリーを入力してください")
            the_day_pro = input("摂取タンパク質を入力してください")
            file = open(str(the_day),"a")
            string_list = [the_day_cal, " ", the_day_pro,"\n"]
            file.writelines(string_list)
            second_dis_0 = int(input("追加書き込みしますか？Y/0 N/1:"))
            if second_dis_0 != 0:
                file.close()
                print (str(the_day) + "の書き込みを終了します")


elif first_dis == 1:
    second_dis_1 = int(input("0.当日 1.別日 :"))

    if second_dis_1 == 0:
        total_cal = 0
        total_pro = 0
        for line in open(str(today2), "r"):
            data = line.split()
            total_cal += int(data[0])
            total_pro += int(data[1])
        print (str(total_cal) + "kcal " + str(total_pro) + "g")

    else:
        the_day = int(input("日付を入力してください(例20191102):"))
        total_cal = 0
        total_pro = 0
        for line in open(str(the_day), "r"):
            data = line.split()
            total_cal += int(data[0])
            total_pro += int(data[1])
        print (str(total_cal) + "kcal " + str(total_pro) + "g")

elif first_dis == 2:
    proc = 2
