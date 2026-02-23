cong_viec = []
while True:
    print("\n==== quản lý công việc ====")
    print("1. Danh sách tất cả công việc")
    print("2. Thêm một công việc mới")
    print("3. Hoàn thành công việc")
    print("0. Thoát")
    lua_chon = input("Chọn chức năng: ")
    if lua_chon == "1":
        if len(cong_viec) == 0:
            print("Danh sách công việc trống.")
        else:
            print("Danh sách công việc.")
            for i in range(len(cong_viec)):
                print(f"{i + 1}. {cong_viec[i]}")
    elif lua_chon == "2":
        ten = input("Nhập tên công việc mới: ")
        cong_viec.append(ten)
        print("Đã thêm công việc.")
    elif lua_chon == "3":
        if len(cong_viec) == 0:
            print("Không có công việc nào để hoàn thành.")
        else:
            for i in range(len(cong_viec)):
                print(f"{i + 1}. {cong_viec[i]}")
            so = int(input("Công việc đã hoàn thành: "))
            if 1 <= so <= len(cong_viec):
                print("Đã hoàn thành công việc.")
            else:
                print("Số không hợp lệ")
    elif lua_chon == "0":
        print("Thoát khỏi chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ")
