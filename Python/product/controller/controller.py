from service.service import ProductService

class ProductController:
    def register(self, product):
        service = ProductService()
        service.register(product)

    def getAll(self):
        service = ProductService()
        return service.getAll()

    def update(self, index, name, price):
        service = ProductService()
        service.update(index, name, price)

    def delete(self, index):
        service = ProductService()
        if index==-1:
            print("삭제가 취소되었습니다")
        else:
            service.delete(index)

    def saveData(self):
        service = ProductService()
        service.saveData()

    def loadData(self):
        service = ProductService()
        service.loadData()