import os.path
from entity.product import Product

def saveData(products):
    save_file = open("C:/Users/OWNER/Desktop/cloud_msa/cloud_msa_assignment/Python/product/product_data.txt","w")
    for i in range(len(products)):
        save_file.write("{}. 상품명 : {}, 상품가격 : {}\n".format(i+1, products[i].name, products[i].price))
    save_file.close()

def loadData():
    products = []
    
    fileExist = os.path.isfile("C:/Users/OWNER/Desktop/cloud_msa/cloud_msa_assignment/Python/product/product_data.txt")
    if fileExist :
        read_file = open("C:/Users/OWNER/Desktop/cloud_msa/cloud_msa_assignment/Python/product/product_data.txt","r")
        while True:
            data = read_file.readline()
            if not data :
                break
            else :
                data = data.split(sep='.')[1]
                products.append(Product(data.split(sep=',')[0][7:], data.split(sep=',')[1][8:].strip('\n')))
        read_file.close()
    return products