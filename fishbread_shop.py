stock = {
    "팥붕어빵" : 10, 
    "슈크림붕어빵" : 8,
    "초코붕어빵" : 5
}

sales = {
    "팥붕어빵" : 0,
    "슈크림붕어빵" : 0,
    "초코붕어빵" : 0
}

def order_bread ():
    while True: 
        bread_type = input("주문할 붕어빵을 선택하세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵) 안에 뒤로가길 원하시면 뒤로가기")
        if bread_type == "뒤로가기":
            break
        if bread_type in stock:
            bread_count = int(input("주문할 개수를 입력하세요: "))
            if stock[bread_type] >= bread_count: 
                stock[bread_type] -= bread_count
                stock[bread_type] += bread_count
                print(f"{bread_type} {bread_count}개가 판매되었습니다")
            else: 
                print(f"재고가 부족합니다. 현재 {stock[bread_type]}개만 주문 가능합니다.")
        else:
            print("정신을 똑바로 차리시고 현재 {stock}[bread_type]")
while True:    
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료): ")
    #mode = "종료"
    if mode == "종료":
        break
    elif mode == "주문":
        order_bread()
    elif mode == "관리자":
        admin_mode()