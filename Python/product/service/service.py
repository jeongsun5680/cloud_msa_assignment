from dao.product_file import saveData, loadData
from entity.product import Product

class ProductService():
    products=[]

    def register(self, product):
        ProductService.products.append(product)

    def getAll(self):
        return ProductService.products

    def update(self, index, name, price):
        ProductService.products[index].name = name
        ProductService.products[index].price = price

    def delete(self, index):
        ProductService.products.pop(index)

    def saveData(self):
        saveData(ProductService.products)

    def loadData(self):
        ProductService.products = loadData()