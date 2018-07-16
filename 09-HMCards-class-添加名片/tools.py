def show_menu():
    print("*" * 30)
    print()
    print("欢迎使用黑马名片管理系统")
    print()
    print("*" * 30)
    print()
    print("  1. 新建名片")
    print("  2. 显示全部")
    print("  3. 查询名片")
    print("  0. 退出系统")
    print()
    print("*" * 30)


def new_card():
    print("功能：新建名片")
    print("-" * 30)

    # 接收用户的数据
    name = input("请输入姓名")
    phone = input("请输入电话")
    qq = input("请输入QQ")
    email = input("请输入邮箱")

    # 拼字典
    card_dict = dict()
    card_dict["name"] = name
    card_dict["phone"] = phone
    card_dict["qq"] = qq
    card_dict["email"] = email

    # 保存在列表中
    card_list = list()
    card_list.append(card_dict)

    print("保存成功")

def show_all():
    print("功能：显示全部")
    pass


def search_card():
    print("功能：查询名片")
    pass

