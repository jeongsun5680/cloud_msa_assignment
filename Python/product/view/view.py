from entity.product import Product

def menuList():
    print("==== Product Info =====")
    print("1. 상품 정보 목록")
    print("2. 상품 정보 등록")
    print("3. 상품 정보 수정")
    print("4. 상품 정보 삭제")
    print("0. 종료")
    while True:
        menu = input("번호 : ")
        if not menu.isdecimal() :
            print("정수 숫자를 입력하세요")
        elif not 0<=int(menu)<=4 :
            print("0~4 중에 입력하세요")
        else :
            return int(menu)

def productList(products):
    for i in range(len(products)):
        print("{}. 상품명 : {}, 가격 : {}".format(i+1, products[i].name, products[i].price))

def productInput():
    name = input("상품명 : ")
    while True:
        price = input("가격 : ")
        if not price.isdecimal():
            print("숫자로 다시 입력하세요")
        else:
            price = int(price)
            return Product(name, price)

def productUpdate(products):
    while True:
        index = input("수정할 상품 번호 : ")
        if not index.isdecimal():
            print("숫자로 다시 입력하세요")
        elif int(index) not in range(1, len(products)+1):
            print("존재하지 않는 상품번호입니다.")
        else:
            index = int(index)-1
            name = input("상품명 : ")
            while True:
                price = input("가격 : ")
                if not price.isdecimal():
                    print("숫자로 다시 입력하세요")
                else:
                    price = int(price)
                    break
            return (index, name, price)

def productDelete(products):
    while True:
        index = input("삭제할 상품 번호 : ")
        if not index.isdecimal():
            print("숫자로 다시 입력하세요")
        elif int(index) not in range(1, len(products)+1):
            print("존재하지 않는 상품번호입니다.")
        else:
            index = int(index)-1
            yn = input("정말로 삭제하시겠습니까? (y/n) : ")
            if yn in ['y', 'Y']:
                return index
            else:
                return -1