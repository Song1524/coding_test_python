shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!

    # 그냥 반복문 돌면서 하나씩 찾는법.
    # 정렬해서 이진탐색으로 찾는법.
    # 반복문이 더 빠를듯
    for order in orders:
        found = False

        for menu in menus:
            if menu == order:
                found = True
                break

        if found == False:
            return False

    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)