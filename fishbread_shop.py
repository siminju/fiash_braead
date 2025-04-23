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
            bread_count = int(input("창고에 채워넣을 개수를 입력하세요: "))
            stock[bread_type] += bread_count
            print(f"{bread_type}의 재고가 {bread_count}개 추가되어, 현재{stock[bread_type]}개 입니다")
        else:
            print("정신을 똑바로 차리시고 현재 {stock}[bread_type]")

def admin_mode():
       while True:
            bread_type = input("주문할 붕어빵을 선택하세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵) 안에 뒤로가길 원하시면 뒤로가기")
            if bread_type == "뒤로가기":
                break
            
    while True:
        password = input("관리자 비밀번호를 입력하세요: ")
        if password == "1234":
            print("관리자 모드에 접속했습니다.")
            break
        else:
            print("비밀번호가 틀렸습니다. 다시 시도하세요.")

    while True:
        action = input("원하는 작업을 선택하세요(재고 확인, 판매 내역 확인, 종료): ")
        if action == "재고 확인":
            print("현재 재고 현황:")
            for bread, count in stock.items():
                print(f"{bread}: {count}개")
        elif action == "판매 내역 확인":
            print("판매 내역:")
            for bread, count in sales.items():
                print(f"{bread}: {count}개")
        elif action == "종료":
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요."

while True:    
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료): ")
    #mode = "종료"
    if mode == "종료":
        break
    elif mode == "주문":
        order_bread()
    elif mode == "관리자":
        admin_mode()


