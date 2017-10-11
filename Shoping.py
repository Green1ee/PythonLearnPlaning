#! /usr/bin/env python
# -*- coding: utf-8 -*-

__Author__ = "GreenLee"
shoping_path = "shoping.list"
welcome = "欢迎下次光临！"
str_exit = "，退出输入Q"
str_error = "输入错误，请重新输入！"
bill = []
open(shoping_path,"a").close()                                      #开始操作文件之前，先以a模式打开一次文件，以确保文件存在
with open(shoping_path, "r", encoding="utf-8") as shoping_list :
    list = shoping_list.readlines()
if len(list) <= 0 :
    with open(shoping_path, "w", encoding="utf-8") as shoping_list:
        shoping_list.writelines(["Pen 50\n","Pencil 2\n", "Mouse 20\n", "Book 5\n"])
while True:
    user_role = input("商家输入A，客户输入B%s："%str_exit)
    if user_role == "A" :
        print("欢迎您，商家！您的商品库存情况如下：")
        break
    elif user_role == "B":
        _user_balance = input("欢迎您，亲爱的顾客！请输入您的余额%s："%str_exit)
        if _user_balance == "Q":
            print(welcome)
            exit(0)
        else:
            try:
                user_balance = float(_user_balance)
            except:
                print(str_error)
                continue
        break
    elif user_role == "Q":
        print(welcome)
        exit(0)
    else:
        print(str_error)
with open(shoping_path, "r", encoding="utf-8") as shoping_list:
    list = shoping_list.readlines()
while True:
    #将商品列表展示出来
    for i,l in enumerate(list) :
        print(i + 1,l)

    #如果是顾客
    if user_role == "B":
        _user_choose = input("请挑选您想要购买的商品%s："%str_exit)
        if _user_choose == "Q":
            print(welcome)
            exit(0)
        elif len(list) <= 0:
            print("对不起，本商店所有商品都已售罄！")
            continue
        else:
            user_choose = int(_user_choose) - 1
        goods = list[user_choose].split(" ")
        isbuy = input("您选择的商品：{goods}，价格：￥{price}，确定要购买吗？(y/n){exit}"
                      .format(goods = goods[0], price = goods[1], exit = str_exit))
        if isbuy == "y":
            goods_price = float(goods[1])
            if user_balance < goods_price:
                print("对不起，您的余额不足以购买该商品！")
                continue
            user_balance -= goods_price
            bill.append(list[user_choose])
            list.pop(user_choose)
            print("购买成功！您已购买的物品清单如下：")
            for i,b in enumerate(bill):
                print(i + 1, b)
            print("你的余额￥：", user_balance)
        elif isbuy == "Q":
            print(welcome)
            exit(0)
        continue
    #如果是商家
    elif user_role == "A":
        _user_choose = input("请选择您要修改的商品，增加请输入0%s："%str_exit)
        if _user_choose == "Q":
            print(welcome)
            break
        else:
            user_choose = int(_user_choose) - 1
        if user_choose > - 1:
            goods = list[user_choose].split(" ")
            ismodify = input("您选择的商品：{goods}，价格：￥{price}，确定要修改吗？(y/n){exit}"
                             .format(goods=goods[0], price=goods[1], exit = str_exit))
            if ismodify == "Q":
                print(welcome)
                break
            elif ismodify == "y":
                price = input("请输入当前商品价格%s："%str_exit)
                if price == "Q":
                    print(welcome)
                    break
                else:
                    list.pop(user_choose)
                    list.append("%s %s"%(goods[0], price))
        else:
            goods_new = input("请输入商品(格式：商品名称 价格)%s："%str_exit)
            if goods_new == "Q":
                print(welcome)
                break
            else:
                list.append(goods_new + "\n")
        continue
with open(shoping_path, "w", encoding="utf-8") as shoping_list:
    shoping_list.writelines(list)